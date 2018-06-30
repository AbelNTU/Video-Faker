import importlib.util
from socket import *
import sys
# If covered file not exist , then run the following to create mp4

spec = importlib.util.spec_from_file_location("server_process", "/Users/joe/Desktop/Video-Faker/video-processing/server_process.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


foo.encry("../network/5.mp4","../network/cover.mp4",11,0)
