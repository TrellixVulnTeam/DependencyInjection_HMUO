# DependencyInjection Guideline

This is built in Flask server. Three main components are <code>(1) MyService.py</code> <code>(2) MyDatabse.py</code> <code> (3) MyContainer.py</code>. These three bases are used together to make a function you want to support(e.g., finding data from mongodb, calling API for Facebook Ads).\\

If you want to add more urls, modify <code> application.py </code>. You can also make different versions of <code>view.py</code> to expand the system(e.g., add TweetTracker, add FacebookAdsTracker...). Finally, <code> server.py </code> will create an application object to run Flask server.

To run this program for your understanding, just execute the <code>server.py</code>.
