# coding=utf-8

import sys
import os
import time
import unittest
from ui.view.businessview.web.common.login_business import simple_login
from ui.view.businessview.web.admin.spotlight_videos_business import *
from ui.view.page.web.business.admin.spotlight_videos_page import SpotligtPage
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path


class web_test_spotlight_videos(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        self.data = Yaml(web_config_path).read()
        self.env = self.data['env']
        self.homeUrl = self.data['portal'][self.env].rstrip("/")
        

    def test_admin_page(self):
        self.driver = simple_login()
        spotlight_videos = SpotlightBusiness(self.driver)

        spotlight_videos.click_admin_link()
        spotlight_videos.admin_settings_page()
        spotlight_videos.click_add_video()
        
        for c in range(0,2):
            
            #spotlight_videos.search('https://web-srol-1.stream.azure-test.net/video/5fe8fb5d-1500-a605-87d8-f1eb4a48bc59')
            #spotlight_videos.video()
            #spotlight_videos.click_Remove_button()
            spotlight_videos.search('https://web-srol-1.stream.azure-test.net/video/5fe8fb5d-1500-a605-87d8-f1eb4a48bc59')
            spotlight_videos.video()
            spotlight_videos.search('https://web-srol-1.stream.azure-test.net/video/06d1fb5d-1500-a60d-6310-f1eb433b05b2')
            spotlight_videos.video()
            spotlight_videos.click_Move_UP_button()
            spotlight_videos.search('https://web-srol-1.stream.azure-test.net/video/06d1fb5d-1500-a60d-0cae-f1eb435845fc')
            spotlight_videos.video()
            spotlight_videos.click_Move_Down_button()
            spotlight_videos.search('https://web-srol-1.stream.azure-test.net/video/10f4fb5d-1500-a936-205a-f1eaa0ff141b')
            spotlight_videos.video()
            
            if (c<1):
                
                spotlight_videos.click_Cancel_button()
        
            else:
                spotlight_videos.click_Save_button()
                
                
                
        spotlight_videos.click_Home_button()
        
        time.sleep(5)  # 停顿五秒
        self.save_img('web_admin_spotlight_videos_1-screenshot1')
        


if __name__ == "_main_":
    unittest.main()
   