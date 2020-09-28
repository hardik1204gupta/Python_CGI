# Python_CGI
# CGI (To execute RHEL 8 Commands)

CGI (Common Gateway Interface) is a standard way of running programs from a Web server. 
This project is a CGI based web application to get the output of RHEL8 cli commands through client's web browser. This project is user friendly, linux commands can be executed in simple english.

### Working of the project

A reader sends a URL that causes the server to use CGI to run a program. The server passes input from the reader to the 
program and output from the program back to the reader. CGI acts as a "gateway" between the server and the program.
The program run by CGI can be any type of executable file on the server platform(here python program is used).

This diagram shows the working of the project:


![image.png](https://www.tcl.tk/man/aolserver3.0/cgi.gif)

### Use Case
Client can run the basic linux cli commands remotely. WebApp takes the input from user in simple english( i.e., show me the date), and gets the output from the server in the browser only.


### Technologies Used

-- Python3 - Used to interact with OS and create a cgi file 

-- RHEL 8 OS - Used as the server, where the client will request for the commands to be executed

-- Apache Web Server - Used for hosting the Web Services

-- Html - For creation of Web Page to create an interface between user and server and to take input from user


### Requirements to use project

-- Apache web server must be enabled

-- Firewall and selinux must be disabled

-- Html page should be in /var/www/html directory

-- CGI page should be in /var/www/cgi-bin directory

-- URL for client is http://--ip_of_server--/name_of_htmlPage--
 
