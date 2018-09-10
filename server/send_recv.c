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

int		send_data(int fd, char *data, int ebytes)
{
	int		nbytes;
	int		tbytes;
	char	*buf;
	int		i;

	buf = (char*)malloc(sizeof(char) * (ebytes + 1));
	memset(buf, 0, ebytes + 1);
	i = -1;
	while (data && data[++i])
		buf[i] = data[i];
	while (i < ebytes)
		buf[i++] = '#';
	buf[i] = '\0';
	tbytes = 0;
	while (1)
	{
		nbytes = send(fd, buf, ebytes - tbytes, 0);
		if (nbytes <= 0)
		{
			perror("send error\n");
			free(buf);
			return (0);
		}
		tbytes += nbytes;
		if (tbytes >= ebytes)
		{
			free(buf);
			return (strlen(data));
		}
	}
}

char	*recv_data(int fd, int ebytes)
{
	int		nbytes;
	int		tbytes;
	char	*buf;
	char	*data;
	int		i;

	buf = (char*)malloc(sizeof(char) * (ebytes + 1));
	data = (char*)malloc(sizeof(char) * (ebytes + 1));
	memset(buf , 0, ebytes + 1);
	memset(data, 0, ebytes + 1);
	tbytes = 0;
	while (1)
	{
		nbytes = recv(fd, buf, ebytes - tbytes, 0);
		if (nbytes < 0)
		{
			free(buf);
			free(data);
			perror("recv error\n");
			return (NULL);
		}
		if (nbytes == 0)
		{
			free(buf);
			free(data);
			return (NULL);
		}
		buf[nbytes] = '\0';
		tbytes += nbytes;
		// i = -1;
		// while (++i < ebytes && buf[i] != '#')
		// 	;
		// buf[i] = '\0';
		strncat(data, buf, i);
		if (tbytes >= ebytes)
		{
			free(buf);
			return (data);
		}
	}

}