try:
    import requests
    r = requests.get("https://www.downloadpirate.com/video-copilot-motionpulse-velocity-sound-effects-pack/")
    print(r.text)
except Exception as e:
    print(e)