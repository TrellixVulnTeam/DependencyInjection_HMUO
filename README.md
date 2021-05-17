# DependencyInjection Guideline

This is built in Flask server. Three main components are <code>(1) MyService.py</code> <code>(2) MyDatabse.py</code> <code> (3) MyContainer.py</code>. These are interconnected and finally called in <code> view.py </code>. If you want to add more urls, modify <code> application.py </code> and it will create an app object which is used in the top level python file <code> server.py </code>
