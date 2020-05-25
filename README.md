# Contents
* [Introduction](#Introduction)
* [The Brief](#The-Brief)
    * [Scope](#Scope)
* [Technologies Used](#Technology-Used)
* [Project Tracking/Planning](#Project-Tracking)
    * [Initial Tracking Board](#Initial-Trello-board)
    * [Final Tracking Board](#Final-Trello-board)
    * [Initial ERDiagram]( Entitiy-Relationship-Diagram)
    * [Final ERDiagram](Final-Entitiy-Relationship-Diagram)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Improvements for the future](#Improvements)

# Introduction
A solo project building a CRUD application using tools and methodologies used during QA Academy training, due to present at the beginning of week 6. 

For my project, I decided to build an application designed to use different types of instrumental music to aid studying depending on users' personalities. 

# The Brief
A wide range of material was covered in training to help build the application which includes:
1. DevOps as a culture
2. Cloud fundamentals
3. Version Control
4. Databases
5. Python, testing with Python and web development
6. CI server
7. Basic Linux

  
## Scope
A list of requirements to meet the MVP were given for the project. 
1. A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced creating your project.

2. A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.

3. Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.

4. A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on your Kanban Board

5. Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach.

6. A functioning front-end website and integrated API's, using Flask.

7. Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.



# Technology Used
A list of technologies was also given:
1. __Kanban Board-__ Trello board
2. __Database-__ GCP SQL Server
3. __Programming Language-__ Python
4. __Unit Testing with Python-__ Pytest
5. Integration Testing with Python (selenium)
6. __Front-end -__ Flask (HTML, some CSS and Jinja2)
7. __Version Control -__ Git
8. __CI Server -__ Jenkins
9. __Cloud server -__ GCP

# Project Tracking
A trello board was used for project management and tracking. Having already used trello for practise exercises during training, it was easy to use and simple to follow.
The user stories were planned out first implementing the MoSCoW principle to keep the focus on the essential areas. Scrum framework was used with the sprint backlog, this was then explored further by adding specific tasks and sprints relating to the backlog. 
## Initial Trello board 
![](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/Initial%20trello%20board.png)

## Final Trello board
![](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/Final%20trello.png)
Once the documentations had been completed, the timescale to create and build the application was a week
 
## Initial Entitiy Relationship Diagram
At least 2 tables sharing a relationship were required to meet the MVP requirement.
ERDiagrams were used to help organise the database.

Below is the initial ERDiagram making use of the MoSCoW principle, ensuring to focus on areas that should be in the application with the help of the user stories. 

![image](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/ERDiagram%20(2).jpg)

## Final Entitiy Relationship Diagram

![image](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/Final%20ERD.jpg)

Initially I wanted to include the playlist table so that songs could be saved into a playlist for ease of use. However, due to time constraints, I decided to only use 2 tables linked with a one to many relationship. 

I had also wanted the Songs table to be pre defined with songs related to both personality types. However, when starting the application I was unsure how that could be added, so a form was used for the user to add their own songs.

# Risk Assessment
![](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/Risk%20Assessment%20key.jpg)

![](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/Risk%20Assessment.png)
(Please click on above image for better view)


# Testing

# Deployment

![](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/CI%20Pipeline.jpg)

### Version Control System
I used three branches on the Version Control System  using the feature branch model. At the beginning, I used the development branch and merged with master once I had working code after completing individual task/sprint sections in the trello board. Later all my work was completed on the development branch. When updating the READme file, which required a lot of images, I created another branch 'images' to store all the diagrams and merge with master when READme was completed.

### CI Server
A lot of issues occurred when deploying with Jenkins due to bugged installations requiring reinstallation and recreating the project on Jenkins. On reinstallation, Jenkins was running the application but builds were not reaching the successful stage.

Having used systemd service to deploy the application in the background, there were multiple occurences of errors which did not allow me access to the application. After many failed attempts to debug the errors, I decided to not use systemd services in order to have a MVP. 

# Improvements
* __Website experience/create functionality-__ With gaining more experience with Python, I later understood how to add a pre defined Songs selection. This would give the user a better experience as it would include the songs tailored to their personalities without having to manually add songs themselves. 

* __Testing__- Increase testing coverage.
* __Improve front end design__- To meet the MVP requirements, there was a priortisation in working software over making the application look good so I had not focused too much on front end design.
* __Feature branch model__ - use feature branch model more effectively. In future I would merge changes onto the master branch after each task on trello board is completed to track changes better.

