from visual_stim import createStimuli
from testLoops import testLoopVisual, testLoopAudio
import sys
import datetime
import pandas as pd
import expUI as UI


resolution = [400, 400]


def main():
    win = UI.window(resolution=resolution, fullscreen=False)
    exp_data = UI.userData()
    stimuli = createStimuli(n_levels=exp_data["levels"], n_trials=exp_data["trials"])

    UI.showInstructions(win, resolution=resolution)

    if exp_data["input"] == "Voice":

        data = testLoopAudio(win, 
                             stimuli, 
                             resolution=resolution, 
                             voice=exp_data["voice"], 
                             language=exp_data["language"], 
                             stop_rule=exp_data["stop_rule"],
                             run_time=exp_data["run_time"])
        
        temp = pd.DataFrame(map(lambda x: data[data["level"] == x]["correct"].sum() / exp_data["trials"], 
                                data["level"].unique()), 
                                index = data["level"].unique(),                         
                                columns=["correct"])
    else:

        data = testLoopVisual(win, 
                              stimuli, 
                              resolution=resolution, 
                              voice=exp_data["voice"], 
                              language=exp_data["language"], 
                              stop_rule=exp_data["stop_rule"],
                              run_time=exp_data["run_time"])
        
        temp = pd.DataFrame(map(lambda x: data[data["level"] == x]["auto_score"].sum() / exp_data["trials"], 
                                data["level"].unique()), 
                                index = data["level"].unique(),                         
                                columns=["correct"])
        
    print(temp)
        
    pd.DataFrame(data).to_csv(sys.path[0] + '/data/' + exp_data["ID"] + "_" + exp_data["condition"] + "_" + str(datetime.date.today()) + '.csv')
    print("Experiment saved as:" + exp_data["ID"] + "_" + str(datetime.date.today()) + '.csv')



if __name__ == "__main__":
    main()    
