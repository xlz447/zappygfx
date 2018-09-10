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

int		perror_rv(char *errmsg);
char	*genmap(int x, int y);
char	*ft_strjoin(char const *s1, char const *s2);
int		send_data(int fd, char *data, int ebytes);
char	*recv_data(int fd, int ebytes);

#endif
