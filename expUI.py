from psychopy import gui, visual, event
from time import sleep
import playsound
import sys


gray = '#969696'
black = '#000000'
white = '#FFFFFF'

language = 'it'


def window(resolution = [600, 600], fullscreen = False):
    win = visual.Window(resolution, units="pix",  color=gray, colorSpace='hex', fullscr=fullscreen, monitor = "testMonitor")
    win.setMouseVisible(True)
    return win


def emptyScreen(win, resolution = [600, 600]):
    background = visual.Rect(win, width=resolution[0]+10, height=resolution[1]+10, fillColor=black, fillColorSpace='hex')
    background.draw()

    # Elements are only displayed after the flip command is executed
    win.flip()


def showStimuli(win, stimulus, resolution = [600, 600], voice=True, language="it"):

    for number in stimulus["stimuli"]:
        background = visual.Rect(win, width=resolution[0]+10, height=resolution[1]+10, fillColor=black, fillColorSpace='hex')
        msg2 = visual.TextStim(win, text=number, color=white, height=200, colorSpace='hex',anchorHoriz='center', anchorVert='center')
               
        background.draw()
        msg2.draw()
        win.flip()

        if voice:
            dir = sys.path[0].replace("\\", "/") + "/audio/number_" + language + "_" + str(number) + ".mp3"
            playsound.playsound(dir)
            sleep(0.3)

        else:       
            sleep(1)


def showInstructions(win, resolution = [600, 600]):
    background = visual.Rect(win, width=resolution[0]+10, height=resolution[1]+10, fillColor=gray, fillColorSpace='hex')
    msg1 = visual.TextStim(win, text="press any key to start", color=white, height=20, colorSpace='hex')
    background.draw()
    msg1.draw()
    win.flip()

    event.waitKeys()



def userData():
    myDlg = gui.Dlg(title="Digit span")
    myDlg.addText('Subject info')
    myDlg.addField('ID:', )
    myDlg.addField('Condition:', )
    myDlg.addText('Experiment Info')
    myDlg.addField('Language:', choices=["it", "en", "de"])
    myDlg.addField('Input:', choices=["Voice", "Keyboard"])
    myDlg.addField('Read numbers:', choices=[True, False])
    myDlg.addField('Levels:', "2,3,4")
    myDlg.addField('Trials per level:', "3")
    myDlg.addField('Stop rule:', choices=["Explorative", "Timer", "None"])
    myDlg.addField('Run time (if Stop rule = timer):', 60)
    exp_data = myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        exp_data = dict(zip(["ID", "condition", "language", "input", "voice", "levels", "trials", "stop_rule", "run_time"], exp_data))
        exp_data["levels"] = list(map(int, exp_data["levels"].split(',')))
        exp_data["trials"] = int(exp_data["trials"])
        exp_data["run_time"] = int(exp_data["run_time"])
        print(exp_data)
        return exp_data
    else:
        quit()


def userInput():
    myDlg = gui.Dlg(title="Digit span")
    myDlg.addField('Sequence:')
    exp_data = myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        print(exp_data)
        return exp_data