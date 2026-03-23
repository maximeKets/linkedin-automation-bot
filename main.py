import pyautogui
import time
import random
import pyperclip
import sys


MESSAGES = [
    "votre message 1",
    "votre message 2",
    "votre message 3",
    "votre message 4",
]


def find_and_click(image_path, confidence=0.8, retries=3):
    """Cherche l'image avec plusieurs tentatives avant d'alerter."""
    for attempt in range(retries):
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if location:
                pyautogui.moveTo(location.x, location.y,
                                 duration=random.uniform(1.2, 2.5),
                                 tween=pyautogui.easeInOutQuad)
                time.sleep(0.5)
                pyautogui.click()
                return True
        except Exception as e:
            if "ImageNotFoundException" not in type(e).__name__:
                print(f"Erreur : {e}")
                sys.exit(1)
            pass

        if retries > 1:
            print(f"Tentative {attempt + 1}/{retries} pour {image_path}...")
            time.sleep(2)

    if retries > 1:
        print(f"ERREUR : Impossible de trouver {image_path}")
    return False


def run_automation(nb_invits=100):
    print("Script lancé. Aller sur la page linkedIn sur votre navigateur")
    time.sleep(5)

    invitations_sent = 0
    consecutive_scrolls = 0

    while invitations_sent < nb_invits:
        print(f"\n--- RECHERCHE PROFIL ({invitations_sent}/{nb_invits} envoyées) ---")

        # 1. On cherche le bouton Se connecter (retries=1 pour ne pas perdre 6 secondes)
        if find_and_click('./image/connect_btn.png', retries=1):
            consecutive_scrolls = 0
            print("Bouton 'Se connecter' trouvé et cliqué !")
            time.sleep(random.uniform(2, 4))

            print("Recherche du bouton 'Ajouter une note'...")
            if find_and_click('./image/add_note_btn.png'):
                print("Bouton 'Ajouter une note' cliqué. Rédaction en cours...")
                time.sleep(1.5)

                msg = random.choice(MESSAGES).format(name="")
                pyperclip.copy(msg)
                
                if sys.platform == "darwin":
                    pyautogui.keyDown('command')
                    pyautogui.press('v')
                    pyautogui.keyUp('command')
                else:
                    pyautogui.hotkey('ctrl', 'v')
                    
                time.sleep(1.5)

                print("Recherche du bouton 'Envoyer'...")
                if find_and_click('./image/send_btn.png'):
                    invitations_sent += 1
                    print(f"Invitation {invitations_sent}/{nb_invits} envoyée avec succès !")
                    
                    pause = random.uniform(5, 12)
                    time.sleep(pause)
                else:
                    print("Erreur : Impossible de trouver le bouton Envoyer (send_btn.png).")
                    sys.exit("Arrêt automatique du script.")
            else:
                print("Erreur : Impossible de trouver le bouton Ajouter une note (add_note_btn.png).")
                sys.exit("Arrêt automatique du script.")
                
        # 2. Si on ne trouve pas de profil sur l'écran visible, ON SCROLL !
        else:
            pyautogui.scroll(-150) 
            time.sleep(1.5) 
            consecutive_scrolls += 1
            try:
                if pyautogui.locateCenterOnScreen('./image/connect_btn.png', confidence=0.8):
                    continue
            except Exception as e:
                if "ImageNotFoundException" not in type(e).__name__:
                    print(f"Erreur : {e}")
                    sys.exit(1)

            try:
                if pyautogui.locateCenterOnScreen('./image/next_page.png', confidence=0.8):
                    find_and_click('./image/next_page.png', retries=1)
                    time.sleep(6)
                    consecutive_scrolls = 0
            except Exception as e:
                if "ImageNotFoundException" not in type(e).__name__:
                    print(f"Erreur : {e}")
                    sys.exit(1)

            if consecutive_scrolls > 10:
                sys.exit(1)


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    run_automation()