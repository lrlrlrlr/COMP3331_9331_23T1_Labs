# COMP3331_9331_23T1_Labs
For M14A students

## Useful links:
 - [Course home page](https://webcms3.cse.unsw.edu.au/COMP3331/23T1/)
 - [Lab timetable and recordings](https://webcms3.cse.unsw.edu.au/COMP3331/22T3/resources/80663)
 - Forumn: https://edstem.org/au/courses/10008/
 - Monday 14:00 (M14A) lab link:  https://unsw.zoom.us/my/ruitut   
 - [MyRecordings](https://www.youtube.com/playlist?list=PL62Uy8LvT4Famj6_UVCQHf8aajP0ySZkL)  
 
## Lab1：  
 - quick notes
   - Please use **[VLAB](https://taggi.cse.unsw.edu.au/FAQ/Really_quick_guide_to_VLAB/)** to run all the commands!
   - Exercise 2: visit the url with the browser and ping command (e.g. ping www.unsw.edu.au), explain if they can not be reached.
   - Exercise 3: 
     - 3.1 run command `traceroute www.columbia.edu`, routers_count = output_lines - 1 (the last one is our destination)
     - 3.2 run traceroute for 3 websites, then draw the diagram for the diverge 
     - 3.3 Steps:
       - 1. visit these two websites
       - 2. Traceroute from the website to our own ip address;
       - 3. Traceroute from our machine to these websites, Compare the outputs;
       - 4. Explain why. 
    - Exercise 4:
      - follow the steps to run the command for `runping.sh` and `plot.sh` for 3 different websites(will take around 7 mins each)
      - calculate
      ![image](https://user-images.githubusercontent.com/27357380/220208534-318783c0-d0ea-496d-beda-a4af81aa0860.png)

 - [recording](https://unsw.zoom.us/rec/share/bog4Y1CNXu86qUZLxQy2CioKgVD6u5zByi4y2eQrKnehPs6FDwxbM0hWqLugG0n9.OwngSptc1JGPwdTG?startTime=1676861413000)
Passcode: Re3!&8C+


## Lab2:
 - quick notes
   - Exercise 3:
  ![image](https://user-images.githubusercontent.com/27357380/221456972-412c8647-79bc-4311-b01d-6ab92058c93f.png)

   - Exercise 4:
   ![image](https://user-images.githubusercontent.com/27357380/221456458-220a643a-6a30-479a-994e-bd77681cf853.png)
     - Etag vs Last-Modified
      ```
      If-Modified-Since is compared to the Last-Modified whereas If-None-Match is compared to ETag. 
      Both Modified-Since and ETag can be used to identify a specific variant of a resource.

      But the comparison of If-Modified-Since to Last-Modified gives you the information whether the cached variant is older or newer whereas the comparison of If-None-Match to ETag just gives you the information whether both are identical or not. 
      Furthermore do most of the ETag generators include the information of the system specific inode so moving a file to a different drive may change the ETag as well.
      ```

    - Exercise 5: Please refer to this 5min video: https://www.youtube.com/watch?v=9ARKigLwJfM&ab_channel=RUILI
  - Recording:  https://youtu.be/tC9fIMj4wCQ 
  
  
## Lab3:
 - quick notes
   - Exercise 3:
     - Q1: To get the IP address of www.eecs.berkeley.edu, we can use the A (Address) DNS record type. We can use the following command to query the default nameserver: `dig www.eecs.berkeley.edu A`
     - Q2: use the following command: `dig www.eecs.berkeley.edu CNAME`
     - Q3: The Authority section of the DNS response contains information about the _____________. The Additional section contains ______________. (google it)
     - Q4: try command `dig .`
     - Q5: try command `dig eecs.berkeley.edu NS`
     - Q6: try command `dig -x 111.68.101.54 PTR`
     - Q7: try command `dig @129.94.242.33 yahoo.com MX`
     - Q8: try command `dig @ns1.eecs.berkeley.edu yahoo.com MX`
     - Q9: To obtain the authoritative answer for the mail servers for Yahoo! Mail, we can use the following command: `dig +trace yahoo.com MX`
     - Q10: To find the IP address of lyre00.cse.unsw.edu.au, we need to follow the iterative DNS query process by querying the authoritative nameservers for each level of the domain hierarchy. Here are the commands:
       - `dig NS .`
       - `dig NS au. @ip_address` (Note: replace the ip_address with the ip address you got from last cmd)
       - `dig NS edu.au. @ip_address` 
       - `dig NS unsw.edu.au. @ip_address`
       - `dig NS cse.unsw.edu.au. @ip_address`
       - `dig A lyre00.cse.unsw.edu.au. @ip_address` -> got the answer, notice the flags should contain "aa"
       - Please watch the recording for better understanding. 
     
     
     - Q11: Yes, but why? (Search)

    - Exercise 4: Here are some general steps you can follow to write this web server:  

      1.  Parse the command line arguments to get the port number to listen on.
      1. Create a socket using the appropriate socket library for your programming language (e.g., socket library in Python).
      1. Bind the socket to the specified port number using the bind method.
      1. Listen for incoming connections using the listen method.
      1. In a loop, accept incoming connections using the accept method. This will return a new socket object that you can use to communicate with the client.
      1. Read the HTTP request from the client using the recv method of the new socket object.
      1. Parse the HTTP request to determine the requested file.
      1. Open the requested file and read its contents.
      1. Construct an HTTP response message that includes the file contents along with appropriate header lines.
      1. Send the response over the TCP connection to the requesting browser using the send method of the new socket object.
      1. Close the new socket object.
      1. You can use the split method of the str class to parse the HTTP request, and the os library to check if a file exists.

            Make sure to handle errors appropriately, and test your web server by accessing it using a web browser on the same machine.
    
  - Recording (including exercise 4 demo code): https://unsw.zoom.us/rec/share/1bL2YzgronP3bHKmlZtPw5SkS1OYNzusYbGs81TaLRO4YaUXiotncx0YY5RGJd63.Ma4mSkpcrJyrnbGA 
Passcode: L30rh^^j


     
