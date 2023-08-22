import random
import pandas as pd


def createStimuli(n_trials = range(1,4), n_levels = range(2,10)):

    stimuli = []

    for level in n_levels:
        for trial in range(0, n_trials):
            stimuli.append([level,
                            trial,
                            random.sample(range(0, 10), level)])

    stimuli = pd.DataFrame(stimuli, columns=["level", "trial", "stimuli"])

    return stimuli





