from psychopy import event, core
from time import sleep
from numpy import nan
import sys
import pandas as pd
import datetime
import keyboard
import voice_input
import expUI as UI



def testLoopVisual(win, stimuli, resolution=[600,600], voice=True, language="it", stop_rule="explorative", run_time=60):
    clock = core.Clock()
    win.clearBuffer()

    stimuli.loc[:, ["answer", "time", "auto_score", "correct"]] = nan * 4
    stimuli["new_level"] = stimuli.loc[:,"level"].diff()

    timer = core.Clock()
    timer.reset()

    event.waitKeys()

    for index in stimuli.index:
        correct = stimuli.loc[index, "stimuli"]
        correct = "".join(str(n) for n in correct)

        UI.showStimuli(win, stimuli.loc[index], resolution=resolution, voice=voice, language=language)
        UI.emptyScreen(win, resolution=resolution)

        clock.reset()

        new_input = UI.userInput()[0]

        time = clock.getTime()

        new_input = str(new_input).replace(" ","")  
        new_input = str(new_input).replace(",","")  

        stimuli.loc[index, ["time", "answer", "auto_score"]] = time, new_input, int((new_input) == str(correct))

        print("You pressed next")
        UI.emptyScreen(win)
        pd.DataFrame(stimuli).to_csv(sys.path[0] + '/temp/temp_' + str(datetime.date.today()) + '.csv')
        sleep(1)

        while True:
            if runStopRule(stop_rule, stimuli, index, timer, run_time):
                break
            else:
                return stimuli

    return stimuli   



def testLoopAudio(win, stimuli, language="it", resolution=[600,600], voice=True, stop_rule="explorative", run_time=60):
    clock = core.Clock()
    win.clearBuffer()


    stimuli.loc[:, ["answer", "time", "auto_score", "correct"]] = nan * 4
    stimuli["new_level"] = stimuli.loc[:,"level"].diff()

    timer = core.Clock()
    timer.reset()

    for index in stimuli.index:
        voice_input.voiceLoad()

        correct = stimuli.loc[index, "stimuli"]
        correct = "".join(str(n) for n in correct)
        print("The correct answer is {}".format(correct))

        UI.showStimuli(win, stimuli.loc[index], resolution=resolution, voice=voice)
        UI.emptyScreen(win, resolution=resolution)

        clock.reset()
        
        answer = voice_input.Answer(language=language)
        answer = str(answer).replace(" ","")    

        time = clock.getTime()

        while True:
            new_input = keyboard.read_event(suppress=True)

            if new_input.event_type == "up":
                continue

            if (new_input.name == "y" or new_input.name == "n"):
                print("You said {}".format(answer))
                print("Is the answer correct? {}". format(str(answer == correct)))

                stimuli.loc[index, ["time", "answer", "auto_score"]] = time, answer, int(answer == correct)

                if (new_input.name == "y"):
                    stimuli.loc[index, ["correct"]] = 1
                else:
                    stimuli.loc[index, ["correct"]] = 0

                UI.emptyScreen(win, resolution=resolution)
                pd.DataFrame(stimuli).to_csv(sys.path[0] + '/temp/temp_' + str(datetime.date.today()) + '.csv')
                break

        while True:
            if runStopRule(stop_rule, stimuli, index, timer, run_time):
                break
            else:
                return stimuli
            
    return stimuli



def runStopRule(stop_rule, stimuli, index, timer, run_time):
    n_trials = stimuli["trial"].max() + 1

    new_level = stimuli.loc[(index+1), "new_level"] > 0
    fail_previous_level = sum(stimuli.loc[(index-n_trials):index, "correct"]) < 1

    if stop_rule == "Explore" and fail_previous_level and new_level: 
        return False
    if stop_rule == "Timer" and timer.getTime() > run_time:
        #print(timer.getTime())
        return False
    if stop_rule == "None": 
        return False
    else:
        return True

