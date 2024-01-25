A visualisation of measles data - population, measles cases, vaccination rates in the federal states of Germany - and in selected cities.
=

Description
-

<p> Our examination goal in the winter semester 2023/24 is to set up a web application that 
provides a quick and clean insight into a self-selected data set.
This application was developed to show the measles figures for the federal 
  states and selected cities in Germany. 

The project aims to point out the relation between the population and the measles cases in cities, and 
it provides an insight of how many paople are actually vaccinated in each federal state. From this perspective, 
one can actually tell whether a federal state or even a city is secure to live in or not.

However, although measles are a disease for which it is mandatory to report to the government (at least in Germany), 
there are always cases which are not recorded and hence not visualized.
</p>

Features
-

<b> Federal state insights: </b> Explore the 16 federal states and their vaccination rates, as well as their measles cases ordered from lowest to highest. The selected bar is highlighted with a black border, and a tooltip appears near the mouse - containing all the stored information for the selected state. 
<br>
<br>
![Screenshot of the functionality for federal states](/Screenshots/MeaslesCasesFederalState.jpg)
![Screenshot of the functionality for federal states](/Screenshots/VaccRateFederalStates.jpg)
<br>
<br>
<b> Cities insights: </b> This chart is made of bubbles whose size represents the relation between the measles cases and the population of the city. Hovering over one bubble, just like we saw at the federal state functionality, highlights it with a black border and shows a tooltip containing the relevant information of the city.
<br>
<br>
![Screenshot of the functionality for cities](/Screenshots/MeaslesCasesCities.jpg)
<br>
<br>
<b> Drop down selection: </b> The user can choose between the visualisation for the federal states and for the cities; while the cities provide another extra-option. Sorting the cities by a certain population limit makes it easier for the user to reliably find the information they are looking for:
<br>
<br>
![Screenshot of the dropdown](/Screenshots/dropdown.jpg)
<br>
<br>

Key User Groups: Families with children who are not able to get vaccinated against measles. 
-

Objective:
-

Measles is not just a children's disease. It is much more than that. If not properly treated, it leads to death quite often (RKI has more reliable information [here](https://www.rki.de/DE/Content/Infekt/EpidBull/Merkblaetter/Ratgeber_Masern.html)).
<br><br>
A key reason why I chose this topic is that there are children who are disabled/immunocompromised, who can't be vaccinated for those and other medical reasons. Their parents must rely on the so called "herd-immunity" which is not always reliably given, especially in those federal states where it isn't mandatory to be vaccinated before going to school or kindergarten. <br>
These families want to find a save home for their children. The app's main goals are to provide the relevant information easily, with no need for any previous knowledge; and to be used with joy. <br>
The choice of the coloration didn't came for any additional functionality but for the sake of usage with joy. Everything around the medical topic, especially when one has a disabled child, they are happy to see at least some colour variety among all these grey or white hospital walls they probably see quite often.


Functionality:
-

<b> Data overview: </b> Allows users to explore the distribution of vaccination rates across Germany, helping to identify safe regions and those that may require extra caution. Furthermore, it provides comprehensive data on total measles cases, supplemented by a representation of the correlation between measles cases and the population in each area.
<br><br>
<b> Detailed information: </b> Within each federal state-bar, data pertaining to the incidence of measles, vaccination rates, population statistics, and current instances of measles are stored. This comprehensive information is elegantly revealed upon hovering the mouse over the respective bar chart representing the selected federal state.

Real-World Application:
-

<b> Empowering families: </b> In practical terms, families unable to vaccinate their children against measles due to medical reasons can rely on this application, provided that the data is consistently updated and accurately reflects the genuine measles statistics.
<br><br>
<b> Professional guidance: </b> Even healthcare professionals can utilize this application to offer guidance to individuals, spanning across all social classes, who currently lack internet access, ensuring that valuable information is accessible to everyone.
<br>
<br>

User Benefit:
-

<b>Well-considered decisions:</b> The app provides an easy way to explore and understand complex data, empowering the user to make informed decisions.
<br><br>
<b> Moving perspectives: </b> Families can carefully consider their new living location by relying on the reliable information provided by the application, ensuring a well-thought-out and health-conscious relocation. 
<br><br>

Installation and Setup Instructions
- 

### Running the application in a devcontainer via GitHub Codespaces.
-----

1. <b> Open in GitHub Codespaces </b>
- Go to the GitHub repository: [https://github.com/xginevra/measlesdata](https://github.com/xginevra/measlesdata).
-  Click on 'Code', then select 'Open with Codespaces'.
- Choose 'New codespace' to create a new development environment.
<br>
2. <b> Automatic setup </b>

- The devcontainer which is included in this repository, will automatically set up the needed codespaces environment.
<br>
3. <b> Accessing the application </b>

- When the codespaces environment is done with building and starting, go to <code>Ports</code>.
- The port 8000 is the one you want to start.
- Click on <code>open in browser</code> - it is a small globe symbol. A new tab running the application will appear.
<br>
4. <b> Upload new data </b>

- Either click on the link in the application where it says "feel free to update your own data here" or visit the route <code> /docs </code>.
- After being redirected, click on the green "POST" link to show the route <code> /uploadjsondata </code>.
- click on <code> try it out </code> and choose your file which must be based on the sample json data provided either in the repository or at the upload location of the examination.
- click on execute and see if the upload worked (status 200) or if it was rejected because of format or wrong file type (status 500)
- delete the /docs (and what follows) so that you only have the "normal" address of your codespace port
- see the uploaded data along with my original files in the visualisation.
<br>
5. <b> Getting back to my "original" data </b>

- get back to the actual codespace, close the tab with the application
- close (<code>CTRL+C</code>) and re-open the uvicorn with the command <code> python3 -m uvicorn main:app --reload </code>.
- open the port again in browser
- see that your inserted data disappeared :)
<br>

### Local Setup

1. <b>Clone the Repository:</b>
   - Run `git clone https://github.com/ali-b7/Covid-Analysis-in-Germany.git` in the terminal.
   - Navigate to the cloned directory.

2. <b>Install Dependencies:</b>
   - In the terminal, run <code>pip install -r requirements.txt</code>.

3. <b>Starting the Application:</b>
   - Run <code>uvicorn main:app --reload</code> in the terminal. -> maybe you must specify a port using the addition <code> --port 8000 </code> before <code>--reload</code>
   - The application will be available on <code>http://localhost:8000</code> or the specified port.
   - Uploading data works the same way as in running the applicaiton in a codespaces.
