# Task 3
After installing docker, I was basically lost, I didn't know anything about how the program works. So all I had with me was our best friend **Google**.

Since we had to host two *static websites*, so I decided to simply implement a workflow only with static websites. Since hosting works with a server, I had to find a way to use a server and host the websites on it using docker. So I first tested out with a basic **Hello World** html file and the apache2 image from docker which uses apache web server. This was a fairly easy task since we ran a single website on a single docker. But the main challenge here is to run both websites  from the same container.

So I did the following steps:
1. Create a new directory and clone both the repositories in that directory:

    `$ mkdir saic_test && cd saic_test/`

    `$ git clone git@github.com:Ritam727/kamandprompt.github.io.git`

    `$ git clone git@github.com:Ritam727/SAIC-Website.git`
2. Create a Dockerfile and configure the commands and server to use:

    `$ nano Dockerfile`

    Inside the editor, I wrote the following lines:

    ```
    FROM ubuntu/apache2:2.4-20.04_beta
    COPY SAIC-Website/. /var/www/saic.example.com
    COPY saic.example.com.conf /etc/apache2/sites-available/
    RUN a2dissite 000-default.conf
    RUN a2ensite saic.example.com
    RUN echo '127.0.0.1 saic.example.com' >> /etc/hosts
    COPY kamandprompt.github.io/. /var/www/kp.example.com
    COPY kp.example.com.conf /etc/apache2/sites-available/
    RUN a2ensite kp.example.com
    RUN echo '127.0.0.1 kp.example.com' >> /etc/hosts
    RUN service apache2 start
    ```
3. Create the files mentioned in the Dockerfile and enter the following lines:

    `$ nano saic.example.com.conf`

    Inside the file enter the following lines and save the file:
    
    ```
    <VirtualHost>
        ServerName saic.example.com
        DocumentRoot /var/www/saic.example.com
    </VirtualHost>
    ```

    `$ nano kp.example.com.conf`

    Inside the editor, enter the following lines and save the file:

    ```
    <VirtualHost>
        ServerName kp.example.com
        DocumentRoot /var/www/kp.example.com
    </VirtualHost>
    ```
4. Change the file called etc/hosts in my **local machine**(this step is necessary):

    `$ sudo nano /etc/hosts`

    Add the following lines to the end of the file:

    ```
    127.0.0.1       saic.example.com
    127.0.0.1       kp.example.com
    ```

    This change ensures that the above domains work in the local system.
5. Then I used `build` command to build the *container*.
    
    `$ sudo docker build -t zblaster/saic_test:latest .`

    This builds the image and makes it ready for publication. For running the image:

    `$ sudo docker run -dit --name saic -p 80:80 zblaster/saic_test:latest`

    This command runs the image on port 80 of the above mentioned domains.

**Saic Website**
![Saic Image](/images/task3_saic.png)

We can see that the SAIC website is up and running on `saic.example.com`

**KamandPrompt Website**
![KamandPrompt Image](/images/task3_kp.png)

We can see that the KamandPrompt website is up and running on `kp.example.com`

Then I published the image to [Docker Hub](https://hub.docker.com):

`$ sudo docker push zblaster/saic_website:latest`

So, if anybody on the internet wants to use it, they can run the docker and then make a few necessary changes to `/etc/hosts` file and they are good to go:

`$ sudo docker run -dit --name <container-name> -p [PORT]:80 zblaster/saic_test:latest`

`$ sudo nano /etc/hosts`

Add the following lines, save the file and close the editor:

```
127.0.0.1       saic.example.com
127.0.0.1       kp.example.com
```

Then the users can check the sites on `saic.example.com:<PORT>` and `kp.example.com:<PORT>`, where `<PORT>` has to be replaced by the port they specified in the command.


---
---


# What I learnt
After completing this challenge, I became a little familiar with docker and docker images, and how most of the static websites are hosted on the internet. Most of the websites run on a server and completing this task, I found myself familiar with how servers are installed and how they work.

# Difficulties faced
After I hosted a basic single website container with docker, I was stuck ( believe me it was for a long time :| ). I couldn't out a way to host multiple websites on the same container. Whenever I searched for something on *Google*, it gave me how to host them on the webservers themselves rather than on docker. So, I had to find out a workaround. I learnt how we set up the apache server for multiple websites using VirtualHost and then applied that indirectly in the docker image.

# References used:
1. A lot of Google searches
2. [Docker documentation](https://docs.docker.com)
