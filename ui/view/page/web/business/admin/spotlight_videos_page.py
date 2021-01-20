# coding=utf-8
# @Time    :
# @Author  :
# @File    : spotlight_videos_page.py

from selenium.webdriver.common.by import By

class SpotligtPage:
    
    settings_button = (By.XPATH, '//*[@id="O365_MainLink_Settings"]/div')
    #settings_button = (By.XPATH, '//span[@class="ms-Icon--Settings"]')
    #Admin_settings_button = (By.XPATH, '//input[@id="AdminSettingsLink or @value="管理设置"]')
    Admin_settings_button = (By.ID, 'AdminSettingsLink')
    Spotlight_videos_button = (By.XPATH, '//*[@id="manage-stream-navigation"]/nav/ul/li[2]/button')
    Add_video_button = (By.XPATH, '//button[@class="add-video c-action-trigger ng-binding"]')
    Search_bor = (By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/admin-setting-detail[1]/div[1]/section[1]/div[1]/div[2]/spotlight-videos[1]/div[1]/spotlight-list[1]/div[1]/div[2]/video-channel-search[1]/div[1]/div[1]/input[1]')
    video = ((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/admin-setting-detail[1]/div[1]/section[1]/div[1]/div[2]/spotlight-videos[1]/div[1]/spotlight-list[1]/div[1]/div[2]/video-channel-search[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]'))
    one_video = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/admin-setting-detail[1]/div[1]/section[1]/div[1]/div[2]/spotlight-videos[1]/div[1]/spotlight-list[1]/div[1]/items-list[1]/div[1]/div[1]/div[1]/item[1]/spotlight-video-item[1]/div[1]/list-row[1]/ng-transclude[1]/list-cell[4]/div[1]/div[1]/ng-transclude[1]')
    #Two_video = (By.XPATH,'//a[@id="video-link-06d1fb5d-1500-a60d-6310-f1eb433b05b2"]')
    Two_video = (By.XPATH,'//a[@href="/video/06d1fb5d-1500-a60d-6310-f1eb433b05b2"]')
    #Two_video = (By.XPATH,'//div[@class="ng-scope ng-isolate-scope"]/tbody/tr[2]/td[5]')
    #Two_video = (By.XPATH,'//items-list[@class="ng-isolate-scope"]/tbody/tr[3]/td[5]')
    
    #Three_video = ((By.XPATH,'//a[@id="video-link-06d1fb5d-1500-a60d-0cae-f1eb435845fc"]'))
    Three_video =(By.XPATH,'//div[@class=" ng-isolate-scope"]/tbody/tr[4]/td[5]')
   # Three_video = ((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/admin-setting-detail[1]/div[1]/section[1]/div[1]/div[2]/spotlight-videos[1]/div[1]/spotlight-list[1]/div[1]/items-list[1]/div[1]/div[1]/div[3]/item[1]/spotlight-video-item[1]/div[1]/list-row[1]/ng-transclude[1]'))
    #Four_video= ((By.XPATH, '//*[@id="video-link-10f4fb5d-1500-a936-205a-f1eaa0ff141b"]/span'))
    #Move_UP_button = (By.CLASS_NAME, 'move-up c-action-trigger ng-scope')
    Move_UP_button = (By.XPATH, '//button[@class="move-up c-action-trigger ng-scope"]')
    Move_Down_button= (By.XPATH, '//button[@class="move-down c-action-trigger ng-scope"]')
    Remove_button = (By.XPATH, '//button[@class="remove c-action-trigger ng-scope"]')
    Cancel_button = (By.XPATH,'//button[contains(text(),"Cancel")]')
    Save_button = (By.XPATH,'//button[contains(text(),"Save")]')
    Home_button= (By.XPATH,'//a[@class="home-link ng-binding"]')
    
