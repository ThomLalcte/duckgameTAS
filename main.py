import keyboard as k
from time import sleep

records = []
recording = False

def jump(jumpHeight:int):
    k.press("w")
    sleep(jumpHeight/59.2);
    k.release("w")

def jumpHover(jumpHeight:int):
    k.press("w")
    sleep(jumpHeight/59.2);
    k.release("w")
    sleep(5/59.2);
    k.press("w")

def angle(data):
    secnd = ""
    if data[1]=="d":
        secnd = "a"
    else:
        secnd = "d"

    k.press(data[1])
    sleep(1/59.2);
    k.release(data[1])
    sleep(3/59.2);
    k.press(secnd)
    #shoot
    sleep(data[0]/59.2);
    k.press("v")
    sleep(3/59.2);
    k.release(secnd)
    k.release("v")
    sleep(1/59.2)
    k.press("v")
    sleep(1/59.2)
    k.release("v")

def shootShutgun():
    k.press("v")
    sleep(1/59.2)
    k.release("v")
    sleep(1/59.2)
    k.press("v")
    sleep(1/59.2)
    k.release("v")

def reload():
    k.press("v")
    sleep(1/59.2)
    k.release("v")

def cuak():
    k.press("e")
    sleep(1/59.2)
    k.release("e")

def quadAngles():
    seq = [[jumpHover, 0, 20], [angle, 2, [0.5,"d"]], [angle, 2, [0.5,"a"]], [angle, 2, [0.5,"d"]], [angle, 2, [0.5,"a"]], [k.release, 1, "w"]]
    playback(seq)
#[action, time delay after action, action parameters]
# sequence = [[jump, 30, [1]],[jump, 30, [3]],[jump, 30, [10]]]
# sequence = [[shootShutgun, 3],[shootShutgun, 3],[shootShutgun, 3]]
# sequence = [[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1],[cuak, 1]]


def playback(seq):
    for action in seq:
        if len(action)==3:
            action[0](action[2])
        else:
            action[0]()
        sleep(action[1]/59.2);
    

if __name__ == "__main__":
    # k.add_hotkey("1",record,suppress=True)
    sequence = [[quadAngles, 0]]
    k.add_hotkey("2",playback,[sequence],suppress=True)
    k.wait()

# def record():
#     global recording
#     if recording:
#         records.append(k.stop_recording())
#         print("Done Recording")
#         recording = False
#     else:
#         print("Recording")
#         k.start_recording()
#         recording = True

# def playback():
#     print("Playing")
#     k.play(records[-1])
#     print("playback over")