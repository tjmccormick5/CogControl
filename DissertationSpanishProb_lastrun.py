#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on Wed Jul 18 21:24:34 2018
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
expName = 'Dissertation'  # from the Builder filename that created this script
expInfo = {u'group': u'', u'session': u'', u'participant': u'', u'level': u''}
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
    originPath=u'/Users/TimothyMcCormick/Desktop/SPR/Selfpaced reading/DissertationSpanishProb.psyexp',
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

# Initialize components for Routine "setupExp"
setupExpClock = core.Clock()
group = expInfo["group"]

# A dictionary, where the key is a block name,
# and the value is the name of the spreadsheet
# containing the trials for that block
condFiles = {
    "A1": "A1.xlsx",
    "B1": "B1.xlsx",
    "A2": "A2.xlsx",
    "B2": "B2.xlsx",
    }

# Key is group (a string "1", "2", etc.)
# Value is a list containing the blocks in the desired
#   order for the group. 
blockSequences = {
    "1": ["A1", "B1"], # Group 1 will see A1 first, then B1.
    "2": ["B1", "A1"],
    "3": ["A2", "B2"],
    "4": ["B2", "A2"],
    }

# Make sure "group" entered in the gui dialog is one that
# we want
assert group in blockSequences, "Invalid group entered"

# Set the block sequence for this participant's group.
blockSeq = blockSequences[group]

