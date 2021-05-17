# DependencyInjection Guideline

This is built in Flask server. Three main components are <code>(1) MyService.py</code> <code>(2) MyDatabse.py</code> <code> (3) MyContainer.py</code>. These are together to make a function for specific url such as <code> view.py </code> which returns <code>index.html</code> to the flask server. If you want to add more urls, modify <code> application.py </code> and add it to <code>view.py</code>. You can also make different versions of <code>view.py</code> to expand the system(e.g., add TweetTracker, add FacebookAdsTracker...). Finally, <code> server.py </code> will create an application object to run Flask server.
