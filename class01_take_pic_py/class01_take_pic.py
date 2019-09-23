import tellopy
from time import sleep

# save Image Handle
def handleFileReceived(event, sender, data):
    pic_name = 'tello.jpg'
    with open(pic_name , 'wb') as fd:
        fd.write(data)
        fd.close
# new Tello
drone = tellopy.Tello()
drone.connect()
drone.wait_for_connection(10) # wait 10 `s for connection
drone.subscribe(drone.EVENT_FILE_RECEIVED,handleFileReceived) # subscribe handleFileReceived()
drone.takeoff() # take off the drone
sleep(3)
drone.take_picture() # take pic
drone.land() # land
drone.quit() # end