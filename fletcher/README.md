#Fletcher Project Deliverables

## Audience:
The goal is to provide a sense of what topics congressmen are speaking about (both in actual sessions of congress and through twitter) to a general audience, without specialized political knowledge.

## Central question:
Do congressional tweets actually represent the political priorities of its members?

## Question Breakdown:
* During any given time-period, what topics are congressmen tweeting about vs. their speeches within congress? Do congressmen misrepresent their priorities through twitter? 
* Can we group members by the topics they focus on?

## Data:
* The last 3000 tweets of each of the (488) member’s of congress on twitter, through the twitter API. This amounts to roughly 100,000 tweets. 
* Text and speaker details (party, state, name) for each individual speech during sessions of congress since 2011 (roughly ~250,000 documents)
* Both datasets are stored in collections within a Mongo database.

## Analysis:

Cluster each of the datasets (tweets and speeches), trying various clustering models, so that we can see how they’re organized by topic. If it’s difficult to discern topics through this method, I will try first combining all of the documents by congressman, and then cluster the members of congress.
  
## Deliverable:
A d3 visualization, which allows one to compare topics in tweets vs. speeches, both in congress overall and by individual. If viable, the timeframe will be adjustable. 

## Challenges:
It’s possible that there is no relation between what congressmen are speaking and tweeting about concurrently, because of how congressional sessions are scheduled. Still, a visualization of topics discussed could provide meaningful insights. 
