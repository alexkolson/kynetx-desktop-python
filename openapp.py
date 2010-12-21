import os
import subprocess 
import kynetx

app = kynetx.kynetx("a369x122")
data = app.raise_event("desktop", "open_app");
action = app.directives[0]['action']
toOpen = app.directives[0]['options']['application']
if action == "open":
    os.chdir('/Applications/'+toOpen+'.app/Contents/MacOS')
    subprocess.call('./'+toOpen)
