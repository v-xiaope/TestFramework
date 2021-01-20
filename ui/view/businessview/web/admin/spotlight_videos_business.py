# coding=utf-8
# @Time    :
# @Author  :
# @File    : spotlight_videos_business.py

from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.businessview.web.common.login_business import LoginBusiness
from ui.view.page.web.business.admin.spotlight_videos_page import SpotligtPage as page
from ui.lib.browser_engine import Logger



class SpotlightBusiness(BusinessWebPage):
    def __init__(self,driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = page()

    # 获取元素点击按钮
    def settings_element(self, sname):
        if self.is_element_clickable(sname):
            self.click(sname)
        else:
            element = self.find_element(*sname)
            self.perform_javascript_click(element)
            

    # 点击admin_settings按钮
    def click_admin_link(self):
        self.settings_element(self._page.settings_button)
        self.settings_element(self._page.Admin_settings_button)

    # 进入Spotlight_videos页面
    def admin_settings_page(self):
        self.settings_element(self._page.Spotlight_videos_button)
        
    # 点击添加视频按钮
    def click_add_video(self):
        self.click(self._page.Add_video_button)

    # 搜索视频
    def search(self, text):
        self.send_keys(self._page.Search_bor, text,need_enter=True)        
        
    # 选择视频
    def video(self):
        self.click(self._page.video)
     
    
    # 移除第一个视频视频
    def click_Remove_button(self):
        self._page.one_video
        self.click(self._page.Remove_button)
      
    #def two_video(self):
       # self.click(self._page.Two_video)
        
    #def Three_video(self):
    
        #self.click(self._page.Three_video)
    
    #def Four_video(self):
        #self.click(self._page.Four_video)
        
    # 第二个视频移动到第一个视频
    def click_Move_UP_button(self):
        btn_str = self.find_elements(*self._page.Move_UP_button)
        
        for btn in btn_str:
            atr = btn.get_attribute("disabled")
            if atr != 'true':
                btn.click()

    
    # 向下移动视频
    def click_Move_Down_button(self):
        self.click(self._page.Move_Down_button)
        
        
    #点击 Cancel_button
    def click_Cancel_button(self):
        self.click(self._page.Cancel_button)
        
    #点击 Save_button
    def click_Save_button(self):
        self.click(self._page.Save_button)
        
    #点击 Home_button
    def click_Home_button(self):
        self.click(self._page.Home_button)
        
