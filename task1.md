# Task 1
I was unable to complete this task completely. I was able to see the website hosted and locate the directories located in the port. After installing VirtualBox and loading up the `hackme.ova` file, I changed the network adapter to `NAT` and then started up the VM.

I followed the following steps:
1. After the VM loaded, I ran `nmap` on localhost to check which ports were open. I ran the following command:

    `$ sudo nmap -sV localhost`

    The output was:

    ```
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.0000050s latency).
    Not shown: 994 closed ports
    PORT     STATE SERVICE VERSION
    25/tcp   open  smtp    Sendmail 8.15.2/8.15.2/Debian-18
    80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
    587/tcp  open  smtp    Sendmail 8.15.2/8.15.2/Debian-18
    631/tcp  open  ipp     CUPS 2.3
    5678/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
    5679/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
    ```

    So I checked for ports `80` and `5678` on localhost. The website was hosted on `5678`.

    ![The Website](/images/hackme.png)

2. I used `nikto` to scan for routes in the port:

    `$ sudo nikto -h localhost -p 5678`

    The output was:

    ```
    - Nikto v2.1.5
    ---------------------------------------------------------------------------
    + Target IP:          127.0.0.1
    + Target Hostname:    localhost
    + Target Port:        5678
    + Start Time:         2021-10-18 11:23:08 (GMT5.5)
    ---------------------------------------------------------------------------
    + Server: Apache/2.4.18 (Ubuntu)
    + Server leaks inodes via ETags, header found with file /, fields: 0xb7 0x5c8cc3a175320 
    + The anti-clickjacking X-Frame-Options header is not present.
    + No CGI Directories found (use '-C all' to force check all possible dirs)
    + Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
    + OSVDB-3268: /files/: Directory indexing found.
    + OSVDB-3092: /files/: This might be interesting...
    + OSVDB-3233: /icons/README: Apache default file found.
    + 6544 items checked: 0 error(s) and 6 item(s) reported on remote host
    + End Time:           2021-10-18 11:23:16 (GMT5.5) (8 seconds)
    ---------------------------------------------------------------------------
    + 1 host(s) tested
    ```
    
    So I checked for `localhost:5678/files/` route:

    ![files/ Directory](/images/task1_files.png)

    ![site.html](/images/task1_site_html.png)

I couldn't progress any further, I did a lot of google searches but I reached the end of the cliff and couldn't find a workaround. So, I stopped at this point.

---
---

# What I learnt
Use of `nikto` to search for routes and directories in a port and use of basic `nmap` command to scan for ports on localhost.

# Difficulties faced
I was stuck at every point in this task, so I would say the whole task was difficult for me :|. I couldn't find out a way to connect `localhost` to the VM, had to look up for it on google to find proper configuration. I didn't know how to list directories in a route, so I made around a hundred google searches to find a tool :'), which was `nikto` for me. The main challenge was to find vulnerabilities in the website to enter into the server, I couldn't find a way to do that.

# References used
Google