# Initialize components for Routine "PreStart"
PreStartClock = core.Clock()
preStartText = visual.TextStim(win=win, name='preStartText',
    text=u"\xa1Genial! \xa1Ya lo tienes!\n\nSi todav\xeda tienes preguntas, hazlas ahora.\nA partir de ahora, queremos evitar las pausas, as\xed que si tienes que usar el ba\xf1o, tomar de tu bebida, etc., por favor hazlo ya.\n\nCuando est\xe9s list@ para iniciar el experimento, pulsa 'espacio'.",
    font='courier',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "pickBlock"
pickBlockClock = core.Clock()


# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
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
    text='+',
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sentences = visual.TextStim(win=win, name='sentences',
    text='This should not appear',
    font='courier',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
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
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
respLeftTS = visual.TextStim(win=win, name='respLeftTS',
    text='default text',
    font='courier',
    pos=(-0.5, -0.5), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
respRightTS = visual.TextStim(win=win, name='respRightTS',
    text='default text',
    font='courier',
    pos=(0.5, -0.5), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "scoreKeeper"
scoreKeeperClock = core.Clock()

RestText = visual.TextStim(win=win, name='RestText',
    text=u'\xa1Cuidado!\n\nEs importante responder r\xe1pido, pero tambi\xe9n es importante que respondas correctamente. \n\nDescansa un momento y cuando contin\xfaes, t\xf3mate tu tiempo.',
    font='courier',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
PressSpaceToContinue = visual.TextStim(win=win, name='PressSpaceToContinue',
    text="Press 'space' to continue.",
    font='courier',
    pos=(0, -0.7), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "midBlockBreak"
midBlockBreakClock = core.Clock()
midBlockBreakText = visual.TextStim(win=win, name='midBlockBreakText',
    text=u'T\xf3mate un momento para descansar. \n',
    font='courier',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
pressSpace = visual.TextStim(win=win, name='pressSpace',
    text="Pulsa 'espacio' para continuar.",
    font='courier',
    pos=(0, -0.7), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "rest"
restClock = core.Clock()
restBetweenBlocks = visual.TextStim(win=win, name='restBetweenBlocks',
    text=u'Descansa!\n\nYa has pasado el punto intermedio.\n\nT\xf3mate un momento para descansar y contin\xfaes cuando est\xe9s list@.',
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

text = visual.TextStim(win=win, name='text',
    text="Pulsa 'espacio' para continuar.",
    font='courier',
    pos=(0, -0.7), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
    text=u'Gracias por completar el estudio.\n\nAntes de que te vayas, el investigador va a pedir que completes un cuestionario sobre tu experiencia ling\xfc\xedstica. \n\nNo dura m\xe1s de 5 minutos.',
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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

# ------Prepare to start Routine "PreStart"-------
t = 0
PreStartClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyResponsePreStart = event.BuilderKeyResponse()
# keep track of which components have finished
PreStartComponents = [preStartText, keyResponsePreStart]
for thisComponent in PreStartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PreStart"-------
while continueRoutine:
    # get current time
    t = PreStartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *preStartText* updates
    if t >= 0.0 and preStartText.status == NOT_STARTED:
        # keep track of start time/frame for later
        preStartText.tStart = t
        preStartText.frameNStart = frameN  # exact frame index
        preStartText.setAutoDraw(True)
    
    # *keyResponsePreStart* updates
    if t >= 0.0 and keyResponsePreStart.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyResponsePreStart.tStart = t
        keyResponsePreStart.frameNStart = frameN  # exact frame index
        keyResponsePreStart.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(keyResponsePreStart.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if keyResponsePreStart.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            keyResponsePreStart.keys = theseKeys[-1]  # just the last key pressed
            keyResponsePreStart.rt = keyResponsePreStart.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreStart"-------
for thisComponent in PreStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyResponsePreStart.keys in ['', [], None]:  # No response was made
    keyResponsePreStart.keys=None
thisExp.addData('keyResponsePreStart.keys',keyResponsePreStart.keys)
if keyResponsePreStart.keys != None:  # we had a response
    thisExp.addData('keyResponsePreStart.rt', keyResponsePreStart.rt)
thisExp.nextEntry()
# the Routine "PreStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=len(blockSeq), method='sequential', 
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
        if criticalSentenceCode > 299:
            continueRoutine = False
        
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
        if criticalSentenceCode > 299:
            continueRoutine = False
        
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
        
        # ------Prepare to start Routine "scoreKeeper"-------
        t = 0
        scoreKeeperClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ''' reset the counter at the beginning of each loop:'''
        if trials.thisN == 0:
            wrongscore = 0
            wrongscoreQuestions = 0
        
        if flankerkeyresponse.corr:
            wrongscore = 0
        else:
            wrongscore = wrongscore + 1
        
        if CompQkeyresponse.corr:
            wrongscoreQuestions = 0
        else:
            wrongscoreQuestions = wrongscoreQuestions + 1
        
        if wrongscore == 3 or wrongscoreQuestions == 5:
            continueRoutine = True
            wrongscore = 0
            wrongscoreQuestions = 0
        else:
            continueRoutine = False
        key_resp_2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        scoreKeeperComponents = [RestText, PressSpaceToContinue, key_resp_2]
        for thisComponent in scoreKeeperComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "scoreKeeper"-------
        while continueRoutine:
            # get current time
            t = scoreKeeperClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *RestText* updates
            if t >= 0.0 and RestText.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestText.tStart = t
                RestText.frameNStart = frameN  # exact frame index
                RestText.setAutoDraw(True)
            
            # *PressSpaceToContinue* updates
            if t >= 10.0 and PressSpaceToContinue.status == NOT_STARTED:
                # keep track of start time/frame for later
                PressSpaceToContinue.tStart = t
                PressSpaceToContinue.frameNStart = frameN  # exact frame index
                PressSpaceToContinue.setAutoDraw(True)
            
            # *key_resp_2* updates
            if t >= 10.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in scoreKeeperComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "scoreKeeper"-------
        for thisComponent in scoreKeeperComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys=None
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "scoreKeeper" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "midBlockBreak"-------
        t = 0
        midBlockBreakClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4 = event.BuilderKeyResponse()
        if trials.thisN == 37:
            continueRoutine = True
        else:
            continueRoutine = False
        # keep track of which components have finished
        midBlockBreakComponents = [midBlockBreakText, key_resp_4, pressSpace]
        for thisComponent in midBlockBreakComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "midBlockBreak"-------
        while continueRoutine:
            # get current time
            t = midBlockBreakClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *midBlockBreakText* updates
            if t >= 0 and midBlockBreakText.status == NOT_STARTED:
                # keep track of start time/frame for later
                midBlockBreakText.tStart = t
                midBlockBreakText.frameNStart = frameN  # exact frame index
                midBlockBreakText.setAutoDraw(True)
            
            # *key_resp_4* updates
            if t >= 7.5 and key_resp_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_4.tStart = t
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_4.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_4.rt = key_resp_4.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *pressSpace* updates
            if t >= 7.5 and pressSpace.status == NOT_STARTED:
                # keep track of start time/frame for later
                pressSpace.tStart = t
                pressSpace.frameNStart = frameN  # exact frame index
                pressSpace.setAutoDraw(True)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in midBlockBreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "midBlockBreak"-------
        for thisComponent in midBlockBreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys=None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
        
        # the Routine "midBlockBreak" was not non-slip safe, so reset the non-slip timer
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
    restComponents = [restBetweenBlocks, rest_keyresponse, text]
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
        if t >= 10.0 and rest_keyresponse.status == NOT_STARTED:
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
        
        
        # *text* updates
        if t >= 10 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
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
# completed len(blockSeq) repeats of 'blocks'


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
