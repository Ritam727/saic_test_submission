# Task 3
After installing docker, I was basically lost, I didn't know anything about how the program works. So all I had with me was our best friend **Google**.

Since we had to host two *static websites*, so I decided to simply implement a workflow only with static websites. Since hosting works with a server, I had to find a way to use a server and host the websites on it using docker. So I first tested out with a basic **Hello World** html file and the apache2 image from docker which uses apache web server. This was a fairly easy task since we ran a single website on a single container. But the main challenge here wass to run both websites from the same container.

So I searched for some workarounds. I found out that it is possible to set up virtual hosts with a webserver and use different ports on the same ip address for two different websites.I used ubuntu/apache2 image from docker to run the server. The process I followed is described in the following steps:
1. Clone both the repositories in a common directory:
    
    `$ mkdir saic && cd saic/`

    `$ git clone git@github.com:Ritam727/SAIC-Website.git`

    `$ git clone git@github.com:Ritam727/kamandprompt.github.io.git`
2. Create a configuration file for the webserver, set up two ports for two websites:
    
    `$ nano saic_test.conf`

    Inside the editor, I wrote the following lines, saved and quit the editor:

    ```
    <VirtualHost *:80>
        ServerName localhost
        DocumentRoot /var/www/saic_website
    </VirtualHost>

    Listen 81
    <VirtualHost *:81>
        ServerName localhost
        DocumentRoot /var/www/kp_website
        Redirect permanent /blog http://blog.pc.iitmandi.co.in
    </VirtualHost>
    ```

    The `Listen 81` command is necessary to instantiate the port 81 and the `Redirect permanent /blog http://blog.pc.iitmandi.co.in` is necessary to redirect the link to the designated site.
3. Create the Dockerfile:

    `$ nano Dockerfile`

    Inside the editor, I wrote the following lines:

    ```
    FROM ubuntu/apache2:2.4-20.04_beta
    COPY SAIC-Website/. /var/www/saic_website
    COPY kamandprompt.github.io/. /var/www/kp_website
    COPY saic_test.conf /etc/apache2/sites-available/
    RUN a2ensite saic_test
    RUN service apache2 start
    ```

    This file would be used to run the create the docker image.
4. Build the docker image and test it locally:
    
    The following command is used to generate an image for your user id in docker hub and use the Dockerfile created:
    
    `$ sudo docker build -t <user-name>/<package-name>:[TAG] .`

    In my case, the command was:
    
    `$ sudo docker build -t zblaster/saic:latest .`

    Then, to run the image in a container, the following command is used:

    `$ sudo docker run -dit <other-flags> <user-name>/<package-name>:[TAG]`

    In my case the following command was used:

    `$ sudo docker run -dit --name saic -p 8080:80 -p 8081:81 zblaster/saic:latest`

    This binds the port 8080 of localhost to 80 of the container and 8081 of localhost to 81 of container. So the SAIC website would be hosted on `localhost:8080` and the KamandPrompt website on `localhost:8081`.

    ![Saic Website](/images/task3_saic.png)
    We can see that the SAIC website is up and running on `localhost:8080`.

    ![KamandPrompt Website](/images/task3_kp.png)
    We can see that the KamandPrompt website is up and running on `localhost:8081`.
5. Publishing the docker image and commands to be used by other users if the they want to use the image:
    
    `$ sudo docker push zblaster/saic:latest`

    This publishes the image to [Docker hub](https://hub.docker.com).

    For other users, they can run the image locally using the following command:

    `$ sudo docker run -dit --name [container-name] -p [PORT1]:80 -p [PORT2]:81 zblaster/saic:latest`

    Replace *container-name* with whatever they like, *PORT1* and *PORT2* with whichever port they find suitable. Then the SAIC and KamandPrompt websites would be hosted on `localhost:PORT1` and `localhost:PORT2` respectively.
[Docker Image link on docker hub](https://hub.docker.com/repository/docker/zblaster/saic)

---
---


# What I learnt
After completing this challenge, I became a little familiar with docker and docker images, and how most of the static websites are hosted on the internet. Most of the websites run on a server and completing this task, I found myself familiar with how servers are installed and how they work.

# Difficulties faced
After I hosted a basic single website container with docker, I was stuck ( believe me it was for a long time :| ). I couldn't find out a way to host multiple websites on the same container. Whenever I searched for something on *Google*, it gave me how to host them on the webservers themselves rather than on docker. So, I had to find out a workaround. I learnt how we set up the apache server for multiple websites using VirtualHost and then applied that indirectly in the docker image.

# References used:
1. A lot of Google searches
2. [Docker documentation](https://docs.docker.com)
