# watchdog_runner.py
import os
import sys
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)

    def restart(self):
        print("Detected changes, restarting server...")
        self.process.terminate()
        self.process = subprocess.Popen(self.command, shell=True)

    def on_any_event(self, event):
        self.restart()


if __name__ == "__main__":
    path = "."
    command = "python main.py"
    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Watching for file changes in directory:", os.path.abspath(path))
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        event_handler.process.terminate()
    observer.join()
