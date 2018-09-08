/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   norm_server.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zfeng <zfeng@student.42.us.org>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/08/31 14:54:00 by zfeng             #+#    #+#             */
/*   Updated: 2018/09/07 17:14:33 by zfeng            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "server.h"


int		perror_rv(char *errmsg)
{
	write(2, errmsg, strlen(errmsg));
	return (EXIT_FAILURE);
}

/*
** get sockaddr, IPv4 or IPv6
*/

void	*get_in_addr(struct sockaddr *sa)
{
	if (sa->sa_family == AF_INET)
		return (&(((struct sockaddr_in*)sa)->sin_addr));
	return (&(((struct sockaddr_in6*)sa)->sin6_addr));
}

/*
** iterate through the return link list of sockets from getaddrinfo()
*/

int		s_iter_sock(struct addrinfo *ai, struct protoent *proto, int reuse)
{
	struct addrinfo *p;
	int				listener;

	p = ai;
	while (p)
	{
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
		break ;
	}
	if (p == NULL)
		return (-1);
	freeaddrinfo(ai);
	return (listener);
}

/*
** create a listener socket
*/

int		s_create_socket(void)
{
	int		listener;
	int		rv;
	int		reuse = 1;

	SOCKET_VARS;
	proto = getprotobyname("tcp");
	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags = AI_PASSIVE;
	if ((rv = getaddrinfo(NULL, "4242", &hints, &ai)) != 0)
		perror_rv((char*)gai_strerror(rv));
	listener = s_iter_sock(ai, proto, reuse);
	return (listener);
}


char	*read_map(char *filename)
{
	int		fd;
	char	buf[MAP_SIZE + 1];
	char	map[MAP_SIZE + 1];
	int		nbytes;

	if ((fd = open(filename, O_RDONLY)) < 0)
		perror("open error\n");
 	while ((nbytes = read(fd, buf, MAP_SIZE)) > 0)
 	{
 		buf[nbytes] = '\0';
 		strncpy(map, buf, nbytes);
 	}
 	map[MAP_SIZE] = '\0';
 	// printf("%s", map);
 	return (map);
}


int		main(int ac, char **av)
{
	int						listener;
	int						newfd;
	socklen_t				addrlen;
	struct sockaddr_storage	remoteaddr;
	char					remote_ip[INET6_ADDRSTRLEN];
	char					*map;

	SELECT_VARS;
	listener = s_create_socket();
	if (listen(listener, 42) == -1)
		return (EXIT_FAILURE);
	addrlen = sizeof(remoteaddr);
	if ((newfd = accept(listener, (struct sockaddr *)&remoteaddr, &addrlen)) == -1)
		perror("accept");
	// printf("new connection from %s on socket %d\n",
	// 		inet_ntop(remoteaddr.ss_family, 
	// 			get_in_addr((struct sockaddr*)&remoteaddr), 
	// 			remote_ip, INET6_ADDRSTRLEN), newfd);
	map = read_map("10x10.map");
	// printf("%lu\n%s\n", strlen(map), map);
	send_msg(newfd, map);
	return (0);
}

