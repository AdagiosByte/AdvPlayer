import pyautogui
import time


while True:
	time.sleep(7)
	pyautogui.click(400, 500)
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(30) #load time

	pyautogui.click(1200, 900) #close popup
	pyautogui.tripleClick(1280, 250) #dollar tag

	#buy upgrades
	pyautogui.click(200, 550) #upgrades
	time.sleep(0.5)
	pyautogui.click(1100, 750) #quick buy
	time.sleep(0.05)
	pyautogui.doubleClick(1280, 270, 0.25) #close menu
	time.sleep(0.05)

	#buy companies
	#pyautogui.doubleClick(1280, 250) #dollar tag
	pyautogui.click(700, 520) #buy newspapers
	pyautogui.click(700, 640) #buy carwashs
	pyautogui.click(700, 760) #buy pizzas
	pyautogui.click(700, 880) #buy donuts
	pyautogui.click(700, 400) #buy lemons
	pyautogui.click(1100, 880) #buy oil rigs
	pyautogui.click(1100, 760) #buy banks
	pyautogui.click(1100, 640) #buy movie studios
	pyautogui.click(1100, 520) #buy hockey teams
	pyautogui.click(1100, 400) #buy shrimp

	#crash game
	pyautogui.click(700, 950) #launch
	time.sleep(0.5)
	pyautogui.click(700, 900) #increase funds
	time.sleep(0.5)
	pyautogui.keyDown('ctrl')
	pyautogui.press('r')
	pyautogui.keyUp('ctrl')
