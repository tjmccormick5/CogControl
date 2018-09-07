#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on Mon May 21 13:43:20 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'withDan'  # from the Builder filename that created this script
expInfo = {u'group': u'', u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/TimothyMcCormick/Desktop/SPR/Selfpaced reading/Dissertation.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Flanker_Instructions"
Flanker_InstructionsClock = core.Clock()
FlankerInstructions = visual.TextStim(win=win, name='FlankerInstructions',
    text=u"Full flanker instructions\n\nPress 'space' to continue.\n",
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Flanker_Instructions2"
Flanker_Instructions2Clock = core.Clock()
flankerInstructions2 = visual.TextStim(win=win, name='flankerInstructions2',
    text=u"Remember\n\nYou'll repeat if you don't get at least 75% correct\n\nPress 'space' when you're ready to continue",
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text=u'+',
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "PracticeFlanker"
PracticeFlankerClock = core.Clock()
practiceFlanker = visual.ImageStim(
    win=win, name='practiceFlanker',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "SPR_Instructions"
SPR_InstructionsClock = core.Clock()
SPRInstructions = visual.TextStim(win=win, name='SPRInstructions',
    text=u"Full Instructions for SPR\n\nPress 'space' to continue.\n\n",
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "SPR_Instructions2"
SPR_Instructions2Clock = core.Clock()
SPRinstructions2 = visual.TextStim(win=win, name='SPRinstructions2',
    text=u"Remember that you need to respond to the questions \nat least 75% correct to continue \n\nPress 'space' when you're ready to continue",
    font=u'courier',
    pos=(0, 0), height=.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "PracticeSentences"
PracticeSentencesClock = core.Clock()
practiceSentences = visual.TextStim(win=win, name='practiceSentences',
    text=u'This should not appear',
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
# now define a function which we can use here and later on to replace letters with '-': 

def replaceWithdash(textList, currentWordNumber): 
    
    dashSentence = '' 
    for index, word in enumerate(textList): # cycle through the words and their index numbers 
        if index != currentWordNumber: 
            dashSentence = dashSentence + ' ' + '-' * len(word)# add a string of dash characters 
        else:
            dashSentence = dashSentence + ' ' + word #for current word, but space was appearing between period and final word, so put space before each word rather than after
    return dashSentence +'.' # yields the manipulated sentence 

# Creating our own clock to time how reaction times
# based on screen flips (i.e. when the word was actually
# shown
wordClock = core.Clock()

# Initialize components for Routine "practiceSentenceCompQ"
practiceSentenceCompQClock = core.Clock()
practiceCompQ = visual.TextStim(win=win, name='practiceCompQ',
    text='default text',
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
practiceCompRespLeft = visual.TextStim(win=win, name='practiceCompRespLeft',
    text='default text',
    font=u'courier',
    pos=(-.5, -.5), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0);
practiceCompRespRight = visual.TextStim(win=win, name='practiceCompRespRight',
    text='default text',
    font=u'courier',
    pos=(.5, -.5), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "setupExp"
setupExpClock = core.Clock()
group = expInfo["group"]

# A dictionary, where the key is a block name,
# and the value is the name of the spreadsheet
# containing the trials for that block
condFiles = {
    "A": "A.csv",
    "B": "B.csv",
    }

# Key is group (a string "1", "2", etc.)
# Value is a list containing the blocks in the desired
#   order for the group. 
blockSequences = {
    "1": ["A", "B"], # Group 1 will see A first, then B.
    "2": ["B", "A"],
    }

# Make sure "group" entered in the gui dialog is one that
# we want
assert group in blockSequences, "Invalid group entered"

# Set the block sequence for this participant's group.
blockSeq = blockSequences[group]

# Initialize components for Routine "Combined_Instructions"
Combined_InstructionsClock = core.Clock()
Instructions_Combined = visual.TextStim(win=win, name='Instructions_Combined',
    text=u"Now you'll do both SPR and flanker\n\nPress 'space' to continue.",
    font=u'Courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "pickBlock"
pickBlockClock = core.Clock()


# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text=u'+',
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "flanker"
flankerClock = core.Clock()
imageStim = visual.ImageStim(
    win=win, name='imageStim',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text=u'+',
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sentences = visual.TextStim(win=win, name='sentences',
    text=u'This should not appear',
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
# now define a function which we can use here and later on to replace letters with '-': 

def replaceWithdash(textList, currentWordNumber): 
    
    dashSentence = '' 
    for index, word in enumerate(textList): # cycle through the words and their index numbers 
        if index != currentWordNumber: 
            dashSentence = dashSentence + ' ' + '-' * len(word)# add a string of dash characters 
        else:
            dashSentence = dashSentence + ' ' + word #for current word, but space was appearing between period and final word, so put space before each word rather than after
    return dashSentence +'.' # yields the manipulated sentence 

# Creating our own clock to time how reaction times
# based on screen flips (i.e. when the word was actually
# shown
wordClock = core.Clock()

# Initialize components for Routine "CompQ"
CompQClock = core.Clock()
questTS = visual.TextStim(win=win, name='questTS',
    text='default text',
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
respLeftTS = visual.TextStim(win=win, name='respLeftTS',
    text='default text',
    font='courier',
    pos=(-0.5, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
respRightTS = visual.TextStim(win=win, name='respRightTS',
    text='default text',
    font='courier',
    pos=(0.5, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "rest"
restClock = core.Clock()
restBetweenBlocks = visual.TextStim(win=win, name='restBetweenBlocks',
    text=u"Rest, muthafucka!\n\nPress 'space' when you're ready to continue",
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
    text=u'Goodbye',
    font=u'courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Flanker_Instructions"-------
t = 0
Flanker_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
FlankerInstructions_keyresponse = event.BuilderKeyResponse()
# keep track of which components have finished
Flanker_InstructionsComponents = [FlankerInstructions, FlankerInstructions_keyresponse]
for thisComponent in Flanker_InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Flanker_Instructions"-------
while continueRoutine:
    # get current time
    t = Flanker_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FlankerInstructions* updates
    if t >= 0.0 and FlankerInstructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        FlankerInstructions.tStart = t
        FlankerInstructions.frameNStart = frameN  # exact frame index
        FlankerInstructions.setAutoDraw(True)
    
    # *FlankerInstructions_keyresponse* updates
    if t >= 0.0 and FlankerInstructions_keyresponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        FlankerInstructions_keyresponse.tStart = t
        FlankerInstructions_keyresponse.frameNStart = frameN  # exact frame index
        FlankerInstructions_keyresponse.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(FlankerInstructions_keyresponse.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if FlankerInstructions_keyresponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            FlankerInstructions_keyresponse.keys = theseKeys[-1]  # just the last key pressed
            FlankerInstructions_keyresponse.rt = FlankerInstructions_keyresponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Flanker_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Flanker_Instructions"-------
for thisComponent in Flanker_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if FlankerInstructions_keyresponse.keys in ['', [], None]:  # No response was made
    FlankerInstructions_keyresponse.keys=None
thisExp.addData('FlankerInstructions_keyresponse.keys',FlankerInstructions_keyresponse.keys)
if FlankerInstructions_keyresponse.keys != None:  # we had a response
    thisExp.addData('FlankerInstructions_keyresponse.rt', FlankerInstructions_keyresponse.rt)
thisExp.nextEntry()
# the Routine "Flanker_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RepeatFlankerIfNeeded = data.TrialHandler(nReps=999, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='RepeatFlankerIfNeeded')
thisExp.addLoop(RepeatFlankerIfNeeded)  # add the loop to the experiment
thisRepeatFlankerIfNeeded = RepeatFlankerIfNeeded.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeatFlankerIfNeeded.rgb)
if thisRepeatFlankerIfNeeded != None:
    for paramName in thisRepeatFlankerIfNeeded:
        exec('{} = thisRepeatFlankerIfNeeded[paramName]'.format(paramName))

for thisRepeatFlankerIfNeeded in RepeatFlankerIfNeeded:
    currentLoop = RepeatFlankerIfNeeded
    # abbreviate parameter names if possible (e.g. rgb = thisRepeatFlankerIfNeeded.rgb)
    if thisRepeatFlankerIfNeeded != None:
        for paramName in thisRepeatFlankerIfNeeded:
            exec('{} = thisRepeatFlankerIfNeeded[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Flanker_Instructions2"-------
    t = 0
    Flanker_Instructions2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    FlankerInstructions2_keyresponse = event.BuilderKeyResponse()
    # keep track of which components have finished
    Flanker_Instructions2Components = [flankerInstructions2, FlankerInstructions2_keyresponse]
    for thisComponent in Flanker_Instructions2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Flanker_Instructions2"-------
    while continueRoutine:
        # get current time
        t = Flanker_Instructions2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *flankerInstructions2* updates
        if t >= 0.0 and flankerInstructions2.status == NOT_STARTED:
            # keep track of start time/frame for later
            flankerInstructions2.tStart = t
            flankerInstructions2.frameNStart = frameN  # exact frame index
            flankerInstructions2.setAutoDraw(True)
        
        # *FlankerInstructions2_keyresponse* updates
        if t >= 0.0 and FlankerInstructions2_keyresponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            FlankerInstructions2_keyresponse.tStart = t
            FlankerInstructions2_keyresponse.frameNStart = frameN  # exact frame index
            FlankerInstructions2_keyresponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(FlankerInstructions2_keyresponse.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if FlankerInstructions2_keyresponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                FlankerInstructions2_keyresponse.keys = theseKeys[-1]  # just the last key pressed
                FlankerInstructions2_keyresponse.rt = FlankerInstructions2_keyresponse.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Flanker_Instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Flanker_Instructions2"-------
    for thisComponent in Flanker_Instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if FlankerInstructions2_keyresponse.keys in ['', [], None]:  # No response was made
        FlankerInstructions2_keyresponse.keys=None
    RepeatFlankerIfNeeded.addData('FlankerInstructions2_keyresponse.keys',FlankerInstructions2_keyresponse.keys)
    if FlankerInstructions2_keyresponse.keys != None:  # we had a response
        RepeatFlankerIfNeeded.addData('FlankerInstructions2_keyresponse.rt', FlankerInstructions2_keyresponse.rt)
    # the Routine "Flanker_Instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceFlankerLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'Practice.csv'),
        seed=None, name='practiceFlankerLoop')
    thisExp.addLoop(practiceFlankerLoop)  # add the loop to the experiment
    thisPracticeFlankerLoop = practiceFlankerLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeFlankerLoop.rgb)
    if thisPracticeFlankerLoop != None:
        for paramName in thisPracticeFlankerLoop:
            exec('{} = thisPracticeFlankerLoop[paramName]'.format(paramName))
    
    for thisPracticeFlankerLoop in practiceFlankerLoop:
        currentLoop = practiceFlankerLoop
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeFlankerLoop.rgb)
        if thisPracticeFlankerLoop != None:
            for paramName in thisPracticeFlankerLoop:
                exec('{} = thisPracticeFlankerLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixation_cross]
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            if t >= 0.0 and fixation_cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cross.tStart = t
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cross.status == STARTED and t >= frameRemains:
                fixation_cross.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "PracticeFlanker"-------
        t = 0
        PracticeFlankerClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        practiceFlanker.setImage(practiceimage)
        PracticeFlankerResponse = event.BuilderKeyResponse()
        ''' reset the counter at the beginning of each practice loop:'''
        if practiceFlankerLoop.thisN == 0:
            number_correct = 0
        # keep track of which components have finished
        PracticeFlankerComponents = [practiceFlanker, PracticeFlankerResponse]
        for thisComponent in PracticeFlankerComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "PracticeFlanker"-------
        while continueRoutine:
            # get current time
            t = PracticeFlankerClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practiceFlanker* updates
            if t >= 0.0 and practiceFlanker.status == NOT_STARTED:
                # keep track of start time/frame for later
                practiceFlanker.tStart = t
                practiceFlanker.frameNStart = frameN  # exact frame index
                practiceFlanker.setAutoDraw(True)
            
            # *PracticeFlankerResponse* updates
            if t >= 0.0 and PracticeFlankerResponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                PracticeFlankerResponse.tStart = t
                PracticeFlankerResponse.frameNStart = frameN  # exact frame index
                PracticeFlankerResponse.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(PracticeFlankerResponse.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if PracticeFlankerResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    PracticeFlankerResponse.keys = theseKeys[-1]  # just the last key pressed
                    PracticeFlankerResponse.rt = PracticeFlankerResponse.clock.getTime()
                    # was this 'correct'?
                    if (PracticeFlankerResponse.keys == str(PracticeimageCorrAns)) or (PracticeFlankerResponse.keys == PracticeimageCorrAns):
                        PracticeFlankerResponse.corr = 1
                    else:
                        PracticeFlankerResponse.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeFlankerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeFlanker"-------
        for thisComponent in PracticeFlankerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if PracticeFlankerResponse.keys in ['', [], None]:  # No response was made
            PracticeFlankerResponse.keys=None
            # was no response the correct answer?!
            if str(PracticeimageCorrAns).lower() == 'none':
               PracticeFlankerResponse.corr = 1  # correct non-response
            else:
               PracticeFlankerResponse.corr = 0  # failed to respond (incorrectly)
        # store data for practiceFlankerLoop (TrialHandler)
        practiceFlankerLoop.addData('PracticeFlankerResponse.keys',PracticeFlankerResponse.keys)
        practiceFlankerLoop.addData('PracticeFlankerResponse.corr', PracticeFlankerResponse.corr)
        if PracticeFlankerResponse.keys != None:  # we had a response
            practiceFlankerLoop.addData('PracticeFlankerResponse.rt', PracticeFlankerResponse.rt)
        ''' update the number correct:'''
        if PracticeFlankerResponse.corr:
            number_correct = number_correct + 1
        
        ''' if this is the final repetition, check the proportion correct.
            (am avoiding hard coding the value '12' for flexibility):'''
        if practiceFlankerLoop.thisN +1 == practiceFlankerLoop.nTotal:
            if number_correct/(practiceFlankerLoop.nTotal + 1) >= 0.75:
                ''' terminate the outer loop so no more practice happens:'''
                RepeatFlankerIfNeeded.finished = True
        
        
        # the Routine "PracticeFlanker" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'practiceFlankerLoop'
    
    thisExp.nextEntry()
    
# completed 999 repeats of 'RepeatFlankerIfNeeded'


# ------Prepare to start Routine "SPR_Instructions"-------
t = 0
SPR_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
SPRInstructions_keyresponse = event.BuilderKeyResponse()
# keep track of which components have finished
SPR_InstructionsComponents = [SPRInstructions, SPRInstructions_keyresponse]
for thisComponent in SPR_InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "SPR_Instructions"-------
while continueRoutine:
    # get current time
    t = SPR_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SPRInstructions* updates
    if t >= 0.0 and SPRInstructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        SPRInstructions.tStart = t
        SPRInstructions.frameNStart = frameN  # exact frame index
        SPRInstructions.setAutoDraw(True)
    
    # *SPRInstructions_keyresponse* updates
    if t >= 0.0 and SPRInstructions_keyresponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        SPRInstructions_keyresponse.tStart = t
        SPRInstructions_keyresponse.frameNStart = frameN  # exact frame index
        SPRInstructions_keyresponse.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(SPRInstructions_keyresponse.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if SPRInstructions_keyresponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            SPRInstructions_keyresponse.keys = theseKeys[-1]  # just the last key pressed
            SPRInstructions_keyresponse.rt = SPRInstructions_keyresponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SPR_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SPR_Instructions"-------
for thisComponent in SPR_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if SPRInstructions_keyresponse.keys in ['', [], None]:  # No response was made
    SPRInstructions_keyresponse.keys=None
thisExp.addData('SPRInstructions_keyresponse.keys',SPRInstructions_keyresponse.keys)
if SPRInstructions_keyresponse.keys != None:  # we had a response
    thisExp.addData('SPRInstructions_keyresponse.rt', SPRInstructions_keyresponse.rt)
thisExp.nextEntry()
# the Routine "SPR_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
RepeatPracticeSentencesIfNeeded = data.TrialHandler(nReps=999, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='RepeatPracticeSentencesIfNeeded')
thisExp.addLoop(RepeatPracticeSentencesIfNeeded)  # add the loop to the experiment
thisRepeatPracticeSentencesIfNeeded = RepeatPracticeSentencesIfNeeded.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeatPracticeSentencesIfNeeded.rgb)
if thisRepeatPracticeSentencesIfNeeded != None:
    for paramName in thisRepeatPracticeSentencesIfNeeded:
        exec('{} = thisRepeatPracticeSentencesIfNeeded[paramName]'.format(paramName))

for thisRepeatPracticeSentencesIfNeeded in RepeatPracticeSentencesIfNeeded:
    currentLoop = RepeatPracticeSentencesIfNeeded
    # abbreviate parameter names if possible (e.g. rgb = thisRepeatPracticeSentencesIfNeeded.rgb)
    if thisRepeatPracticeSentencesIfNeeded != None:
        for paramName in thisRepeatPracticeSentencesIfNeeded:
            exec('{} = thisRepeatPracticeSentencesIfNeeded[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "SPR_Instructions2"-------
    t = 0
    SPR_Instructions2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    SPRinstructions2_keyresponse = event.BuilderKeyResponse()
    # keep track of which components have finished
    SPR_Instructions2Components = [SPRinstructions2, SPRinstructions2_keyresponse]
    for thisComponent in SPR_Instructions2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "SPR_Instructions2"-------
    while continueRoutine:
        # get current time
        t = SPR_Instructions2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SPRinstructions2* updates
        if t >= 0.0 and SPRinstructions2.status == NOT_STARTED:
            # keep track of start time/frame for later
            SPRinstructions2.tStart = t
            SPRinstructions2.frameNStart = frameN  # exact frame index
            SPRinstructions2.setAutoDraw(True)
        
        # *SPRinstructions2_keyresponse* updates
        if t >= 0.0 and SPRinstructions2_keyresponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            SPRinstructions2_keyresponse.tStart = t
            SPRinstructions2_keyresponse.frameNStart = frameN  # exact frame index
            SPRinstructions2_keyresponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(SPRinstructions2_keyresponse.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if SPRinstructions2_keyresponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                SPRinstructions2_keyresponse.keys = theseKeys[-1]  # just the last key pressed
                SPRinstructions2_keyresponse.rt = SPRinstructions2_keyresponse.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SPR_Instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SPR_Instructions2"-------
    for thisComponent in SPR_Instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if SPRinstructions2_keyresponse.keys in ['', [], None]:  # No response was made
        SPRinstructions2_keyresponse.keys=None
    RepeatPracticeSentencesIfNeeded.addData('SPRinstructions2_keyresponse.keys',SPRinstructions2_keyresponse.keys)
    if SPRinstructions2_keyresponse.keys != None:  # we had a response
        RepeatPracticeSentencesIfNeeded.addData('SPRinstructions2_keyresponse.rt', SPRinstructions2_keyresponse.rt)
    # the Routine "SPR_Instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceSentenceLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'Practice.csv'),
        seed=None, name='practiceSentenceLoop')
    thisExp.addLoop(practiceSentenceLoop)  # add the loop to the experiment
    thisPracticeSentenceLoop = practiceSentenceLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeSentenceLoop.rgb)
    if thisPracticeSentenceLoop != None:
        for paramName in thisPracticeSentenceLoop:
            exec('{} = thisPracticeSentenceLoop[paramName]'.format(paramName))
    
    for thisPracticeSentenceLoop in practiceSentenceLoop:
        currentLoop = practiceSentenceLoop
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeSentenceLoop.rgb)
        if thisPracticeSentenceLoop != None:
            for paramName in thisPracticeSentenceLoop:
                exec('{} = thisPracticeSentenceLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "PracticeSentences"-------
        t = 0
        PracticeSentencesClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # remove any keypresses remaining in the buffer from 
        # before  this routine started:
        event.clearEvents() 
        practiceSentenceList = practiceSentence.split() 
        # this breaks your sentence's single string of characters into a list of individual 
        # words, e.g. 'The quick brown fox.' becomes ['The', 'quick', 'brown', 'fox.'] 
        
        # keep track of which word we are up to: 
        wordNumber = -1 # -1 as we haven't started yet 
        
        # now at the very beginning of the trial, we need to run this function for the 
        # first time. As the current word number is -1, it should make all words '-'. 
        # Use the actual name of your Builder text component here: 
        
        practiceSentences.text = replaceWithdash(practiceSentenceList, wordNumber) 
        
        # DAN: reset our wordClock (it gets set to 0)
        wordClock.reset()
        
        # In the Builder interface, specify a "constant" value for the text content, e.g. 
        # 'test', so it doesn't conflict with our code. 
        
        # keep track of which components have finished
        PracticeSentencesComponents = [practiceSentences]
        for thisComponent in PracticeSentencesComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "PracticeSentences"-------
        while continueRoutine:
            # get current time
            t = PracticeSentencesClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practiceSentences* updates
            if t >= 0.0 and practiceSentences.status == NOT_STARTED:
                # keep track of start time/frame for later
                practiceSentences.tStart = t
                practiceSentences.frameNStart = frameN  # exact frame index
                practiceSentences.setAutoDraw(True)
            keypresses = event.getKeys() # returns a list of keypresses 
            
            if len(keypresses) > 0: # at least one key was pushed 
            
                if 'space' in keypresses: 
                    
                    thisResponseTime = t # the current time in the trial 
            
                    # DAN: Also saving the time based on our wordClock,
                    # which is reset when the next word is actually shown
                    rtFromFlip = wordClock.getTime()
                    # Tell psychopy to call the wordClock's reset() method
                    # the next time the window flips:
                    win.callOnFlip(wordClock.reset)
            
                    wordNumber = wordNumber + 1 
                    if wordNumber < len(practiceSentenceList): 
            
                        if wordNumber == 0: # need to initialise a variable: 
                            timeOfLastResponse = 0 
            
                        # save the inter response interval for this keypress, 
                        # in variables called IRI_0, IRI_1, etc: 
                        thisExp.addData('IRI_' + str(wordNumber), thisResponseTime - timeOfLastResponse) 
                        timeOfLastResponse = thisResponseTime 
            
                        # Saving our flip-based rt
                        thisExp.addData("IRI_FL_" + str(wordNumber), rtFromFlip)
            
                        # Also, since you asked, we'll save the time
                        # since the trial started. (i.e. if the 'space' is hit
                        # at second 1 and 2:
                        #   IRI_1 = 1 
                        #   IRI_2 = 1
                        #   space_1 = 1
                        #   space_2 = 2
                        thisExp.addData("space_" + str(wordNumber), thisResponseTime) 
            
                        # update the text by masking all but the current word 
                        practiceSentences.text = replaceWithdash(practiceSentenceList, wordNumber) 
                    else: 
                        continueRoutine = False # time to go on to the next trial 
            
                elif 'escape' in keypresses: 
            
                    core.quit() # I think you'll need to handle quitting manually now. 
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeSentencesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeSentences"-------
        for thisComponent in PracticeSentencesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "PracticeSentences" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "practiceSentenceCompQ"-------
        t = 0
        practiceSentenceCompQClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        practiceCompQ.setText(practiceSentenceCompQ)
        practiceCompRespLeft.setText(compRespL)
        practiceCompRespRight.setText(compRespR)
        key_resp_practiceCompQ = event.BuilderKeyResponse()
        ''' reset the counter at the beginning of each practice loop:'''
        if practiceSentenceLoop.thisN == 0:
            number_correct = 0
        # keep track of which components have finished
        practiceSentenceCompQComponents = [practiceCompQ, practiceCompRespLeft, practiceCompRespRight, key_resp_practiceCompQ]
        for thisComponent in practiceSentenceCompQComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practiceSentenceCompQ"-------
        while continueRoutine:
            # get current time
            t = practiceSentenceCompQClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practiceCompQ* updates
            if t >= 0.0 and practiceCompQ.status == NOT_STARTED:
                # keep track of start time/frame for later
                practiceCompQ.tStart = t
                practiceCompQ.frameNStart = frameN  # exact frame index
                practiceCompQ.setAutoDraw(True)
            
            # *practiceCompRespLeft* updates
            if t >= 0.0 and practiceCompRespLeft.status == NOT_STARTED:
                # keep track of start time/frame for later
                practiceCompRespLeft.tStart = t
                practiceCompRespLeft.frameNStart = frameN  # exact frame index
                practiceCompRespLeft.setAutoDraw(True)
            
            # *practiceCompRespRight* updates
            if t >= 0.0 and practiceCompRespRight.status == NOT_STARTED:
                # keep track of start time/frame for later
                practiceCompRespRight.tStart = t
                practiceCompRespRight.frameNStart = frameN  # exact frame index
                practiceCompRespRight.setAutoDraw(True)
            
            # *key_resp_practiceCompQ* updates
            if t >= 0.0 and key_resp_practiceCompQ.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_practiceCompQ.tStart = t
                key_resp_practiceCompQ.frameNStart = frameN  # exact frame index
                key_resp_practiceCompQ.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_practiceCompQ.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_practiceCompQ.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_practiceCompQ.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_practiceCompQ.rt = key_resp_practiceCompQ.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_practiceCompQ.keys == str(compRespCorr)) or (key_resp_practiceCompQ.keys == compRespCorr):
                        key_resp_practiceCompQ.corr = 1
                    else:
                        key_resp_practiceCompQ.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceSentenceCompQComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practiceSentenceCompQ"-------
        for thisComponent in practiceSentenceCompQComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_practiceCompQ.keys in ['', [], None]:  # No response was made
            key_resp_practiceCompQ.keys=None
            # was no response the correct answer?!
            if str(compRespCorr).lower() == 'none':
               key_resp_practiceCompQ.corr = 1  # correct non-response
            else:
               key_resp_practiceCompQ.corr = 0  # failed to respond (incorrectly)
        # store data for practiceSentenceLoop (TrialHandler)
        practiceSentenceLoop.addData('key_resp_practiceCompQ.keys',key_resp_practiceCompQ.keys)
        practiceSentenceLoop.addData('key_resp_practiceCompQ.corr', key_resp_practiceCompQ.corr)
        if key_resp_practiceCompQ.keys != None:  # we had a response
            practiceSentenceLoop.addData('key_resp_practiceCompQ.rt', key_resp_practiceCompQ.rt)
        ''' update the number correct:'''
        if key_resp_practiceCompQ.corr:
            number_correct = number_correct + 1
        
        ''' if this is the final repetition, check the proportion correct.
            (am avoiding hard coding the value '12' for flexibility):'''
        if practiceSentenceLoop.thisN + 1 == practiceSentenceLoop.nTotal:
            if number_correct/(practiceSentenceLoop.nTotal + 1) >= 0.75:
                ''' terminate the outer loop so no more practice happens:'''
                RepeatPracticeSentencesIfNeeded.finished = True
        
        # the Routine "practiceSentenceCompQ" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'practiceSentenceLoop'
    
    thisExp.nextEntry()
    
# completed 999 repeats of 'RepeatPracticeSentencesIfNeeded'


# ------Prepare to start Routine "setupExp"-------
t = 0
setupExpClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
setupExpComponents = []
for thisComponent in setupExpComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "setupExp"-------
while continueRoutine:
    # get current time
    t = setupExpClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setupExp"-------
for thisComponent in setupExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "setupExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Combined_Instructions"-------
t = 0
Combined_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
combinedInstructions_keyresponse = event.BuilderKeyResponse()
# keep track of which components have finished
Combined_InstructionsComponents = [Instructions_Combined, combinedInstructions_keyresponse]
for thisComponent in Combined_InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Combined_Instructions"-------
while continueRoutine:
    # get current time
    t = Combined_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_Combined* updates
    if t >= 0.0 and Instructions_Combined.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions_Combined.tStart = t
        Instructions_Combined.frameNStart = frameN  # exact frame index
        Instructions_Combined.setAutoDraw(True)
    
    # *combinedInstructions_keyresponse* updates
    if t >= 0.0 and combinedInstructions_keyresponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        combinedInstructions_keyresponse.tStart = t
        combinedInstructions_keyresponse.frameNStart = frameN  # exact frame index
        combinedInstructions_keyresponse.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(combinedInstructions_keyresponse.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if combinedInstructions_keyresponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            combinedInstructions_keyresponse.keys = theseKeys[-1]  # just the last key pressed
            combinedInstructions_keyresponse.rt = combinedInstructions_keyresponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Combined_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Combined_Instructions"-------
for thisComponent in Combined_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if combinedInstructions_keyresponse.keys in ['', [], None]:  # No response was made
    combinedInstructions_keyresponse.keys=None
thisExp.addData('combinedInstructions_keyresponse.keys',combinedInstructions_keyresponse.keys)
if combinedInstructions_keyresponse.keys != None:  # we had a response
    thisExp.addData('combinedInstructions_keyresponse.rt', combinedInstructions_keyresponse.rt)
thisExp.nextEntry()
# the Routine "Combined_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=len(condFiles), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pickBlock"-------
    t = 0
    pickBlockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # If we're on the 0th repetition (in our case meaning the 1st block),
    # get the 0th item in blockSeq list we made earlier.
    block = blockSeq[blocks.thisRepN]
    
    # Get the conditions file for that block
    condFile = condFiles[block]
    # keep track of which components have finished
    pickBlockComponents = []
    for thisComponent in pickBlockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pickBlock"-------
    while continueRoutine:
        # get current time
        t = pickBlockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pickBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pickBlock"-------
    for thisComponent in pickBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "pickBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condFile),
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
        
        # ------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixation_cross]
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            if t >= 0.0 and fixation_cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cross.tStart = t
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cross.status == STARTED and t >= frameRemains:
                fixation_cross.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "flanker"-------
        t = 0
        flankerClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        imageStim.setImage(image)
        flankerkeyresponse = event.BuilderKeyResponse()
        # keep track of which components have finished
        flankerComponents = [imageStim, flankerkeyresponse]
        for thisComponent in flankerComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "flanker"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = flankerClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *imageStim* updates
            if t >= 0.0 and imageStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                imageStim.tStart = t
                imageStim.frameNStart = frameN  # exact frame index
                imageStim.setAutoDraw(True)
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if imageStim.status == STARTED and t >= frameRemains:
                imageStim.setAutoDraw(False)
            
            # *flankerkeyresponse* updates
            if t >= 0.0 and flankerkeyresponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                flankerkeyresponse.tStart = t
                flankerkeyresponse.frameNStart = frameN  # exact frame index
                flankerkeyresponse.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(flankerkeyresponse.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if flankerkeyresponse.status == STARTED and t >= frameRemains:
                flankerkeyresponse.status = STOPPED
            if flankerkeyresponse.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    flankerkeyresponse.keys = theseKeys[-1]  # just the last key pressed
                    flankerkeyresponse.rt = flankerkeyresponse.clock.getTime()
                    # was this 'correct'?
                    if (flankerkeyresponse.keys == str(imageCorrAns)) or (flankerkeyresponse.keys == imageCorrAns):
                        flankerkeyresponse.corr = 1
                    else:
                        flankerkeyresponse.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in flankerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "flanker"-------
        for thisComponent in flankerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if flankerkeyresponse.keys in ['', [], None]:  # No response was made
            flankerkeyresponse.keys=None
            # was no response the correct answer?!
            if str(imageCorrAns).lower() == 'none':
               flankerkeyresponse.corr = 1  # correct non-response
            else:
               flankerkeyresponse.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('flankerkeyresponse.keys',flankerkeyresponse.keys)
        trials.addData('flankerkeyresponse.corr', flankerkeyresponse.corr)
        if flankerkeyresponse.keys != None:  # we had a response
            trials.addData('flankerkeyresponse.rt', flankerkeyresponse.rt)
        
        # ------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixation_cross]
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            if t >= 0.0 and fixation_cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cross.tStart = t
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cross.status == STARTED and t >= frameRemains:
                fixation_cross.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # remove any keypresses remaining in the buffer from 
        # before  this routine started:
        event.clearEvents() 
        sentenceList = sentence.split() 
        # this breaks your sentence's single string of characters into a list of individual 
        # words, e.g. 'The quick brown fox.' becomes ['The', 'quick', 'brown', 'fox.'] 
        
        # keep track of which word we are up to: 
        wordNumber = -1 # -1 as we haven't started yet 
        
        # now at the very beginning of the trial, we need to run this function for the 
        # first time. As the current word number is -1, it should make all words '-'. 
        # Use the actual name of your Builder text component here: 
        
        sentences.text = replaceWithdash(sentenceList, wordNumber) 
        
        # DAN: reset our wordClock (it gets set to 0)
        wordClock.reset()
        
        # In the Builder interface, specify a "constant" value for the text content, e.g. 
        # 'test', so it doesn't conflict with our code. 
        
        # keep track of which components have finished
        trialComponents = [sentences]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sentences* updates
            if t >= 0.0 and sentences.status == NOT_STARTED:
                # keep track of start time/frame for later
                sentences.tStart = t
                sentences.frameNStart = frameN  # exact frame index
                sentences.setAutoDraw(True)
            keypresses = event.getKeys() # returns a list of keypresses 
            
            if len(keypresses) > 0: # at least one key was pushed 
            
                if 'space' in keypresses: 
                    
                    thisResponseTime = t # the current time in the trial 
            
                    # DAN: Also saving the time based on our wordClock,
                    # which is reset when the next word is actually shown
                    rtFromFlip = wordClock.getTime()
                    # Tell psychopy to call the wordClock's reset() method
                    # the next time the window flips:
                    win.callOnFlip(wordClock.reset)
            
                    wordNumber = wordNumber + 1 
                    if wordNumber < len(sentenceList): 
            
                        if wordNumber == 0: # need to initialise a variable: 
                            timeOfLastResponse = 0 
            
                        # save the inter response interval for this keypress, 
                        # in variables called IRI_0, IRI_1, etc: 
                        thisExp.addData('IRI_' + str(wordNumber), thisResponseTime - timeOfLastResponse) 
                        timeOfLastResponse = thisResponseTime 
            
                        # Saving our flip-based rt
                        thisExp.addData("IRI_FL_" + str(wordNumber), rtFromFlip)
            
                        # Also, since you asked, we'll save the time
                        # since the trial started. (i.e. if the 'space' is hit
                        # at second 1 and 2:
                        #   IRI_1 = 1 
                        #   IRI_2 = 1
                        #   space_1 = 1
                        #   space_2 = 2
                        thisExp.addData("space_" + str(wordNumber), thisResponseTime) 
            
                        # update the text by masking all but the current word 
                        sentences.text = replaceWithdash(sentenceList, wordNumber) 
                    else: 
                        continueRoutine = False # time to go on to the next trial 
            
                elif 'escape' in keypresses: 
            
                    core.quit() # I think you'll need to handle quitting manually now. 
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "CompQ"-------
        t = 0
        CompQClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        questTS.setText(compQ)
        respLeftTS.setText(compRespL)
        respRightTS.setText(compRespR)
        CompQkeyresponse = event.BuilderKeyResponse()
        # keep track of which components have finished
        CompQComponents = [questTS, respLeftTS, respRightTS, CompQkeyresponse]
        for thisComponent in CompQComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "CompQ"-------
        while continueRoutine:
            # get current time
            t = CompQClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *questTS* updates
            if t >= 0.0 and questTS.status == NOT_STARTED:
                # keep track of start time/frame for later
                questTS.tStart = t
                questTS.frameNStart = frameN  # exact frame index
                questTS.setAutoDraw(True)
            
            # *respLeftTS* updates
            if t >= 0.0 and respLeftTS.status == NOT_STARTED:
                # keep track of start time/frame for later
                respLeftTS.tStart = t
                respLeftTS.frameNStart = frameN  # exact frame index
                respLeftTS.setAutoDraw(True)
            
            # *respRightTS* updates
            if t >= 0.0 and respRightTS.status == NOT_STARTED:
                # keep track of start time/frame for later
                respRightTS.tStart = t
                respRightTS.frameNStart = frameN  # exact frame index
                respRightTS.setAutoDraw(True)
            
            # *CompQkeyresponse* updates
            if t >= 0.0 and CompQkeyresponse.status == NOT_STARTED:
                # keep track of start time/frame for later
                CompQkeyresponse.tStart = t
                CompQkeyresponse.frameNStart = frameN  # exact frame index
                CompQkeyresponse.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(CompQkeyresponse.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if CompQkeyresponse.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    CompQkeyresponse.keys = theseKeys[-1]  # just the last key pressed
                    CompQkeyresponse.rt = CompQkeyresponse.clock.getTime()
                    # was this 'correct'?
                    if (CompQkeyresponse.keys == str(compRespCorr)) or (CompQkeyresponse.keys == compRespCorr):
                        CompQkeyresponse.corr = 1
                    else:
                        CompQkeyresponse.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CompQComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CompQ"-------
        for thisComponent in CompQComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if CompQkeyresponse.keys in ['', [], None]:  # No response was made
            CompQkeyresponse.keys=None
            # was no response the correct answer?!
            if str(compRespCorr).lower() == 'none':
               CompQkeyresponse.corr = 1  # correct non-response
            else:
               CompQkeyresponse.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('CompQkeyresponse.keys',CompQkeyresponse.keys)
        trials.addData('CompQkeyresponse.corr', CompQkeyresponse.corr)
        if CompQkeyresponse.keys != None:  # we had a response
            trials.addData('CompQkeyresponse.rt', CompQkeyresponse.rt)
        # the Routine "CompQ" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "rest"-------
    t = 0
    restClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rest_keyresponse = event.BuilderKeyResponse()
    if blocks.thisN + 1 == blocks.nTotal:
        continueRoutine = False
    # keep track of which components have finished
    restComponents = [restBetweenBlocks, rest_keyresponse]
    for thisComponent in restComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *restBetweenBlocks* updates
        if t >= 0.0 and restBetweenBlocks.status == NOT_STARTED:
            # keep track of start time/frame for later
            restBetweenBlocks.tStart = t
            restBetweenBlocks.frameNStart = frameN  # exact frame index
            restBetweenBlocks.setAutoDraw(True)
        
        # *rest_keyresponse* updates
        if t >= 0.0 and rest_keyresponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            rest_keyresponse.tStart = t
            rest_keyresponse.frameNStart = frameN  # exact frame index
            rest_keyresponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(rest_keyresponse.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if rest_keyresponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                rest_keyresponse.keys = theseKeys[-1]  # just the last key pressed
                rest_keyresponse.rt = rest_keyresponse.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if rest_keyresponse.keys in ['', [], None]:  # No response was made
        rest_keyresponse.keys=None
    blocks.addData('rest_keyresponse.keys',rest_keyresponse.keys)
    if rest_keyresponse.keys != None:  # we had a response
        blocks.addData('rest_keyresponse.rt', rest_keyresponse.rt)
    
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed len(condFiles) repeats of 'blocks'


# ------Prepare to start Routine "Goodbye"-------
t = 0
GoodbyeClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
GoodbyeComponents = [EndText]
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Goodbye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GoodbyeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndText* updates
    if t >= 0.0 and EndText.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndText.tStart = t
        EndText.frameNStart = frameN  # exact frame index
        EndText.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if EndText.status == STARTED and t >= frameRemains:
        EndText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
