Fletcher Project Deliverables

1.	 Audience:
The goal is to provide a sense of what topics congressmen are speaking about (both in actual sessions of congress and through twitter) to a general audience, without specialized political knowledge.
2.  Central question:
Do congressional tweets actually represent the political priorities of its members?
3. Question Breakdown:
o  During any given time-period, what topics are congressmen tweeting about vs. their speeches within congress? Do congressmen misrepresent their priorities through twitter? 
o  Can we group members by the topics they focus on?

4. Data:
o  The last 3000 tweets of each of the (488) member’s of congress on twitter, through the twitter API. This amounts to roughly 100,000 tweets. 
o  Text and speaker details (party, state, name) for each individual speech during sessions of congress since 2011 (roughly ~250,000 documents)
o  Both datasets are stored in collections within a Mongo database.

5. Analysis:

Cluster each of the datasets (tweets and speeches), trying various clustering models, so that we can see how they’re organized by topic. If it’s difficult to discern topics through this method, I will try first combining all of the documents by congressman, and then cluster the members of congress.  
6.	Deliverable:
A d3 visualization, which allows one to compare topics in tweets vs. speeches, both in congress overall and by individual. If viable, the timeframe will be adjustable. 
7.   Challenges:
It’s possible that there is no relation between what congressmen are speaking and tweeting about concurrently, because of how congressional sessions are scheduled. Still, a visualization of topics discussed could provide meaningful insights. 
