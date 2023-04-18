# COMP3331_9331_23T1_Labs
For M14A students

## Useful links:
 - [Course home page](https://webcms3.cse.unsw.edu.au/COMP3331/23T1/)
 - [Lab timetable and recordings](https://webcms3.cse.unsw.edu.au/COMP3331/22T3/resources/80663)
 - Forumn: https://edstem.org/au/courses/10008/
 - Monday 14:00 (M14A) lab link:  https://unsw.zoom.us/my/ruitut   
 - [MyRecordings](https://www.youtube.com/playlist?list=PL62Uy8LvT4Famj6_UVCQHf8aajP0ySZkL)  
 
 
 
## Testcase for assignment:
 ### prep:
  1. move your code to VLab Env (**very important**)
  1. use this .txt file to do the test: https://github.com/lrlrlrlr/COMP3331_9331_23T1_Labs/blob/main/ruitest.txt 
  1. put your sender and receiver in different folder (they should be able to run stand alone)
 ### section 1:  Stop and Wait
  steps:  
  1. run your program with:
  `python3 receiver.py 56007 59606 FileToReceive.txt 0 0`  
  `python3 sender.py 59606 56007 test1.txt 1000 500`  
  
  2. check:
   - log file should be able to generated in both side (sender log and receiver log)
     - check the sender log file:
       - if the format is correct 
       - if the timer is making sense
       - check if there is any SYN/SYNACK packet at the beggining
       - if the sequence number is random number? 
       - if the seq_no calculation correct? (for syn and fin)
       - if any packet loss in the log(should not have any loss)
       - if there is FIN/FINACK at the end of the log

     - check the receiver log:
       - if the format is correct
       - if the timer is correct (not sync with the sender)
       - if SYN/FIN packets received
     - check the receiver side txt file
       - if the filesize the same?
       - if the file content the same? (make sure have correct order, you can use `diff` command to do the cmp in linux)

  3. repeat the test with different param:  
       - try different rto value for the sender.py
        - `python3 sender.py 59606 56007 test1.txt 1000 100`   
        - `python3 sender.py 59606 56007 test1.txt 1000 500`  
        - `python3 sender.py 59606 56007 test1.txt 1000 2500`  

 ### section 2: pipelining (sliding window)
   steps:  
  1. run your program with:
  `python3 receiver.py 56007 59606 FileToReceive.txt 0 0`  
  `python3 sender.py 59606 56007 test1.txt 5000 500`  
  
  2. check:
   - log file should be able to generated in both side (sender log and receiver log)
     - check the sender log file:
       - if the format is correct 
       - if the timer is making sense
       - if the sender is able to send 5 packets in a row?
     - check the receiver log:
       - if the format is correct
     - check the receiver side txt file
       - if the file content the same? (make sure have correct order, you can use `diff` command to do the cmp in linux)

  3. repeat the test with different param:  
       - try different max_win value for the sender.py
        - `python3 sender.py 59606 56007 test1.txt 5000 500`  
        - `python3 sender.py 59606 56007 test1.txt 10000 500`  


 ### section 3: unreliable transmission (sliding window)
   steps:  
  1. run your program with:  
  `python3 receiver.py 56007 59606 FileToReceive.txt 0.5 0.5`  
  `python3 sender.py 59606 56007 test1.txt 4000 500`  
  
  2. check:
   - log file should be able to generated in both side (sender log and receiver log)
     - check the sender log file:
       - if around hale of the packets lost (should have packet lose as we have 50% of chance to lose all types of packet)
       - if any timeout triggered (could be), if so, will the oldest packet be retranmitted? (make sure only the oldest one)
       - if the sequence number is calculated correctly

     - check the receiver side txt file
       - if the file content the same? (make sure have correct order, you can use `diff` command to do the cmp in linux)

  3. repeat the test with different param:  
       - try different flp/rlp value for the sender.py
        - `python3 receiver.py 56007 59606 FileToReceive.txt 0.1 0.1`    
        - `python3 receiver.py 56007 59606 FileToReceive.txt 0.9 0.9`    

 

## Assignment demo 
  I will have assignment demo session for python.  
  - Schedule:  https://webcms3.cse.unsw.edu.au/COMP3331/23T1/resources/85995  
  - Link: https://unsw.zoom.us/my/ruitut   
  - Schedule:
    - W5: week assignment overview: How to start from 0. basic code demo.
      - What is the task?
      - play around with the demo code


    - W7: Assignment 101, how to get started with the template code (multi-threading)
      - app design / protocol design
      - data structure
      - basic python operations
        - how to create/delete/modify txt file
        - how to send/receive json object between server/clients
        - Recording link: to be uploaded  
        - Demo code used in the tutorial: https://github.com/lrlrlrlr/COMP3331_9331_23T1_Labs/tree/main/demo%20w7 
        
    - W8: Application protocol design and data structure
        - Demo code used in the tutorial: https://github.com/lrlrlrlr/COMP3331_9331_23T1_Labs/tree/main/demo%20w8 

    - W9: Testing, code style, submission Q&A
        - TODO: I will upload some testcase here, feel free to try it with your program. But it is not offcial testcase and it will not represent how will the tutors test your program!  
        - report content
        	- 1. how to run the script
        	- 2. what is your application protocol and data structre?
        	- 3. any bug or trade-off you made for your program? (for example, you have significant delay on UDP file transmission to make sure the reliable file transfer)
        	- ps: 1~2 pages is enough, make it simple and clear.
        - new text file
        - submission checklist


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




  
## Tut01:
 - recording: https://youtu.be/meJ3keKIEZ4 
 - useful materials:  https://github.com/lrlrlrlr/COMP3331_9331_21T3/tree/main/9331review 
 
 
## Lab4:
 - Exercise 1: Understanding TCP using Wireshark
   - Q1 & Q2:
    ![image](https://user-images.githubusercontent.com/27357380/227826086-1d46a547-b599-4336-8852-aa2f0a42d124.png)  
   - Q3 - Q4
   
     EstimatedRTT = 0.875 * EstimatedRTT + 0.125 * Sample RTT.   
     | segment | length | seq. number | sent time | received time | SampleRTT | EstimatedRTT |  
     |-|-|-|-|-|-|-|
     | 1 | 232129013 | 565 |0.026477 |0.053937 |	0.02746 |  0.02746 |  
     | 2 | .. | .. |.. |.. |.. | ..|
     | 3 | .. | .. |.. |.. |.. |  ..|
     
   - Q5:  
     - check the SYN/ACK packet, there is a "window" header in the TCP section.
   - Q6:  
     - Generate a Sequence Numbers(Stevens) Graph
   - Q7:
     - Please observe the packet #53~#62, why we have only 4 ACK for 6 packets?
   - Q8:
     - throughput = (#202_seq - #4_seq - 1) / (#202_ack_time - #4_seq_time)
     
