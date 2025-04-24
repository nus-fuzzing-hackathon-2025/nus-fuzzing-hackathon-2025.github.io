#!/bin/bash

rsync -a --delete dylan@afltools.d2.comp.nus.edu.sg:/home/dylan/git/fuzzing-comp-assignment/report-pdfs .
rsync -a --delete dylan@afltools.d2.comp.nus.edu.sg:/home/dylan/git/fuzzing-comp-assignment/build-logs .
# rsync -a --delete dylan@afltools.d2.comp.nus.edu.sg:/home/dylan/git/fuzzing-comp-assignment/summary.csv .
# rsync -a --delete dylan@afltools.d2.comp.nus.edu.sg:/home/dylan/git/fuzzing-comp-assignment/status.csv .
rsync -a --delete dylan@afltools.d2.comp.nus.edu.sg:/home/dylan/git/fuzzing-comp-assignment/index.html .
