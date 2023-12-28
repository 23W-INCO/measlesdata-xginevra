# A visualisation of Measles Data - 
## Population, measles cases, vaccination rates
### in the Federal States of Germany.
find me here https://xginevra.github.io/measlesdata/ <br>
and here http://measlesdata.ecriprojects.de <br>
Also, i am working with FastAPI! <br>
All the necessary files are stored in the /app folder and regularly updated along with the files in the root folder of the repository. 

--work in progress--


### What i achieved so far:

- A web application which provides two "sides" -> right for the map visualization (static!) , left for the clickable bar chart (dynamic!)
- Heatmap of Germany, clickable, information displayed after clicking and in beautiful coloration (layers) 
- Dropdown menue to chose which bar chart you want to see for more "serious" data visualisation -> i found barcharts to be most informative and comparable with each other against other methods
- Description for every Bundesland in the bar chart (still in progress; problems with undefined values)
- the application takes .json files as data

-> i keep this section of the readme updated as further achievements come to my mind <br> <br>

# TODOS:

-> TODO: - SQLite file to replace a database with json file to feed. <br>
-> TODO: - make clicking on the bar chart more informative than it is right now (undefined values)

 
------
- ### Who is your key user group? What are your users trying to achieve/understand/ inquire?
  The target group we want to reach are parents of disabled children who are, among other things, immunocompromised. They should be able to see how many of the children in the selected
  federal state are vaccinated and how many of them have actually been sick from measles. It helps deciding whether families should try vaccinating their child or
  not despite several dangers they are exposed to; also it helps finding a fitting federal state with the so called "herd immunity" - so that the children who cannot be vaccinated
   for reasons, find their safe home.
According to the user group, we want to see where it would be safest to live
  for parents with a disabled/immunocompromised child.

-----
- ### How does the type of visualization chosen help achieve this task effectively and efficiently?
Through visualization on an actual map of germany, every person can directly see
where they must click to see their information of interest. No special reading skills 
are needed to access the map of Germany - assuming they know where they are living. 
As soon as you click on the desired federal state, you'll see the information you want
to see when visiting the website. 

------
- ### How do the other features of your application further help your users achieve this task?
It is visually more appealing to see something you are familiar with (like the map of your country) rather than seeing just 
random diagrams with numbers and names without a picture to them. Clicking on it immediately produces a reaction from the website -
fancy! <br>
So, information is transmitted more easily for any social class.

-------



