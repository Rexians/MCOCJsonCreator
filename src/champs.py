from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By 


class ChampsInfo():
    def __init__(self) -> None:
        pass

    def get_champ_info(self, champname, tier, rank, signature):
        url = f"https://auntm.ai/champions/{champname}/tier/{tier}"
        opts = webdriver.ChromeOptions()
        opts.add_argument("--no-sandbox");
        opts.add_argument("--disable-dev-shm-usage");
        #opts.add_argument(" --headless");
        opts.add_argument("--disable-gpu")        
        browser = webdriver.Chrome(options=opts)
        try:
            browser.get(url)
            browser.maximize_window()
            
            browser.find_element(By.ID, 'rankDropdown').click()
            browser.find_element(By.XPATH, f"//*[contains(text(), 'RANK {rank}')]").click()
            sig_json = 0
            if signature !=0:
                
                browser.find_element(By.ID, 'sigDropdown').click()
                sig_select = browser.find_elements(By.XPATH, f"//*[contains(text(), '{signature}')]")

                for x in sig_select:
                                        
                    if x.text == f'{signature}' and x.get_attribute('class') == 'dropdown-item':
                        print('     ')
                        x.click()
                        sig_json = x.text
                    else:
                        continue    
            
            name_acc = browser.find_element(By.CSS_SELECTOR, '.sc-bZSQDF')
            link_acc = browser.find_element(By.CSS_SELECTOR, 'div.sc-bkzZxe:nth-child(1) > img:nth-child(1) ').get_attribute("src")
            prestige_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(9) > div:nth-child(2)')
            hp_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(10) > div:nth-child(2)')
            attack_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(11) > div:nth-child(2)')
            crit_rate_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(12) > div:nth-child(2)')
            crit_dmge_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(13) > div:nth-child(2)')
            armor_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(14) > div:nth-child(2)')
            block_prof_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(15) > div:nth-child(2)')
            energy_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(16) > div:nth-child(2)')
            physical_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(17) > div:nth-child(2)')
            crit_resist_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-dmlrTW:nth-child(18) > div:nth-child(2)')
            sig_info_access = browser.find_element(By.CSS_SELECTOR, 'div.sc-eGCarw:nth-child(2) > div:nth-child(1)')
            self.champsjson = {
                "name" : name_acc.text,
                "rank" : rank,
                "prestige" : prestige_access.text,
                "hp" : hp_access.text,
                "attack" : attack_access.text,
                "crit_rate" : crit_rate_access.text,
                "crit_dmge" : crit_dmge_access.text,
                "armor" : armor_access.text,
                "block_prof" : block_prof_access.text,
                "energy_resist" : energy_resist_access.text,
                "physical_resist" : physical_resist_access.text,
                "crit_resist" : crit_resist_access.text,
                "sig_number" : sig_json,
                "sig_info" : sig_info_access.text,
                "url_page" : url,
                "champid" : f"{champname}+{tier}+{rank}+{signature}",
                "img_potrait" : link_acc
            }   
            browser.close()    
        except:
            raise LookupError