/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   send_recv.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zfeng <zfeng@student.42.us.org>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/07 18:25:18 by zfeng             #+#    #+#             */
/*   Updated: 2018/09/07 18:40:41 by zfeng            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "server.h"

void	send_msg(int fd, char *msg)
{
	int		nbytes;
	int		tbytes;
	char	buf[MAP_SIZE];
	int		i;

	// printf("server inital msg = |% s|\n", msg);
	i = 0;
	while (msg[i])
	{
		buf[i] = msg[i];
		i++;
	}
	while (i < MAP_SIZE)
	{
		buf[i] = '#';
		i++;
	}
	buf[i] = '\0';
	tbytes = 0;
	while (tbytes < MAP_SIZE)
	{
		nbytes = send(fd, buf, MAP_SIZE - tbytes, 0);
		// nbytes = send(fd, buf, MAP_SIZE, 0);
		if (nbytes < 0)
		{
			perror("send error\n");
			return ;
		}
		tbytes += nbytes;
		if (tbytes >= MAP_SIZE)
		{
			// printf("server send msg = |%s|\n", buf);
			memset(buf, 0, MAP_SIZE);
			return ;
		}
	}
}

void	recv_print(int fd)
{
	int		nbytes;
	int		tbytes;
	char	buf[MAP_SIZE + 1];
	char	msg[MAP_SIZE + 1];
	int		i;

	tbytes = 0;
	while (tbytes < MAP_SIZE)
	{
		nbytes = recv(fd, buf, MAP_SIZE - tbytes, 0);
		// nbytes = recv(fd, buf, MAP_SIZE, 0);
		if (nbytes < 0)
		{
			perror("recv error\n");
			return ;
		}
		if (nbytes == 0)
		{
			printf("sending done\n");
			return ;
		}
		buf[nbytes] = '\0';
		printf("client recv msg = |%s|\n", buf);
		tbytes += nbytes;
		i = 0;
		while (i < MAP_SIZE)
		{
			if (buf[i] == '#')
				buf[i] = '\0';
			i++;
		}
		strncpy(msg, buf, i);
		if (tbytes >= MAP_SIZE)
		{
			msg[MAP_SIZE] = '\0';
			printf("client unpad msg = |%s|\n", msg);
			break ;
		}
	}
	
}