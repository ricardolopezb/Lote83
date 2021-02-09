from chatbot import Chatbot
from order_maker import OrderMaker
from window import Window
from window_manager import WindowManager
import threading
import time

bot = Chatbot()
orderMaker = OrderMaker()
window = WindowManager()





window.startWindows()



#threadServer = threading.Thread(target=startServer(), args=())
#threadWindows = threading.Thread(target=window.startWindows(), args=())


#threadWindows.start()
#threadServer.start()


