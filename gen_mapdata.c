#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_X 15
#define MAX_Y 15
#define BUF_SIZE MAX_X*MAX_Y*4+6

// map is in the format:
// X,Y,1001101(0~127)...,#######

int		main(int ac, char **av)
{
	int		x = atoi(av[1]);
	int		y = atoi(av[2]);
	int		i = 0;
	int		j;
	int		r;
	char	b[9];
	int		v;
	int 	total = 0;

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
		total += printf("%d,", v);
		// printf("%d ", v);
		i++;
	}
	while (total < BUF_SIZE)
	{
		total+=printf("#");
	}
	printf("total:|%i|\n", total);
	return (0);
}