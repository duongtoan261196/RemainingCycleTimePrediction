import os
from os.path import dirname
root_path = dirname(dirname(os.path.dirname(os.path.realpath(__file__))))
print(root_path)
import pandas as pd
import datetime, time

data_dir = root_path + '/RemainingCycleTimePrediction/1_Data/'
project_dir = root_path + '/RemainingCycleTimePrediction/'


def decode_prediction(predict_vector, onehot_encoder):
    y_one_hot = 1*(predict_vector >= predict_vector.max()).reshape((1,len(predict_vector)))    
    return onehot_encoder.inverse_transform(y_one_hot)[0]


def Extract_trace_and_temporal_features(tab):
    # Extract trace and compute the 4 timed features for each event
    lastcase = ''
    line = [] # to store all activities of each case
    firstLine = True
    lines = [] # to store activities of all cases
    lines_t = [] # to store all timediff from last event of all cases
    lines_t2 = [] # to store all timediff2 from start case event of all cases
    lines_t3 = [] # to store all timediff3 from midnight of all cases
    lines_t4 = [] # to store all timediff4 day in week of all cases
    times = []  # to store all timediff in a case
    times2 = [] # to store all timediff2 in a case
    times3 = [] # to store all timediff3 in a case
    times4 = [] # to store all timediff4 in a case
    casestarttime = None
    lasteventtime = None
    for i in range(len(tab)):
        t = time.mktime(datetime.datetime.strptime(tab['timestamp'][i],"%Y/%m/%d %H:%M:%S").timetuple())
        if tab['Case_ID'][i] != lastcase: # if its a new case
            casestarttime = t
            lasteventtime = t
            lastcase = tab['Case_ID'][i]
            if not firstLine: # add the previous case
                lines.append(line)
                lines_t.append(times)
                lines_t2.append(times2)
                lines_t3.append(times3)
                lines_t4.append(times4)
            line = []
            times = []
            times2 = []
            times3 = []
            times4 = []
        line.append(tab['Activity'][i])
        timesincelastevent = t - lasteventtime
        timesincecasestart = t - casestarttime
        midnight = datetime.datetime.fromtimestamp(t).replace(hour=0, minute=0, second=0, microsecond=0)
        timesincemidnight = (datetime.datetime.fromtimestamp(t)-midnight).total_seconds()
        dayinweek = datetime.datetime.fromtimestamp(t).weekday() #day of the week
        times.append(timesincelastevent)
        times2.append(timesincecasestart)
        times3.append(timesincemidnight)
        times4.append(dayinweek)
        lasteventtime = t
        firstLine = False

    # add the last case
    lines.append(line)
    lines_t.append(times)
    lines_t2.append(times2)
    lines_t3.append(times3)
    lines_t4.append(times4)
    return lines, lines_t, lines_t2, lines_t3, lines_t4


def Extract_prefix(lines, lines_t, lines_t2, lines_t3, lines_t4):
    step = 1
    sentences = []
    next_ope = []
    sentences_t = []
    sentences_t2 = []
    sentences_t3 = []
    sentences_t4 = []
    next_ope_t = []
    end_ope_t = []
    for line, line_t, line_t2, line_t3, line_t4 in zip(lines, lines_t, lines_t2, lines_t3, lines_t4):
        for i in range(2, len(line), step): # Keep only prefix with length min = 2
            sentences.append(line[0: i])
            sentences_t.append(line_t[0:i])
            sentences_t2.append(line_t2[0:i])
            sentences_t3.append(line_t3[0:i])
            sentences_t4.append(line_t4[0:i])
            next_ope.append(line[i])
            next_ope_t.append(line_t[i])
            end_ope_t.append(line_t2[-1] - line_t2[i-1])
    return [sentences, sentences_t, sentences_t2, sentences_t3, sentences_t4], [next_ope, next_ope_t, end_ope_t]


if __name__ == "__main__":
#     tab_train= pd.read_csv(data_dir+"PPM_data/Helpdesk_processed_train_v1.csv")
    tab_test = pd.read_csv(data_dir+"Helpdesk_processed_test.csv")
    lines, lines_t, lines_t2, lines_t3, lines_t4 = Extract_trace_and_timed_features(tab_test)
    prefix, output = Extract_prefix(lines, lines_t, lines_t2, lines_t3, lines_t4)
    print(len(prefix[0]))
    
    
    
    