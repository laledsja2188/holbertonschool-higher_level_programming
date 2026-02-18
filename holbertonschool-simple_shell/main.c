#include "shell.h"

/**
 * main - main function for simple shell
 *
 * Return: 0
 */
int main(void)
{
	char *line;
	int keep_going = 1;

	while (keep_going)
	{
		printf("#cisfun$ ");
		fflush(stdout);
		line = get_line();
		if (line == NULL)
		{
			printf("\n");
			break;
		}
		if (strlen(line) > 0)
			execute_command(line);
		free(line);
	}
	return (0);
}
