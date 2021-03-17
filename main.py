import threading
import requests


def download():
  def get_requests():
    global num_downloads
    global num_money
    
    _r = requests.get('https://mdundo.com/dl/1306447')
    num_downloads += 1
    num_money += 0.2
    
  
  
  while True:
    t = threading.Thread(target=get_requests)
    t.start()
    
    
if __name__ == '__main__':
  for _i in range(10):
      t = threading.Thread(target=download)
