#!/usr/bin/env python
import time
from time import gmtime, strftime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
        def on_created(self, event):
                print strftime("%Y-%m-%d %H:%M:%S", gmtime()), event

        def on_deleted(self, event):
                print strftime("%Y-%m-%d %H:%M:%S", gmtime()), event

        def on_moved(self, event):
                print strftime("%Y-%m-%d %H:%M:%S", gmtime()), event



observer = Observer()
observer.schedule(Handler(), path='/var', recursive=True)
observer.start()



try:
        while True:
                time.sleep(0.1)


except KeyboardInterrupt:
        observer.stop()

observer.join()
