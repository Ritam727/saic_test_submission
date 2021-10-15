# Task 3
After installing docker, I was basically lost, I didn't know anything about how the program works. So all I had with me was our best friend **Google**.

Since we had to host two *static websites*, so I decided to simply implement a workflow only with static websites. Since hosting works with a server, I had to find a way to use a server and host the websites on it using docker. So I first tested out with a basic **Hello World** html file and the httpd image from docker which uses apache web server.

I used the following steps to run the websites mentioned to run the SAIC-Website:
1. Forked and cloned the repositories in my local system:
    
    `$ git clone git@github.com:Ritam727/SAIC-Website.git`
2. Created a Dockerfile mentioning the required packages to use a webserver(in my case its httpd image from docker which uses apache):

    `$ cd SAIC-Website/`
    
    `$ nano Dockerfile`

    Inside the editor I wrote the following lines:
    ```
    FROM httpd:2.4
    COPY . /usr/local/apache2/htdocs/
    ```
    What this code does is simple, it installs the httpd package and copies the files from the working directory to the `/usr/local/apache2/htdocs` directory in server system.
3. Then I ran created the image file using the `build` command of docker:

    `$ sudo docker build -t <user-name>/<image-name>:[TAG] .`

    For my case, I used the following command:

    `$ sudo docker build -t zblaster/saic_website:latest .`

    This creates a docker image with the name zblaster/saic_website and tags it latest.
4. Then I created a container using the `run` command that uses the image we just created and hosts the site on the server:

    `$ sudo docker run -dit --name <container-name> -p [PORT_ON_LOCALHOST]:80 <user-name>/<image-name>:[TAG]`

    For my case, the following command was used:

    `$ sudo docker run -dit --name saic_website -p 1234:80 zblaster/saic_website:latest`

    This basically sets up the server and hosts the website on the server. In my case, the server would be hosted on `http://localhost:1234`.
5. Then to publish the image, I used the `push` command of docker to push the repository to [Docker hub](https://hub.docker.com) on my repository:

    `$ docker push <user-name>/<package-name>:[TAG]`

    In my case the command was:

    `$ docker push zblaster/saic_website:latest`

    This published the image file on the web and anyone who wishes to test the server can first install apache2 and start the process and then use the following command to clone the package to run the server:

    `$ sudo docker run -dit --name <container-name> -p [PORT]:80 zblaster/saic_website:latest`

The steps to run the Kamandprompt website were similar. The only changes were in the *package-name* in the commands and the port I used was `1235` instead of `1234`, since the former was already running in port `1234`. The package-name is kp_website.

**Saic Website**

![Saic_Website](/images/task3_saic.png)

**Kamandprompt Website**
![Kp_Website](/images/task3_kp.png)

---
---

Performing this task, I came to learn about what the **docker**  program does and how to use it. It is basically used for creating *Containers* to ship applications to test them out before publishing it. We can test out the look and feel of Operating Systems before deploying them with a kernel, or test out websites by hosting them locally. In this task we were to host two websites locally, which we can easily do within a few minutes if the website is ready. This helps us to test out how the website would look and function in a web server using the same application that we use in the *Container*. In our case its an apache server, which is one of the most commonly used web servers. I did not use that directly in the container, instead I used httpd, which is available as a docker image and uses apache to host the website.

References used:
1. Google
2. [Docker Documentation](https://docs.docker.com)
3. [httpd Documentation](https://hub.docker.com/_/httpd)
