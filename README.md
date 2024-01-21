# A visualisation of Measles Data - 
## Population, measles cases, vaccination rates
### in the Federal States of Germany.

I am working with FastAPI! <br>
All the necessary files are stored in the /app folder which is the working directory.

---------------------

### What i achieved so far:

- A web application which provides two "sides" -> right for the map visualization (static!) , left for the clickable bar chart (dynamic!)
- Heatmap of Germany, clickable, information displayed after clicking and in beautiful coloration (layers) 
- Dropdown menue to chose which bar chart you want to see for more "serious" data visualisation -> i found barcharts to be most informative and comparable with each other against other methods
- tooltip: Description for every Bundesland in the bar chart
- but also the same for the cities section and the circles - i found them very appealing and nice 
- created a docker file and tried it out in codespaces (forgot to stop the codespace, now I can't access it anymore due to limitations of github)
- added cities and their measles cases (look for cities with a limit of inhabitants) 
- It works with an sqlite file, is being fed from a fhir-compliant json file (which i added to the repo lately!).
- the circles visualisation is now animated :)
- got rid of the empty space in the x-axis
- updated the text of the application to introduce the cities option
- i added the .json file which i fed into the database for a sample (for the sake of compability!)
- i validated the .json file to be FHIR-compliant with [Simplifier.net](https://simplifier.net/validate)
- i managed to automate the feeding of the .json file into the visualisation (left side, right side remains static because it is beautiful and informative as it is!) - an exchange is easily possible by replacing the .json file 

-> i keep this section of the readme updated as further achievements come to my mind <br> <br>


------
- ### Who is your key user group? What are your users trying to achieve/understand/ inquire?
  The target group we want to reach are parents of disabled children who are, among other things, immunocompromised. They should be able to see how many of the children in the selected
  federal state are vaccinated and how many of them have actually been sick from measles - also in selected cities. It helps deciding whether families should try vaccinating their child or
  not despite several dangers they are exposed to; also it helps finding a fitting federal state with the so called "herd immunity" - so that the children who cannot be vaccinated
   for reasons, find their safe home.
According to the user group, we want to see where it would be safest to live
  for parents with a disabled/immunocompromised child. 

-----

- ### How does the type of visualization chosen help achieve this task effectively and efficiently?
Through visualization on an actual map of germany for an overview, every person can directly see
where they must click to see their information of interest. No special reading skills 
are needed to access the map of Germany - assuming they know where they are living. 
As soon as you click on the desired federal state, you'll see the information you want
to see when visiting the website. <br><br>
The selected bar charts make it possible to directly compare every single federal state with<br>
the other in terms of vaccination rates and measles cases.<br>
The city data visualisation gives information about every selected city, ordered by <br>
population (x-axis) and measles cases (y-axis)<br>
This is a really convenient way of looking at data and understanding what they want to tell you.


------

- ### How do the other features of your application further help your users achieve this task?
It is visually more appealing to see something you are familiar with (like the map of your country) rather than seeing just 
random diagrams with numbers and names without a picture to them. Clicking on it immediately produces a reaction from the website -
fancy! <br>
it is easy to get to see the desired information by simply clicking on the drop-down menue and does not need any further explanation.
<br> even writing skills aren't required
So, information is transmitted more easily for any social class.

-------



