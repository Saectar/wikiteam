#set -e 

export PYTHONPATH=$HOME/experiments/wikiteam/
cd ${HOME}/experiments/wikiteam/data
python $HOME/experiments/wikiteam/dumpgenerator.py

echo going to run process
cd ${HOME}/experiments/wikiteam/data
#pwd
python $HOME/experiments/wikiteam/process.py
rm -rf  ${HOME}/experiments/wikiteam/data/enwikipedia*
#rm -rf  ${HOME}/experiments/wikiteam/data/Api*
