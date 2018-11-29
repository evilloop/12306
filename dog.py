import importlib
from watchdog.observers import Observer
from watchdog.events import *
import time

class ScriptEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    # 文件移动
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    # 文件新建
    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            # self.reload_module(event.src_path)
            print("file created:{0}".format(event.src_path))

    # 文件删除
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    # 文件修改
    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
            # self.reload_module(event.src_path)

    # # 重载模块
    # def reload_module(self, module_name: str):
    #     module_name = module_name.replace('/', '.')
    #     module_name = module_name.replace('.py', '')
    #     instance = importlib.import_module(module_name)
    #     if instance:
    #         importlib.reload(instance)


observer = Observer()
event_handler = ScriptEventHandler()
# ./test为需要监控的目录
observer.schedule(event_handler, '.', True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
