<img src="https://www.tutorialspoint.com/videotutorials/assets/videos/courses/78/images/course_78_image.png">

# 0x05. Processes and signals

### CONCEPTS

A process can be thought of as an instance of a program in execution. We called this an ‘instance of a program’, because if the same program is run lets say 10 times then there will be 10 corresponding processes.

A PID (i.e., process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system.

A process is an executing (i.e., running) instance of a program. Each process is guaranteed a unique PID, which is always a non-negative integer.

The process init is the only process that will always have the same PID on any session and on any system, and that PID is 1. This is because init is always the first process on the system and is the ancestor of all other processes.

A very large PID does not necessarily mean that there are anywhere near that many processes on a system. This is because such numbers are often a result of the fact that PIDs are not immediately reused, in order to prevent possible errors.

What is a signal? Signals are software interrupts.

A robust program need to handle signals. This is because signals are a way to deliver asynchronous events to the application.

A user hitting ctrl+c, a process sending a signal to kill another process etc are all such cases where a process needs to do signal handling.

Linux Signals
In Linux, every signal has a name that begins with characters SIG. For example :

* A SIGINT signal that is generated when a user presses ctrl+c. This is the way to terminate programs from terminal.
* A SIGALRM  is generated when the timer set by alarm function goes off.
* A SIGABRT signal is generated when a process calls the abort function.

### TASKS

0. What is my PID.
Write a Bash script that displays its own PID.
1. List your processes mandatory
Write a Bash script that displays a list of currently running processes.
2. Show your Bash PID mandatory
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
3. Show your Bash PID made easy mandatory
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
4. To infinity and beyond mandatory
Write a Bash script that displays To infinity and beyond indefinitely.
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
Write a Bash script that kills 4-to_infinity_and_beyond process.
6. Kill me now made easy mandatory
Write a Bash script that kills 4-to_infinity_and_beyond process.
7. Highlander mandatory
Write a Bash script that displays:
To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
8. Beheaded process mandatory
Write a Bash script that kills the process 7-highlander.

And 4 advanced tasks.


---

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)

---

## Installation

Copy the code, compile (if is necessary), and execute it.

---

### Setup

---

## Features
## Usage 

See the codes of different functions and programs.

## Documentation 

<a href="https://intranet.hbtn.io/rltoken/FcpEdqz8hau7eEB0Pi8Ong">`Linux PID`</a><br>
<a href="https://intranet.hbtn.io/rltoken/hX_t2YK0erLPbdTq0-uKwQ">`Linux process`</a><br>
<a href="https://intranet.hbtn.io/rltoken/SojW4zvL8j1yaoa7_NM6rA">`Linux signal`</a><br>

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using 

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using. 
---

## Team

https://github.com/Charliemur2

---

## Support

Feel free to contact me!

- GitHub at <a href="https://github.com/Charliemur2">`Charliemur2`</a>
- Twitter at <a href="https://twitter.com/charliesoka">`@charliesoka`</a>
- Insert more social links here.

---

## License

Free Source Code
