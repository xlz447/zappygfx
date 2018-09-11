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
	char	*map;
	int		nbytes;

	map = (char*)malloc(sizeof(char) * (MAP_SIZE + 1));
	if ((fd = open(filename, O_RDONLY)) < 0)
		perror("open error\n");
 	while ((nbytes = read(fd, buf, MAP_SIZE)) > 0)
 	{
 		buf[nbytes] = '\0';
 		strncat(map, buf, nbytes);
 	}
 	map[MAP_SIZE] = '\0';
 	return (map);
}


char	*player_data0 =	"00,00,03,03,1,02,03,04,05,06,03,99\n"
						"01,00,04,04,1,02,03,04,05,06,03,99\n"
						"02,00,05,05,3,02,03,04,05,06,03,99\n";
char	*player_data1 =	"00,00,03,04,3,02,03,04,05,06,03,99\n"
						"01,00,04,05,1,02,03,04,05,06,03,99\n";
char	*player_data2 =	"00,00,04,04,4,02,03,04,05,06,03,99\n"
						"01,00,04,06,1,02,03,04,05,06,03,99\n"
						"02,00,07,05,3,02,03,04,05,06,03,99\n";
char	*player_data3 =	"00,00,04,03,2,02,03,04,05,06,03,99\n"
						"01,00,04,07,1,02,03,04,05,06,03,99\n"
						"02,00,08,05,3,02,03,04,05,06,03,99\n"
						"03,00,09,09,1,02,03,04,05,06,03,99\n";


int		main(int ac, char **av)
{
	int						listener;
	int						newfd;
	socklen_t				addrlen;
	struct sockaddr_storage	remoteaddr;
	char					remote_ip[INET6_ADDRSTRLEN];
	char					*map;
	static int				move = 0;
	char					*data;

	listener = s_create_socket();
	if (listen(listener, 42) == -1)
		return (EXIT_FAILURE);
	addrlen = sizeof(remoteaddr);
	if ((newfd = accept(listener, (struct sockaddr *)&remoteaddr, &addrlen)) == -1)
		perror("accept");

	while (1)
	{
		map = genmap(10,10);
		switch (move++ % 4) {
			case 0:
				data = ft_strjoin(map, "\n");
				data = ft_strjoin(data, player_data0);
				data = ft_strjoin(data, "@");
				send_data(newfd, data, strlen(data));
				break;
			case 1:
				data = ft_strjoin(map, "\n");
				data = ft_strjoin(data, player_data1);
				data = ft_strjoin(data, "@");
				send_data(newfd, data, strlen(data));
				break;
			case 2:
				data = ft_strjoin(map, "\n");
				data = ft_strjoin(data, player_data2);
				data = ft_strjoin(data, "@");
				send_data(newfd, data, strlen(data));
				break;
			case 3:
				data = ft_strjoin(map, "\n");
				data = ft_strjoin(data, player_data3);
				data = ft_strjoin(data, "@");
				send_data(newfd, data, strlen(data));
				break;
	}

		sleep(1);
	}
	return (0);
}
