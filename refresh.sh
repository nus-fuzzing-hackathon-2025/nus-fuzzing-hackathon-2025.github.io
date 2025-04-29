#!/bin/bash

rsync -a --delete /home/dylan/git/fuzzing-comp-assignment/report-pdfs .
rsync -a --delete /home/dylan/git/fuzzing-comp-assignment/build-logs .
# rsync -a --delete /home/dylan/git/fuzzing-comp-assignment/summary.csv .
# rsync -a --delete /home/dylan/git/fuzzing-comp-assignment/status.csv .
rsync -a --delete /home/dylan/git/fuzzing-comp-assignment/index.html .

cp build-logs_template.html build-logs.html
cp reports_template.html reports.html

build_logs_path="https://raw.githubusercontent.com/nus-fuzzing-hackathon-2024/nus-fuzzing-hackathon-2024.github.io/main/build-logs/"

report_pdfs_path="https://raw.githubusercontent.com/nus-fuzzing-hackathon-2024/nus-fuzzing-hackathon-2024.github.io/main/report-pdfs/"

for file in build-logs/*; do
  sed -i "s|</tbody>|<tr><td>$(basename $file)</td><td><a class=\"nav-link\" href="${build_logs_path}$(basename $file)">Link to file</a></td></tr></tbody>|g" build-logs.html
done

#for file in report-pdfs/*; do
#  sed -i "s|</tbody>|<tr><td>$(basename $file)</td><td><a class=\"nav-link\" href="${report_pdfs_path}$(basename $file)">Link to file</a></td></tr></tbody>|g" reports.html
#done

## DEPLOY HERE
git add -A
git commit -m "refreshing data"
git push
