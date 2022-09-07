# DependencyInjection Guideline

This is built in Flask server. Three main components are <code>(1) services.py</code> <code> (2) containers.py</code>. These two bases are used together to make a function you want to support(e.g., finding data from mongodb, calling API for Facebook Ads).

<code> (3) MyDatabase.py</code> is used to get the connection to pymongo (Make sure that you have installed Pymongo before if you wanna combine it to <code>services.py</code>

make different versions of <code>views.py</code> to expand the system(e.g., add TweetTracker, add FacebookAdsTracker...). 


To run this program for your understanding, just execute the <code>run.sh</code>.
To exit this program for your understanding, just execute the <code>stop.sh</code>.
You can install packages required by <code>pip install -r requirements.txt</code>.
