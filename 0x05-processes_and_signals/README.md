# *0x05. Processes and signals*

`DevOps`   `Shell`   `Bash`   `Syscall`   `Scripting`

By: Sylvain Kalache

## *Resources:*

Read or watch:

- [Linux PID](https://www.linfo.org/pid.html)
- [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
- [Linux signal](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
- [Process management in linux](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)

man or help:

- `ps`
- `pgrep`
- `pkill`
- `kill`
- `exit`
- `trap`

## *General:*

- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## *More Info:*

For those who want to know more and learn about all signals, check out [this article](https://www.computerhope.com/unix/signals.htm).

## *Tasks:*

#### [0. What is my PID](0-what-is-my-pid)

Write a Bash script that displays its own PID.

#### [1. List your processes](1-list_your_processes)

Write a Bash script that displays a list of currently running processes.

Requirements:

- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

#### [2. Show your Bash PID](2-show_your_bash_pid)

Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

Requirements:

- You cannot use `pgrep`
- The third line of your script must be `# shellcheck disable=SC2009` (for more info about ignoring `shellcheck` error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))


#### [3. Show your Bash PID made easy](3-show_your_bash_pid_made_easy)

Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

Requirements:

- You cannot use `ps`

Here we can see that:

- For the first iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4555`
- For the second iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4557`


#### [4. To infinity and beyond](4-to_infinity_and_beyond)

Write a Bash script that displays `To infinity and beyond` indefinitely.

Requirements:

In between each iteration of the loop, add a `sleep 2`

#### [5. Don't stop me now!](5-dont_stop_me_now)

We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.

Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:

- You must use `kill`


I opened 2 terminals in this example, started by running my `4-to_infinity_and_beyond` Bash script in terminal #0 and then moved on terminal #1 to run `5-dont_stop_me_now`. We can then see in terminal #0 that my process has been terminated.

    
#### [6. Stop me if you can](6-stop_me_if_you_can)

Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:

- You cannot use `kill` or `killall`

#### [7. Highlander](7-highlander)

Write a Bash script that displays:

- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a `SIGTERM` signal

Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

I started `7-highlander` in Terminal #0 and then run `67-stop_me_if_you_can` in terminal #1, for every iteration we can see `I am invincible!!!` appearing in terminal #0.

#### [8. Beheaded process](8-beheaded_process)

Write a Bash script that kills the process `7-highlander`.

I started `7-highlander` in Terminal #0 and then run `8-beheaded_process` in terminal #1 and we can see that the `7-highlander` has been killed.

#### [9. Process and PID file](100-process_and_pid_file)

Write a Bash script that:

- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a SIGTERM signal
- Displays `Y U no love me?!` when receiving a SIGINT signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

![d8ecfe9109334898b9540ffd20cf64d1c06f0c09](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/83cef324-e167-49b5-aab0-244bfe057085)

Executing the `100-process_and_pid_file` script and killing it with `ctrl+c`.
Starting `100-process_and_pid_file` in the terminal #0 and then killing it in the terminal #1.

#### [10. Manage my process](101-manage_my_process)

![37975393ead381f4d27f268f7337c6d3013b4991](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/f824bf9d-f838-44a6-9bc8-49c55a916d01)

Read:

- [&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
- [init.d](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
- [Daemon](https://en.wikipedia.org/wiki/Daemon_%28computing%29)
- [Positional parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

man: `sudo`

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: `start`, `restart` and `stop`. The most popular way of doing so on Unix system is to use the init scripts.

Write a `manage_my_process` Bash script that:

- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
- In between every `I am alive!` message, the program should pause for 2 seconds

Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. (both files need to be pushed to git)

Requirements:

- When passing the argument start:
   - Starts `manage_my_process`
   - Creates a file containing its PID in `/var/run/my_process.pid`
   - Displays `manage_my_process` started
- When passing the argument stop:
   - Stops `manage_my_process`
   - Deletes the file `/var/run/my_process.pid`
   - Displays `manage_my_process` stopped
- When passing the argument restart
   - Stops `manage_my_process`
   - Deletes the file `/var/run/my_process.pid`
   - Starts `manage_my_process`
   - Creates a file containing its PID in `/var/run/my_process.pid`
   - Displays `manage_my_process` restarted
- Displays Usage: `manage_my_process` `{start|stop|restart}` if any other argument or no argument is passed

Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started.

 
#### [11. Zombie](102-zombie.c)

![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/255/C6mO7b3.jpg)

Read [what a zombie process is](https://zombieprocess.wordpress.com/what-is-a-zombie-process/).

Write a C program that creates 5 zombie processes.

Requirements:

- For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
- Your code should use the `Betty style`. It will be checked using `betty-style.pl` and `betty-doc.pl`
- When your code is done creating the parent process and the zombies, use the function bellow
```
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```
In Terminal #0, I start by compiling `102-zombie.c` and executing `zombie` which creates 5 zombie processes. In Terminal #1, I display the list of processes and look for lines containing `Z+.*<defunct>` which catches zombie process.

