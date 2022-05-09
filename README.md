# Machine Learning Engineer Assesment

Every month, there are thousands of events active on TicketSwap websites. These events range from music festivals to concerts to sporting events, stand up comedy shows and more. To help our users find the events they would like to attend, we try to extract the event lineup, as well as any additional information, from the event titles. 

## Part 1

Inside the data directory there are two files:
* A file containing a list of event titles, event_titles.txt
* A list of artists from our database, artists.txt. For the sake of this assignment, we do not differentiate between artists, stand up comedians, football clubs, or festival names. They all are listed together in the same artists.txt file.

We would like you to build a solution, given an event title, it would return the potential lineup (artist names) or equivalent (football teams, festival names, etc). 

Your solution should consider the following:

* Not all artists are listed in our database. Think of ways to extract ones not in our database yet. 
* The same artists can have different spellings, think Pink vs P!NK. 
* The same name can refer to multiple things, think Arsenal (football club) vs Arsenal (band)

#### Bonus questions

* What additional information can you extract from the event titles? What additional business value do you think this information can provide? 
* Can you differentiate between your confidence levels for when different artists are extracted?

## Part 2

Once your solution is ready, other parts of our product will need to communicate with it. What is the best way to make your predictions available for the rest of the product to consume? Will your solution differ in case the predictions are needed in real-time vs offline batch jobs? What are the different deployment options you can think of?  

Please build a very simple prototype for making your predictions available on demand to our different microservices?

## Part 3

Your prototype proved to be successful and you want to push it forward. How would you communicate with the following teams and what evidences will you try to provide to convince them about your solution:

* Content team. This is the team that currently adds line-up to events manually, and this project will help them automate this part of their job
* Marketing team. This is the team that needs to have line-ups for events to be able to promote the events with popular artists.

How would you approach other teams to put your solution in production, and make sure they can consume your predictions successfully? For example, the front-end and back-end team who will need to integrate with your solution? Can you think of other technical teams that you will need to align with?

Finally, will you need to collect additional data for your future iterations on your solution?   



Best of luck to you
