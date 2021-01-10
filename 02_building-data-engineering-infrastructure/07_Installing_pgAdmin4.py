''' 
- pgAdmin 4 will make managing PostgreSQL much easier if you are new to relational
  databases. The web-based GUI will allow you to view your data and allow you to visually
  create tables. To install pgAdmin 4 we need:

1. to add the repository to Ubuntu. 

    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - 

    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'

    sudo apt update
    
    sudo apt install pgadmin4 pgadmin4-apache2 -y

2. Access via:

  http://127.0.0.1:36251/browser/#
'''