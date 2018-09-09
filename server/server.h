#ifndef SERVER_H
# define SERVER_H

# include <fcntl.h>
# include <stdlib.h>
# include <unistd.h>
# include <stdio.h>
# include <string.h>
# include <sys/types.h>
# include <ctype.h>
# include <sys/time.h>
# include <math.h>
# include <sys/socket.h>
# include <netinet/in.h>
# include <arpa/inet.h>
# include <netdb.h>
# include <errno.h>
# include <sys/select.h>

# define MAP_SIZE 906

# define SOCKET_VARS struct addrinfo hints, *ai; struct protoent *proto;
# define SELECT_VARS fd_set master, read_fds; int fdmax;


int		perror_rv(char *errmsg);
void	send_msg(int fd, char *msg);
void	recv_print(int fd);
char*		gen(int x, int y);
#endif
