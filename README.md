# Dinex
A comprehensive command line application for dealing with anything related to binary numbers. It's designed to be the all-in-one, easy to use, quick to compute program to deal with anything related to networking, like subnets, IP addresses, binary conversions and much more.

The project includes two main branches: main, and main-dev. Main will always only be the up-to-date stable release of the application, while main-dev is the non-stable, but the absolute most up-to-date version.

If any bugs are found, feel free to post them on the discussions page. Most importantly, though, what on earth is Dinex? It's (D)ecimals, b(in)aries and h(ex)adecimals, all in one!

---
## Contents
- [Features](#features)
- [Tips](#tips)
- [Facts](#facts)

---
## Features

Currently supported features:
- Converting decimal numbers to binary and vice versa. Also supports IPv4, IPv6, subnet masks and MAC addresses

Upcoming features:
- Converting decimal numbers to hexadecimal and vice versa. Also supports IPv4, IPv6, subnet masks and MAC addresses
- Converting binary numbers to hexadecimal and vice versa. Also supports IPv4, IPv6, subnet masks and MAC addresses
- Automatically create a chart with subnets, subnetmask, hosts IDs, network IDs and prefix and display it on console. (This will take some time before it's released.)

---
## Tips
The main file in the application, "dinex", is actually a python file, but unconventionally does not have the ".py" extension. This is because it's designed to be a pure commandline tool. Follow the below steps to add it to PATH and use it as any other commandline tools:
- Change directory to the project directory
- `chmod +x dinex`
- `cd ~`
- `echo 'export "PATH=/home/user/project_dir:$PATH" >> [.bashrc, .bash_profile or .profile]'`

---
## Facts
Q: Why bother writing this application when there already are plenty of tools, even websites, out there doing the exact same thing?

A: This project is created as a means of just writing code for fun and for my exams