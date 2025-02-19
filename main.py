import os
from keep_alive import keep_alive

from src.client import client
import src.cmds
import src.fact
import src.hug
import src.image
import src.info
import src.speak
import src.suggest
import src.welcome

from dotenv import load_dotenv

try:
  load_dotenv()
  keep_alive()
  client.run(os.environ['TOKEN'])
except Exception as e:
  os.system('kill 1')
