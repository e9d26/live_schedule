# live_schedule
**Attention!**  
**_this application is being created, and not finished!_**

this is the application that shows list of commedy live schedule.

##  Architecture overview
1. Scrape live schedule information from several web sites.
2. Store that information into database as same format.
3. Create pages that shows live schedule.
4. Return proper page to each request.

![ws000359](https://user-images.githubusercontent.com/35652396/35775753-3c472f82-09d2-11e8-87fb-abc49b99c69a.JPG)

##  Tools to realize this architecture
1. Requests/BeautifulSoup  
    →**Web scraping**
2. Django  
    →**Web application**

## Environment
* AmazonLinux1
* Apache  2.2.34
* python  3.6.4
* django  2.0.2

## Additional Package
* request  (for **get html**)  
`pip install requests`  
* lxml  (for **parse html**)  
`pip install lxml`  
* httpd-devel  (for **apache server**)  
`yum install httpd-devel`
* mod_wsgi 4.5.14  (for **federate**)  
`wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.14.tar.gz`  
`tar -zxvf 4.5.14.tar.gz`  
`cd mod_wsgi-4.5.14/`  
`./configure --with-python=/usr/bin/.pyenv/versions/3.6.4/bin/python`  
`make`  
**↑error happens!! try to recompile**    
`CONFIGURE_OPTS="--enable-shared" CFLAGS="-fPIC" pyenv install 3.6.4`  
`make clean`  
`./configure CFLAGS=-fPIC --enable-shared`  
`make`  
`sudo make install`  
