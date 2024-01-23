# A visualisation of Measles Data - 
## Population, measles cases, vaccination rates
### in the Federal States of Germany - and in selected bigger cities.

---------------------

# important: - To update the application and upload a new file to the application, please see the route <code> /docs </code> - linked in the application itself, click on "try it out" and upload the desired file. reload to the standard route <code> "/" </code> and see how your new file is being embedded in the visualisation.

Only stopping uvicorn by clicking ctrl+c and restarting it resets the data to the "standard" data. 


- ### What i achieved so far:

- A web application which provides two "sides" -> right for the map visualization (static!) , left for the clickable bar chart (dynamic!) <br>
but i needed to leave the map out, so it is just a chart visualisation (it was really beautiful, though)

- Heatmap of Germany, clickable, information displayed after clicking and in beautiful coloration (layers) <br>
  but i needed to leave it out because it would do more harm then benefit 
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
- i managed to automate the feeding of the .json file into the visualisation - an exchange is easily possible by replacing the .json file
- either replacing the .json file (this would be a final decision, also you loose "my" data) or uploading on the /docs route (this is temporary, you just add your data to mine) makes it possible to change data. 

-> read further to see the latest changes and achievements.

------
- ### Who is your key user group? What are your users trying to achieve/understand/ inquire?
  The target group we want to reach are parents of disabled children who are, among other things, immunocompromised. They should be able to see how many of the children in the selected federal state are vaccinated and how many of them have actually been sick from measles - also in selected cities. It helps deciding whether families should try vaccinating their child or not despite several dangers they are exposed to; also it helps finding a fitting federal state with the so called "herd immunity" - so that the children who cannot be vaccinated for several medical reasons, find their safe home.
According to the user group, we want to see where it would be safest to live
  for parents with a disabled/immunocompromised child.

-----

- ### How does the type of visualization chosen help achieve this task effectively and efficiently?
The selected bar charts make it possible to directly compare every single federal state with<br>
the other in terms of vaccination rates and measles cases.<br>
The city data visualisation bubbles give information about every selected city, ordered by <br>
population (x-axis) and measles cases (y-axis). The size of the bubbles <br>
 represents the relation between measles cases and population.
This is a really convenient way of looking at data and understanding what they want to tell you. <br>
Though, i came across the fact that there are more likely the most measles cases in cities with the most inhabitants. <br>
This is being "proved" in the visualisation, and though it is a pleasure to look at it <br>
and to compare the cities with each other.


------

- ### How do the other features of your application further help your users achieve this task?
It is easy to get to see the desired information by simply clicking on the drop-down menue and does not need any further explanation.
<br> even writing skills aren't required. <br>
So, information is transmitted more easily for any social class. <br>
The joyful coloration of the bars and the bubbles don't give that sterile feeling one gets when <br>
using an app in a medical context. We don't want the parents of the disabled children <br>
to feel even more bad having to look at those diagrams to see where they can even live nowadays.<br>
At least, they should see some colour in their lives - even if it is just a rainbow colored <br>
visualisation. <br>
The reqirement said, we should make it a joy using the app - and i frankly think that <br>
colours make everything better. All of the "serious-themed" applications should appear <br>
much friendlier as they actually do now. 

---------

- ### Achievements during the project time and a brief description for evaluation

- First, i wanted to make a map with Folium where you can click on the desired federal state for an overview and to get familiar with the application, before the user would change to the other visualisations. But the map wasn't made with d3.js, so i had to drop this idea. Furthermore, the bar charts are giving the same information but built with d3 and this is what the requirement says.
- I decided on bar charts to visualize the relations of the measles cases with the population - i've had the idea from the beginning. Later, i added the "per 100.000" value which represents the incidence of the federal state. I used a dropdown menue for the user to choose what they want to see - measles cases per Bundesland or the vaccination rate of each.
- I tried to dockerize the repo and its files to make it compatible to run automatically in codespaces - docker alone didn't work, so i added a .devcontainer folder containing such a file to make it automatically start; you just need to click the "open in browser" at the port after starting the codespace. The starting command <code> cd app && python3 -m uvicorn --reload </code> makes the output of the uvicorn disappear/not even show up, but it should run anyway.
- Later, the idea of adding cities came across my way to expand the amount of data we're handling and to make it even more tangible. I added chosen cities and added 4 more options for cities with chosen amounts of population: up to 200,000; more than 200,000; more than 500,000; and more than 1,000,000. It should make it easier for families to decide which city fits their needs most - where are the least measles cases (the relation between the population and the cases is represented by the size of the bubbles; though logically, the smallest cities in a selection usually have the least amount of measles cases.
- After successfully implementing a .db file for the backend, I managed to automate the process of putting the fhir-compliant .json file into the .db file which feeds the visualisation. After freshly starting the application, it automatically re-fills the database with the original file i provide with the application.
- To update the application and upload a new file additionally, please see the route <code> /docs </code>, click on "try it out" and upload the desired file. go back to the standard route <code> "/" </code> and see how your new file is being embedded in the visualisation.
- I added tooltips via the .on(mouseover) funtion; they show the underlying data for each city and bundesland and highlight the selected section of the visualisation, to make it more tangible (we want to make it easy to use for everyone)
- The upload functionality accepts only an appropriate .json file, as provided as sample.
- 
