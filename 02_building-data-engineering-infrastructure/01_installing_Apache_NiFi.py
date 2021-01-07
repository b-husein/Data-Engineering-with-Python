
# INSTALLING AND CONFIGURING APACHE NIFI

''' 
    Apache Nifi is the primary tool (in this book) for building data engineering pipelines.
    NiFi allows you to build data pipelines using prebuilt processors that you can configure
    for your needs. It also provides a scheduler to set how frequently you would like your 
    pipelines to run. In addition, it will handle backpressure - if one task works faster
    than another, you can slow down the task.

    To install Apache NiFi, you will need to dowload it from: 
    https://nifi.apache.org/download.html:

        1. By using curl and command line:
        curl https://mirrors.estointernet.in/apache/nifi/1.12.1/nifi-1.12.1-bin.tar.gz

        (addendum) if curl is not install, we can install it via:
        sudo apt install curl

        2. Extract the NiFi files from the .tar.gz using the following command:
        tar xvzf nifi.tar.gz

        3. You will now have a folder named nifi-1.12.1. You can run NiFi by executing
        the following from inside the folder:
        bin/nifi.sh start

        4. If you already have Java installed and configured, when you run the status tool
        as shown in the following snippet, you will see a path set for JAVA_HOME:
        sudo bin/nifi.sh status

        5. If you do not see JAVA_HOME set, you may need to install JAVA using the following
        command:
        sudo apt install openjdk-11-jre-headless

        6. Then you should edit .bash_profile to include the following line so that NiFi can 
        find the JAVA_HOME variable:
        export JAVA_HOME=/usr/lib/jvm/java11-openjdk-amd64

        7. Lastly, reload .bash_profile:
        source .bash_profile

        8. When you run for the status on NiFi, you should now see a path for JAVA_HOME:
        sudo nifi*/bin/nifi.sh start

        Java home: /usr/lib/jvm/java-1.11.0-openjdk-amd64
        NiFi home: /home/paulcrickard/nifi-1.11.3

        Bootstrap Config File: /home/paulcrickard/nifi-1.11.3/conf/bootstrap.conf

        9. When NiFi is ready, which may take a minute, open your web browser and 
        go to: 
        http://localhost:8080/nifi/

        In later chapters, you will learn about many of the available configurations
        for NiFi, but for now, you will only change the port NiFi runs on.
        In conf/nifi.properties change nifi.web.http.port=8080 under the web properties
        heading to 9300 as  shown:

        # web properties #
        nifi.web.http.port=9300

        if your firewall is on, you may need to open the port:
        sudo ufw allow 9300/tcp

        Now you can relaunch NiFi and view the GUI at:
        http://localhost:9300/nifi/


'''

''' 
 - Additional notes related to JAVA_HOME path setting:
    - sudo gedit /etc/profile
    - JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
    - export JAVA_HOME
    - export PATH=$PATH:$JAVA_HOME/bin


    - Start in terminal:
    /Downloads/nifi-1.12.1$ bin/nifi.sh start

    - Browser:
    http://localhost:9300/nifi/
'''