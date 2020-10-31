#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Mon Oct 26 17:01:54 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'Big5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sabrinado/Desktop/Big5_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Big_5"
Big_5Clock = core.Clock()
IntroScreen = visual.TextStim(win=win, name='IntroScreen',
    text='Big 5 Test',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Spatial Anxiety Scale\n\nOn the next page, you will be presented a number of scenarios. Please rate your anxiety on the 5 point scale based off the scenario given.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "SpatialAnxietyScale"
SpatialAnxietyScaleClock = core.Clock()
scenario1 = visual.TextStim(win=win, name='scenario1',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
notAtAll = visual.TextStim(win=win, name='notAtAll',
    text='Not at All',
    font='Times New Roman',
    pos=(-0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
veryMuch = visual.TextStim(win=win, name='veryMuch',
    text='Very much',
    font='Times New Roman',
    pos=(0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')

# Initialize components for Routine "RiskBehaviorScale"
RiskBehaviorScaleClock = core.Clock()
riskBehaviorScaleScreen = visual.TextStim(win=win, name='riskBehaviorScaleScreen',
    text='Risk Behavior Scale\n\nFor each of the statements, please indicate the likelihood of engaging in each activity. Provide a rating from 1 to 5, using the scale.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "riskBehaviorScaleScreen_2"
riskBehaviorScaleScreen_2Clock = core.Clock()
activity = visual.TextStim(win=win, name='activity',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
notAtAll2 = visual.TextStim(win=win, name='notAtAll2',
    text='Extremely unlikely',
    font='Times New Roman',
    pos=(-0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ExtremelyLikely = visual.TextStim(win=win, name='ExtremelyLikely',
    text='Extremely likely',
    font='Arial',
    pos=(0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')

# Initialize components for Routine "RiskPerception"
RiskPerceptionClock = core.Clock()
riskPerceptionInstructions = visual.TextStim(win=win, name='riskPerceptionInstructions',
    text='People often see some risk in situations that contain uncertainty about what the outcome or consequences will be and for which there is the possibility of ‘bad’ consequences. However, riskiness is a very personal and intuitive notion, and we are interested in your gut level assessment of how risky each situation is. \n\nFor each of the following statements, please indicate how risky you perceive each situation. Provide a rating from 1 to 5 using the scale provided. ',
    font='Times New Roman',
    pos=(0, 0), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "riskPerceptionActual"
riskPerceptionActualClock = core.Clock()
riskPerceptionActivity2 = visual.TextStim(win=win, name='riskPerceptionActivity2',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_4 = visual.RatingScale(win=win, name='rating_4', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
notAtAllRisky = visual.TextStim(win=win, name='notAtAllRisky',
    text='Not at all risky',
    font='Times New Roman',
    pos=(-0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ExtremelyRisky = visual.TextStim(win=win, name='ExtremelyRisky',
    text='Extremely risky\n',
    font='Times New Roman',
    pos=(0.4,-0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ModeratelyRisky = visual.TextStim(win=win, name='ModeratelyRisky',
    text='Moderately risky',
    font='Times New Roman',
    pos=(0, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "instrBenefits"
instrBenefitsClock = core.Clock()
expBenefits = visual.TextStim(win=win, name='expBenefits',
    text='Expected Benefits Scale\n\nFor each of the following statements, please indicate the benefits you would obtain from each situation. Provide a rating from 1 to 5 using the scale. ',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "expectedBenefits_2"
expectedBenefits_2Clock = core.Clock()
riskBenefitsScale = visual.TextStim(win=win, name='riskBenefitsScale',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
noBenefits = visual.TextStim(win=win, name='noBenefits',
    text='No benefits at all',
    font='Times New Roman',
    pos=(-0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_3 = visual.RatingScale(win=win, name='rating_3', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
greatBenefits = visual.TextStim(win=win, name='greatBenefits',
    text='Great benefits',
    font='Times New Roman',
    pos=(0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
moderateBenefits = visual.TextStim(win=win, name='moderateBenefits',
    text='Moderate benefits',
    font='Times New Roman',
    pos=(0, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "big5"
big5Clock = core.Clock()
big5Screen = visual.TextStim(win=win, name='big5Screen',
    text='The Big Five\n\nThe following slides will display a number of characteristics that may or may not apply to you. For example, do you agree that you are someone who likes to spend time with others? Please choose a number next to each statement to indicate the extent to which you agree or disagree with the statement. ',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "big5Screen_2"
big5Screen_2Clock = core.Clock()
rating_5 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=5, labels=[''], scale='')
characText = visual.TextStim(win=win, name='characText',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Someone = visual.TextStim(win=win, name='Someone',
    text='I am someone who…',
    font='Times New Roman',
    pos=(-0.33, 0.2), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
disagreeStrongly = visual.TextStim(win=win, name='disagreeStrongly',
    text='Disagree\nStrongly',
    font='Times New Roman',
    pos=(-0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
disagreeALittle = visual.TextStim(win=win, name='disagreeALittle',
    text='Disagree\na little',
    font='Times New Roman',
    pos=(0.2, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Neutral = visual.TextStim(win=win, name='Neutral',
    text='Neutral;\nno opinion',
    font='Arial',
    pos=(0, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
AgreeALittle = visual.TextStim(win=win, name='AgreeALittle',
    text='Agree\na little',
    font='Times New Roman',
    pos=(0.2, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
AgreeStrongly = visual.TextStim(win=win, name='AgreeStrongly',
    text='Agree\nstrongly',
    font='Times New Roman',
    pos=(0.4, -0.2), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Big_5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Big_5Components = [IntroScreen, key_resp_3]
for thisComponent in Big_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Big_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Big_5"-------
while continueRoutine:
    # get current time
    t = Big_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Big_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IntroScreen* updates
    if IntroScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroScreen.frameNStart = frameN  # exact frame index
        IntroScreen.tStart = t  # local t and not account for scr refresh
        IntroScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroScreen, 'tStartRefresh')  # time at next scr refresh
        IntroScreen.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Big_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Big_5"-------
for thisComponent in Big_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('IntroScreen.started', IntroScreen.tStartRefresh)
thisExp.addData('IntroScreen.stopped', IntroScreen.tStopRefresh)
# the Routine "Big_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructions, key_resp_2]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../Library/CELSYS/spatialAnxietyScale1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "SpatialAnxietyScale"-------
    continueRoutine = True
    # update component parameters for each repeat
    scenario1.setText(Scenario)
    rating.reset()
    # keep track of which components have finished
    SpatialAnxietyScaleComponents = [scenario1, notAtAll, veryMuch, rating]
    for thisComponent in SpatialAnxietyScaleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SpatialAnxietyScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SpatialAnxietyScale"-------
    while continueRoutine:
        # get current time
        t = SpatialAnxietyScaleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SpatialAnxietyScaleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scenario1* updates
        if scenario1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scenario1.frameNStart = frameN  # exact frame index
            scenario1.tStart = t  # local t and not account for scr refresh
            scenario1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scenario1, 'tStartRefresh')  # time at next scr refresh
            scenario1.setAutoDraw(True)
        
        # *notAtAll* updates
        if notAtAll.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            notAtAll.frameNStart = frameN  # exact frame index
            notAtAll.tStart = t  # local t and not account for scr refresh
            notAtAll.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notAtAll, 'tStartRefresh')  # time at next scr refresh
            notAtAll.setAutoDraw(True)
        
        # *veryMuch* updates
        if veryMuch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            veryMuch.frameNStart = frameN  # exact frame index
            veryMuch.tStart = t  # local t and not account for scr refresh
            veryMuch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(veryMuch, 'tStartRefresh')  # time at next scr refresh
            veryMuch.setAutoDraw(True)
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SpatialAnxietyScaleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SpatialAnxietyScale"-------
    for thisComponent in SpatialAnxietyScaleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('scenario1.started', scenario1.tStartRefresh)
    trials.addData('scenario1.stopped', scenario1.tStopRefresh)
    trials.addData('notAtAll.started', notAtAll.tStartRefresh)
    trials.addData('notAtAll.stopped', notAtAll.tStopRefresh)
    trials.addData('veryMuch.started', veryMuch.tStartRefresh)
    trials.addData('veryMuch.stopped', veryMuch.tStopRefresh)
    thisExp.addData('lastRating', ((rating.markerPlacedAt*0.20)))
    
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    trials.addData('rating.started', rating.tStart)
    trials.addData('rating.stopped', rating.tStop)
    # the Routine "SpatialAnxietyScale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "RiskBehaviorScale"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
RiskBehaviorScaleComponents = [riskBehaviorScaleScreen, key_resp_4]
for thisComponent in RiskBehaviorScaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RiskBehaviorScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RiskBehaviorScale"-------
while continueRoutine:
    # get current time
    t = RiskBehaviorScaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RiskBehaviorScaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *riskBehaviorScaleScreen* updates
    if riskBehaviorScaleScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        riskBehaviorScaleScreen.frameNStart = frameN  # exact frame index
        riskBehaviorScaleScreen.tStart = t  # local t and not account for scr refresh
        riskBehaviorScaleScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(riskBehaviorScaleScreen, 'tStartRefresh')  # time at next scr refresh
        riskBehaviorScaleScreen.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=None, waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RiskBehaviorScaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RiskBehaviorScale"-------
for thisComponent in RiskBehaviorScaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('riskBehaviorScaleScreen.started', riskBehaviorScaleScreen.tStartRefresh)
thisExp.addData('riskBehaviorScaleScreen.stopped', riskBehaviorScaleScreen.tStopRefresh)
# the Routine "RiskBehaviorScale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../Library/CELSYS/activities.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "riskBehaviorScaleScreen_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    activity.setText(C)
    rating_2.reset()
    # keep track of which components have finished
    riskBehaviorScaleScreen_2Components = [activity, notAtAll2, ExtremelyLikely, rating_2]
    for thisComponent in riskBehaviorScaleScreen_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    riskBehaviorScaleScreen_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "riskBehaviorScaleScreen_2"-------
    while continueRoutine:
        # get current time
        t = riskBehaviorScaleScreen_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=riskBehaviorScaleScreen_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *activity* updates
        if activity.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            activity.frameNStart = frameN  # exact frame index
            activity.tStart = t  # local t and not account for scr refresh
            activity.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(activity, 'tStartRefresh')  # time at next scr refresh
            activity.setAutoDraw(True)
        
        # *notAtAll2* updates
        if notAtAll2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            notAtAll2.frameNStart = frameN  # exact frame index
            notAtAll2.tStart = t  # local t and not account for scr refresh
            notAtAll2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notAtAll2, 'tStartRefresh')  # time at next scr refresh
            notAtAll2.setAutoDraw(True)
        
        # *ExtremelyLikely* updates
        if ExtremelyLikely.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExtremelyLikely.frameNStart = frameN  # exact frame index
            ExtremelyLikely.tStart = t  # local t and not account for scr refresh
            ExtremelyLikely.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtremelyLikely, 'tStartRefresh')  # time at next scr refresh
            ExtremelyLikely.setAutoDraw(True)
        # *rating_2* updates
        if rating_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_2.frameNStart = frameN  # exact frame index
            rating_2.tStart = t  # local t and not account for scr refresh
            rating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_2, 'tStartRefresh')  # time at next scr refresh
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in riskBehaviorScaleScreen_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "riskBehaviorScaleScreen_2"-------
    for thisComponent in riskBehaviorScaleScreen_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('activity.started', activity.tStartRefresh)
    trials_2.addData('activity.stopped', activity.tStopRefresh)
    trials_2.addData('notAtAll2.started', notAtAll2.tStartRefresh)
    trials_2.addData('notAtAll2.stopped', notAtAll2.tStopRefresh)
    trials_2.addData('ExtremelyLikely.started', ExtremelyLikely.tStartRefresh)
    trials_2.addData('ExtremelyLikely.stopped', ExtremelyLikely.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating_2.response', rating_2.getRating())
    trials_2.addData('rating_2.rt', rating_2.getRT())
    trials_2.addData('rating_2.started', rating_2.tStart)
    trials_2.addData('rating_2.stopped', rating_2.tStop)
    # the Routine "riskBehaviorScaleScreen_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "RiskPerception"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
RiskPerceptionComponents = [riskPerceptionInstructions, key_resp_5]
for thisComponent in RiskPerceptionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RiskPerceptionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RiskPerception"-------
while continueRoutine:
    # get current time
    t = RiskPerceptionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RiskPerceptionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *riskPerceptionInstructions* updates
    if riskPerceptionInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        riskPerceptionInstructions.frameNStart = frameN  # exact frame index
        riskPerceptionInstructions.tStart = t  # local t and not account for scr refresh
        riskPerceptionInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(riskPerceptionInstructions, 'tStartRefresh')  # time at next scr refresh
        riskPerceptionInstructions.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=None, waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RiskPerceptionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RiskPerception"-------
for thisComponent in RiskPerceptionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('riskPerceptionInstructions.started', riskPerceptionInstructions.tStartRefresh)
thisExp.addData('riskPerceptionInstructions.stopped', riskPerceptionInstructions.tStopRefresh)
# the Routine "RiskPerception" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../Library/CELSYS/activities.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "riskPerceptionActual"-------
    continueRoutine = True
    # update component parameters for each repeat
    riskPerceptionActivity2.setText(AppendixC)
    rating_4.reset()
    # keep track of which components have finished
    riskPerceptionActualComponents = [riskPerceptionActivity2, rating_4, notAtAllRisky, ExtremelyRisky, ModeratelyRisky]
    for thisComponent in riskPerceptionActualComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    riskPerceptionActualClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "riskPerceptionActual"-------
    while continueRoutine:
        # get current time
        t = riskPerceptionActualClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=riskPerceptionActualClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *riskPerceptionActivity2* updates
        if riskPerceptionActivity2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            riskPerceptionActivity2.frameNStart = frameN  # exact frame index
            riskPerceptionActivity2.tStart = t  # local t and not account for scr refresh
            riskPerceptionActivity2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(riskPerceptionActivity2, 'tStartRefresh')  # time at next scr refresh
            riskPerceptionActivity2.setAutoDraw(True)
        # *rating_4* updates
        if rating_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_4.frameNStart = frameN  # exact frame index
            rating_4.tStart = t  # local t and not account for scr refresh
            rating_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_4, 'tStartRefresh')  # time at next scr refresh
            rating_4.setAutoDraw(True)
        continueRoutine &= rating_4.noResponse  # a response ends the trial
        
        # *notAtAllRisky* updates
        if notAtAllRisky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            notAtAllRisky.frameNStart = frameN  # exact frame index
            notAtAllRisky.tStart = t  # local t and not account for scr refresh
            notAtAllRisky.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(notAtAllRisky, 'tStartRefresh')  # time at next scr refresh
            notAtAllRisky.setAutoDraw(True)
        
        # *ExtremelyRisky* updates
        if ExtremelyRisky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExtremelyRisky.frameNStart = frameN  # exact frame index
            ExtremelyRisky.tStart = t  # local t and not account for scr refresh
            ExtremelyRisky.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExtremelyRisky, 'tStartRefresh')  # time at next scr refresh
            ExtremelyRisky.setAutoDraw(True)
        
        # *ModeratelyRisky* updates
        if ModeratelyRisky.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ModeratelyRisky.frameNStart = frameN  # exact frame index
            ModeratelyRisky.tStart = t  # local t and not account for scr refresh
            ModeratelyRisky.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ModeratelyRisky, 'tStartRefresh')  # time at next scr refresh
            ModeratelyRisky.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in riskPerceptionActualComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "riskPerceptionActual"-------
    for thisComponent in riskPerceptionActualComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('riskPerceptionActivity2.started', riskPerceptionActivity2.tStartRefresh)
    trials_3.addData('riskPerceptionActivity2.stopped', riskPerceptionActivity2.tStopRefresh)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('rating_4.response', rating_4.getRating())
    trials_3.addData('rating_4.rt', rating_4.getRT())
    trials_3.addData('rating_4.started', rating_4.tStart)
    trials_3.addData('rating_4.stopped', rating_4.tStop)
    trials_3.addData('notAtAllRisky.started', notAtAllRisky.tStartRefresh)
    trials_3.addData('notAtAllRisky.stopped', notAtAllRisky.tStopRefresh)
    trials_3.addData('ExtremelyRisky.started', ExtremelyRisky.tStartRefresh)
    trials_3.addData('ExtremelyRisky.stopped', ExtremelyRisky.tStopRefresh)
    trials_3.addData('ModeratelyRisky.started', ModeratelyRisky.tStartRefresh)
    trials_3.addData('ModeratelyRisky.stopped', ModeratelyRisky.tStopRefresh)
    # the Routine "riskPerceptionActual" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "instrBenefits"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
instrBenefitsComponents = [expBenefits, key_resp_6]
for thisComponent in instrBenefitsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrBenefitsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrBenefits"-------
while continueRoutine:
    # get current time
    t = instrBenefitsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrBenefitsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *expBenefits* updates
    if expBenefits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        expBenefits.frameNStart = frameN  # exact frame index
        expBenefits.tStart = t  # local t and not account for scr refresh
        expBenefits.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(expBenefits, 'tStartRefresh')  # time at next scr refresh
        expBenefits.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrBenefitsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrBenefits"-------
for thisComponent in instrBenefitsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('expBenefits.started', expBenefits.tStartRefresh)
thisExp.addData('expBenefits.stopped', expBenefits.tStopRefresh)
# the Routine "instrBenefits" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../Library/CELSYS/activities.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "expectedBenefits_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    riskBenefitsScale.setText(AppendixC)
    rating_3.reset()
    # keep track of which components have finished
    expectedBenefits_2Components = [riskBenefitsScale, noBenefits, rating_3, greatBenefits, moderateBenefits]
    for thisComponent in expectedBenefits_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    expectedBenefits_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "expectedBenefits_2"-------
    while continueRoutine:
        # get current time
        t = expectedBenefits_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=expectedBenefits_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *riskBenefitsScale* updates
        if riskBenefitsScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            riskBenefitsScale.frameNStart = frameN  # exact frame index
            riskBenefitsScale.tStart = t  # local t and not account for scr refresh
            riskBenefitsScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(riskBenefitsScale, 'tStartRefresh')  # time at next scr refresh
            riskBenefitsScale.setAutoDraw(True)
        
        # *noBenefits* updates
        if noBenefits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noBenefits.frameNStart = frameN  # exact frame index
            noBenefits.tStart = t  # local t and not account for scr refresh
            noBenefits.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noBenefits, 'tStartRefresh')  # time at next scr refresh
            noBenefits.setAutoDraw(True)
        # *rating_3* updates
        if rating_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_3.frameNStart = frameN  # exact frame index
            rating_3.tStart = t  # local t and not account for scr refresh
            rating_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_3, 'tStartRefresh')  # time at next scr refresh
            rating_3.setAutoDraw(True)
        continueRoutine &= rating_3.noResponse  # a response ends the trial
        
        # *greatBenefits* updates
        if greatBenefits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            greatBenefits.frameNStart = frameN  # exact frame index
            greatBenefits.tStart = t  # local t and not account for scr refresh
            greatBenefits.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(greatBenefits, 'tStartRefresh')  # time at next scr refresh
            greatBenefits.setAutoDraw(True)
        
        # *moderateBenefits* updates
        if moderateBenefits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moderateBenefits.frameNStart = frameN  # exact frame index
            moderateBenefits.tStart = t  # local t and not account for scr refresh
            moderateBenefits.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moderateBenefits, 'tStartRefresh')  # time at next scr refresh
            moderateBenefits.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expectedBenefits_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "expectedBenefits_2"-------
    for thisComponent in expectedBenefits_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('riskBenefitsScale.started', riskBenefitsScale.tStartRefresh)
    trials_4.addData('riskBenefitsScale.stopped', riskBenefitsScale.tStopRefresh)
    trials_4.addData('noBenefits.started', noBenefits.tStartRefresh)
    trials_4.addData('noBenefits.stopped', noBenefits.tStopRefresh)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('rating_3.response', rating_3.getRating())
    trials_4.addData('rating_3.rt', rating_3.getRT())
    trials_4.addData('rating_3.started', rating_3.tStart)
    trials_4.addData('rating_3.stopped', rating_3.tStop)
    trials_4.addData('greatBenefits.started', greatBenefits.tStartRefresh)
    trials_4.addData('greatBenefits.stopped', greatBenefits.tStopRefresh)
    trials_4.addData('moderateBenefits.started', moderateBenefits.tStartRefresh)
    trials_4.addData('moderateBenefits.stopped', moderateBenefits.tStopRefresh)
    # the Routine "expectedBenefits_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "big5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
big5Components = [big5Screen, key_resp_7]
for thisComponent in big5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
big5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "big5"-------
while continueRoutine:
    # get current time
    t = big5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=big5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *big5Screen* updates
    if big5Screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        big5Screen.frameNStart = frameN  # exact frame index
        big5Screen.tStart = t  # local t and not account for scr refresh
        big5Screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(big5Screen, 'tStartRefresh')  # time at next scr refresh
        big5Screen.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=None, waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in big5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "big5"-------
for thisComponent in big5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('big5Screen.started', big5Screen.tStartRefresh)
thisExp.addData('big5Screen.stopped', big5Screen.tStopRefresh)
# the Routine "big5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../Library/CELSYS/charac.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "big5Screen_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    rating_5.reset()
    characText.setText(Charac)
    # keep track of which components have finished
    big5Screen_2Components = [rating_5, characText, Someone, disagreeStrongly, disagreeALittle, Neutral, AgreeALittle, AgreeStrongly]
    for thisComponent in big5Screen_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    big5Screen_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "big5Screen_2"-------
    while continueRoutine:
        # get current time
        t = big5Screen_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=big5Screen_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating_5* updates
        if rating_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_5.frameNStart = frameN  # exact frame index
            rating_5.tStart = t  # local t and not account for scr refresh
            rating_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_5, 'tStartRefresh')  # time at next scr refresh
            rating_5.setAutoDraw(True)
        continueRoutine &= rating_5.noResponse  # a response ends the trial
        
        # *characText* updates
        if characText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            characText.frameNStart = frameN  # exact frame index
            characText.tStart = t  # local t and not account for scr refresh
            characText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(characText, 'tStartRefresh')  # time at next scr refresh
            characText.setAutoDraw(True)
        
        # *Someone* updates
        if Someone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Someone.frameNStart = frameN  # exact frame index
            Someone.tStart = t  # local t and not account for scr refresh
            Someone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Someone, 'tStartRefresh')  # time at next scr refresh
            Someone.setAutoDraw(True)
        
        # *disagreeStrongly* updates
        if disagreeStrongly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disagreeStrongly.frameNStart = frameN  # exact frame index
            disagreeStrongly.tStart = t  # local t and not account for scr refresh
            disagreeStrongly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disagreeStrongly, 'tStartRefresh')  # time at next scr refresh
            disagreeStrongly.setAutoDraw(True)
        
        # *disagreeALittle* updates
        if disagreeALittle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disagreeALittle.frameNStart = frameN  # exact frame index
            disagreeALittle.tStart = t  # local t and not account for scr refresh
            disagreeALittle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disagreeALittle, 'tStartRefresh')  # time at next scr refresh
            disagreeALittle.setAutoDraw(True)
        
        # *Neutral* updates
        if Neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Neutral.frameNStart = frameN  # exact frame index
            Neutral.tStart = t  # local t and not account for scr refresh
            Neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Neutral, 'tStartRefresh')  # time at next scr refresh
            Neutral.setAutoDraw(True)
        
        # *AgreeALittle* updates
        if AgreeALittle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AgreeALittle.frameNStart = frameN  # exact frame index
            AgreeALittle.tStart = t  # local t and not account for scr refresh
            AgreeALittle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AgreeALittle, 'tStartRefresh')  # time at next scr refresh
            AgreeALittle.setAutoDraw(True)
        
        # *AgreeStrongly* updates
        if AgreeStrongly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AgreeStrongly.frameNStart = frameN  # exact frame index
            AgreeStrongly.tStart = t  # local t and not account for scr refresh
            AgreeStrongly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AgreeStrongly, 'tStartRefresh')  # time at next scr refresh
            AgreeStrongly.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in big5Screen_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "big5Screen_2"-------
    for thisComponent in big5Screen_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('rating_5.response', rating_5.getRating())
    trials_5.addData('rating_5.rt', rating_5.getRT())
    trials_5.addData('rating_5.started', rating_5.tStart)
    trials_5.addData('rating_5.stopped', rating_5.tStop)
    trials_5.addData('characText.started', characText.tStartRefresh)
    trials_5.addData('characText.stopped', characText.tStopRefresh)
    trials_5.addData('Someone.started', Someone.tStartRefresh)
    trials_5.addData('Someone.stopped', Someone.tStopRefresh)
    trials_5.addData('disagreeStrongly.started', disagreeStrongly.tStartRefresh)
    trials_5.addData('disagreeStrongly.stopped', disagreeStrongly.tStopRefresh)
    trials_5.addData('disagreeALittle.started', disagreeALittle.tStartRefresh)
    trials_5.addData('disagreeALittle.stopped', disagreeALittle.tStopRefresh)
    trials_5.addData('Neutral.started', Neutral.tStartRefresh)
    trials_5.addData('Neutral.stopped', Neutral.tStopRefresh)
    trials_5.addData('AgreeALittle.started', AgreeALittle.tStartRefresh)
    trials_5.addData('AgreeALittle.stopped', AgreeALittle.tStopRefresh)
    trials_5.addData('AgreeStrongly.started', AgreeStrongly.tStartRefresh)
    trials_5.addData('AgreeStrongly.stopped', AgreeStrongly.tStopRefresh)
    # the Routine "big5Screen_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_5'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
