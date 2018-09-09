#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

#define MAX_X 15
#define MAX_Y 15
#define BUF_SIZE MAX_X*MAX_Y*4+6

// map is in the format:
// X,Y,1001101(0~127)...,#######

static char    *ft_strnew(size_t size)
{
    char *str;

    if (!(str = (char *)malloc(sizeof(char) * (size + 1))))
        return (NULL);
    bzero(str, size + 1);
    return (str);
}

static int    str_size(int n)
{
    int    i;

    i = 1;
    while (n > 9)
    {
        n /= 10;
        i++;
    }
    return (i);
}

char        *ft_itoa(int n)
{
    char    *str;
    int        size;
    int        neg;

    neg = n < 0 ? 1 : 0;
    if (n == -2147483648)
        return (strdup("-2147483648"));
    n = abs(n);
    size = neg + str_size(n);
    str = ft_strnew(size);
    if (!str)
        return (NULL);
    while (size > 0)
    {
        size--;
        str[size] = abs(n % 10) + '0';
        n /= 10;
    }
    if (neg)
        str[0] = '-';
    return (str);
}

char*		gen(int x, int y)
{
	int		i = 0;
	int		j;
	int		r;
	char	b[9];
	int		v;
	int 	total = 0;
	char	out[BUF_SIZE+1];

	strcat(out, ft_itoa(x));
	strcat(out, ",");
	strcat(out, ft_itoa(y));
	strcat(out, ",");
	total += printf("%d,%d,", x, y);
	srand(time(NULL));
	while (i < x * y)
	{
		j = 0;
		while (j < 7)
		{
			if ((r = rand() % 10) < 10)
			{
				if (r > 4)
					b[j] = 1;
				else
					b[j] = 0;
			}
			else
				continue;
			// printf("%d ", 127);
			j++;
		}
		v = b[0]*pow(2, 6) + b[1]*pow(2, 5) + b[2]*pow(2, 4) +
			b[3]*pow(2, 3) + b[4]*pow(2, 2) + b[5]*pow(2, 1) + b[6];
		strcat(out, ft_itoa(v));
		strcat(out, ",");
		total += printf("%d,", v);
		// printf("%d ", v);
		i++;
	}
	while (total < BUF_SIZE)
	{
		strcat(out, "#");
		total+=printf("#");
	}
	printf("\n");
	return (out);
}
