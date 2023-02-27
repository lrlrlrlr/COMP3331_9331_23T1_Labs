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

 - [recording](https://unsw.zoom.us/rec/share/bog4Y1CNXu86qUZLxQy2CioKgVD6u5zByi4y2eQrKnehPs6FDwxbM0hWqLugG0n9.OwngSptc1JGPwdTG?startTime=1676861413000
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


 
