/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   norm_server.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zfeng <zfeng@student.42.us.org>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/08/31 14:54:00 by zfeng             #+#    #+#             */
/*   Updated: 2018/09/02 19:55:41 by zfeng            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "server_client.h"

t_player	g_players[MAX_FD];
t_team		g_teams[MAX_TEAM];

void	s_add_to_team(char *team_name, int fd, int nb_client)
{
	int		i;

	i = 0;
	while (*g_teams[i].team_name)
	{
		if (strcmp(g_teams[i].team_name, team_name) == 0)
		{
			if (g_teams[i].nb_client == 0)
				return ;
			g_teams[i].nb_client--;
			return ;
		}
		i++;
	}
	g_teams[i].team_id = i;
	strcpy(g_teams[i].team_name, team_name);
	g_teams[i].nb_client = nb_client;
	g_players[fd].fd = fd;
	g_players[fd].team_id = i;
}

/*
int		s_get_team_id(char *team_name)
{
	int		i;

	i = 0;
	if (*g_teams[i].team_name)
		return (0);
	while (i < MAX_TEAM)
	{
		if (strcmp(g_teams[i].team_name, team_name) == 0)
			return (i);
		i++;
	}
	return (-1);
}
*/

void	s_clear_player(int fd)		// clear the player data when a client is terminated
{
	g_players[fd].nb_req = 0;
	memset(g_players[fd].inventory, 0, 7);
	memset(g_players[fd].pos, 0, 2);
	g_players[fd].level = 0;
}


// get sockaddr, IPv4 or IPv6:
void *get_in_addr(struct sockaddr *sa)
{
    if (sa->sa_family == AF_INET)
        return &(((struct sockaddr_in*)sa)->sin_addr);
    return &(((struct sockaddr_in6*)sa)->sin6_addr);
}

int		create_socket(char *port)
{ 
    int 			listener;
    struct addrinfo hints, *ai, *p;
	struct protoent	*proto;
	int				reuse;
	int				rv;
	
	proto = getprotobyname("tcp");
	reuse = 1;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE;
    if ((rv = getaddrinfo(NULL, port, &hints, &ai)) != 0) 
	{
        fprintf(stderr, "selectserver: %s\n", gai_strerror(rv));
        return (EXIT_FAILURE);
	}
	p = ai;
	while (p)
	{
		//listener = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
		listener = socket(p->ai_family, p->ai_socktype, proto->p_proto);
		if (listener < 0)
		{
			p = p->ai_next;
			continue;
		}
		setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(int));
		if (bind(listener, p->ai_addr, p->ai_addrlen) < 0)
		{
			close(listener);
			continue;
		}
		break;
	}	
    if (p == NULL)
	{
        fprintf(stderr, "selectserver: failed to bind\n");
        return (EXIT_FAILURE);
    }
    freeaddrinfo(ai);
	return (listener);
}


int		main(int ac, char **av)
{
    fd_set master;    // master file descriptor list
    fd_set read_fds;  // temp file descriptor list for select()
    int fdmax;        // maximum file descriptor number

    int listener;     // listening socket descriptor
    int newfd;        // newly accept()ed socket descriptor
    struct sockaddr_storage remoteaddr; // client address
    socklen_t addrlen;

    char buf[BUF_SIZE];    // buffer for client data
    int nbytes;

    char remoteIP[INET6_ADDRSTRLEN];

    int i, j;

    FD_ZERO(&master);    // clear the master and temp sets
    FD_ZERO(&read_fds);

	listener = create_socket(av[1]); 

    // listen
    if (listen(listener, 42) == -1) 
	{
        perror("listen");
        exit(3);
    }

    // add the listener to the master set
    FD_SET(listener, &master);

    // keep track of the biggest file descriptor
    fdmax = listener; // so far, it's this one


	t_cmdq	*cmdq;
	cmdq = NULL;
	
    // main loop
    while (1)
	{
		memcpy(&read_fds, &master, sizeof(master));
		if (select(fdmax + 1, &read_fds, NULL, NULL, NULL) == -1)
		{
			perror("select");
			exit(4);
		}
		i = 0;
		while (i <= fdmax)
		{
			//printf("server side buf = |%s|\n", buf);
			if (FD_ISSET(i, &read_fds))
			{
				if (i == listener)
				{
					addrlen = sizeof(remoteaddr);
					if ((newfd = accept(listener, (struct sockaddr *)&remoteaddr, &addrlen)) == -1)
						perror("accept");
					//send(newfd, "WELCOME 🙂\n", 13, 0);
					send(newfd, WELCOME_MSG, strlen(WELCOME_MSG), 0);
					if ((nbytes = recv(newfd, buf, BUF_SIZE, 0)) < 0)
						perror(strerror(errno));
					buf[nbytes] = '\0';
					s_add_to_team(buf, newfd, 3);
					if (g_teams[g_players[newfd].team_id].nb_client == 0)
					{
						send(newfd, TEAM_FULL_MSG, strlen(TEAM_FULL_MSG), 0);
						close(newfd);
					}
					else
					{
						FD_SET(newfd, &master);
						if (newfd > fdmax)
							fdmax = newfd;
						printf("%d\n", g_teams[g_players[newfd].team_id].nb_client);
						printf("x: | y: \n");
						send(newfd, "joined team", 11, 0);
						printf("selectserver: new connection from %s on socket %d\n",
								inet_ntop(remoteaddr.ss_family, 
									get_in_addr((struct sockaddr*)&remoteaddr), 
									remoteIP, INET6_ADDRSTRLEN), newfd);
					}
				}
				else
				{
					if ((nbytes = recv(i, buf, BUF_SIZE, 0)) <= 0)
					{
						if (nbytes == 0)
						{
							s_clear_player(i);
							printf("selectserver: socket %d hung up\n", i);
						}
						else
							perror("recv");
						close(i);
						FD_CLR(i, &master);
					}
					else
					{
						if (g_players[i].nb_req < 11)
						{
							buf[nbytes] = '\0';
							printf("nb_req = %d\n", g_players[i].nb_req);
							//enqueue(&cmdq, i, buf);
							g_players[i].nb_req++;
							printf("%d bytes received: |%s|\n", nbytes, buf);
							memset(buf, 0, strlen(buf));
						}
					}
				}
			}
			i++;
		}
	}
    
    return (0);
}
