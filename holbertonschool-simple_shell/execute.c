#include "shell.h"

/**
 * execute_command - executes a command
 * @command: command to execute
 */
void execute_command(char *command)
{
	pid_t pid;
	int status;
	char *args[2];
	extern char **environ;

	args[0] = command;
	args[1] = NULL;

	pid = fork();
	if (pid == 0)
	{
		if (execve(command, args, environ) == -1)
		{
			printf("./shell: No such file or directory\n");
			exit(127);
		}
	}
	else if (pid < 0)
	{
		perror("fork");
	}
	else
	{
		waitpid(pid, &status, 0);
	}
}
