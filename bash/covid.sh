#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
ICUCURRENT=$(echo $DATA | jq '.[0].inIcuCurrently')
ICUCUM=$(echo $DATA | jq '.[0].inIcuCumulative')
TOTAL=$(($POSTIVE + $NEGATIVE))
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases out of $TOTAL total tests. There are currently $ICUCURRENT people in the ICU and $ICUCUM have been in the ICU due to COVID-19"
