#!/usr/bin/env python

from dvl_pub_pkg.msg import Wayfinder_DVL
from rospy import Publisher, Rate, init_node, is_shutdown
from requests import get


class DVLNodePublisher:

    URL_ROUTE = 'http://127.0.0.1:5000/dvl'
    DEFAULT_SLEEP_TIMEOUT = 3

    def __init__(self, topic_to_publish_to, node_base_name, rate=10, default_queue_size=10):
        self.dvl_msg_data = Wayfinder_DVL()        
        self.pub = Publisher(topic_to_publish_to, Wayfinder_DVL, queue_size=default_queue_size)
        init_node(node_base_name, anonymous=True)
        self.rate = Rate(rate)

    def publish_dvl_message(self):
        if self._request_dvl_data():
            self.pub.publish(self.dvl_msg_data)        
        self.rate.sleep()

    def _request_dvl_data(self):
        server_response = get(DVLNodePublisher.URL_ROUTE)
        if server_response.ok:
            self._populate_dvl_msg_data(server_response.json()['DVL_Data'])
            return True
        else:
            print 'Could not retrieve data from DVL server.'
            return False
            
    
    def _populate_dvl_msg_data(self, data_from_request):
        # print data_from_request
        # print self.dvl_msg_data
        for key, val in data_from_request.items(): 
            if key in dir(self.dvl_msg_data):            
                # attr = getattr(self.dvl_msg_data, key)
                if isinstance(val, unicode):
                    msg_attr = getattr(self.dvl_msg_data, key)
                    msg_attr.data = val.encode('utf-8')                        
                else:          
                    setattr(self.dvl_msg_data, key, val)
        
            


if __name__=='__main__':
    dvl_pub = DVLNodePublisher('dvl', 'Wayfinder_DVL_Filter')
    while not is_shutdown():
        dvl_pub.publish_dvl_message()
        



