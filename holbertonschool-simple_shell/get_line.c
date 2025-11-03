#include "shell.h"

/**
 * get_line - gets a line from stdin
 *
 * Return: line from stdin
 */
char *get_line(void)
{
	char *line = NULL;
	size_t bufsize = 0;
	ssize_t len;

	len = getline(&line, &bufsize, stdin);
	if (len == -1)
	{
		free(line);
		return (NULL);
	}

	if (len > 0 && line[len - 1] == '\n')
		line[len - 1] = '\0';

	return (line);
}
