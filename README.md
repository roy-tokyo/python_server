# python_server
A simple json and zip file http server code by python


How to use:

【Start server】
#cd <the location of server.py and *.json>
#python server.py

【curl or type in the browser】
http://localhost:8888/test   ←if test.json exist　the content of test.json will response <200 OK>
http://localhost:8888/notest  ←if notest.json not exist　the content of notfound.json will response <404 NotFound>

http://localhost:8888/test.zip ←if test.zip exist　the zip file will download <200 OK>

