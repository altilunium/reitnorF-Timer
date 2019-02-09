# reitnorF-Timer
Simple timer for your casual usage

## Requirement

* Python 2.7
* Pyperclip (pip install pyperclip) 


## Background
I need to track how much time i spent when working on a project (for reporting purposes)

## How it works
This program consist of 2 thread. First thread, listen for keypress. The second thread, counting the time since program started. When specific keypress is detected (q->enter), this thread will tell the second thread to stop. Then , full report will be generated (when started, when finished, duration) and automatically copied to your clipboard. So you can store the report somewhere for reporting purposes

