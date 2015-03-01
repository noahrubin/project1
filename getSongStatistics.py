#getSongStatistics.py
#Noah Rubin (nar62)
#February 28, 2015

import json
from pprint import pprint
import math
import numpy

def groupByYear(jsonData):
    songs_1970 = []
    songs_1980 = []
    songs_1990 = []
    songs_2000 = []
    songs_2010 = []
    songs_IDK = []

    for elem in jsonData:
        if (elem["tempo"] != 0 and elem["hotttnesss"] != 0):
            if (elem["year"] >= 1970 and elem["year"] < 1980):
                songs_1970.append(elem)
            elif (elem["year"] >= 1980 and elem["year"] < 1990):
                songs_1980.append(elem)
            elif (elem["year"] >= 1990 and elem["year"] < 2000):
                songs_1990.append(elem)
            elif (elem["year"] >= 2000 and elem["year"] < 2010):
                songs_2000.append(elem)
            elif (elem["year"] >= 2010):
                songs_2010.append(elem)
            elif (elem["year"] == 0):
                songs_IDK.append(elem)
        else:
            songs_IDK.append(elem)

    return songs_1970, songs_1980, songs_1990, songs_2000, songs_2010, songs_IDK

def getMean_ints(songs_Year, measure):
    sum = 0
    for elem in songs_Year:
        sum += elem[measure]

    return sum/len(songs_Year)

def getMedian(songs_Year, measure):
    measures = []
    for elem in songs_Year:
        measures.append(elem[measure])

    return numpy.median(measures)

def getMean_floats(songs_Year, measure):
    tempos = []
    for elem in songs_Year:
        tempos.append(elem[measure])

    return math.fsum(tempos)/len(songs_Year)

def jsonifySongs(decade, h_mean, h_median, t_mean, t_median):
    return json.dumps({"decade":decade, "hotttnesss_mean":h_mean,
           "hotttnesss_median":h_median, "tempo_mean":t_mean,
           "tempo_median":t_median}, sort_keys=True, indent=4, separators=(',',':'))

if __name__ == "__main__":

    json_data = open('songs.json')
    data = json.load(json_data)
    newline = "\n"
    comma = ","

    songs_1970, songs_1980, songs_1990, songs_2000, songs_2010, songs_IDK = groupByYear(data)

    #extract Hotttness means
    hotttness_mean_1970 = getMean_ints(songs_1970, "hotttnesss")
    hotttness_mean_1980 = getMean_ints(songs_1980, "hotttnesss")
    hotttness_mean_1990 = getMean_ints(songs_1990, "hotttnesss")
    hotttness_mean_2000 = getMean_ints(songs_2000, "hotttnesss")
    hotttness_mean_2010 = getMean_ints(songs_2010, "hotttnesss")

    #extract Hotttness medians
    hotttness_median_1970 = getMedian(songs_1970, "hotttnesss")
    hotttness_median_1980 = getMedian(songs_1980, "hotttnesss")
    hotttness_median_1990 = getMedian(songs_1990, "hotttnesss")
    hotttness_median_2000 = getMedian(songs_2000, "hotttnesss")
    hotttness_median_2010 = getMedian(songs_2010, "hotttnesss")

    #extract Tempo means
    tempo_mean_1970 = getMean_floats(songs_1970, "tempo")
    tempo_mean_1980 = getMean_floats(songs_1980, "tempo")
    tempo_mean_1990 = getMean_floats(songs_1990, "tempo")
    tempo_mean_2000 = getMean_floats(songs_2000, "tempo")
    tempo_mean_2010 = getMean_floats(songs_2010, "tempo")

    #extract Tempo medians
    tempo_median_1970 = getMedian(songs_1970, "tempo")
    tempo_median_1980 = getMedian(songs_1980, "tempo")
    tempo_median_1990 = getMedian(songs_1990, "tempo")
    tempo_median_2000 = getMedian(songs_2000, "tempo")
    tempo_median_2010 = getMedian(songs_2010, "tempo")

    # #extract Danceability means
    # danceability_1970 = getMean_ints(songs_1970, "danceability")
    # danceability_1980 = getMean_ints(songs_1980, "danceability")
    # danceability_1990 = getMean_ints(songs_1990, "danceability")
    # danceability_2000 = getMean_ints(songs_2000, "danceability")
    # danceability_2010 = getMean_ints(songs_2010, "danceability")

    data_1970 = jsonifySongs(1970, hotttness_mean_1970, hotttness_median_1970, tempo_mean_1970, tempo_median_1970)
    data_1980 = jsonifySongs(1980, hotttness_mean_1980, hotttness_median_1980, tempo_mean_1980, tempo_median_1980)
    data_1990 = jsonifySongs(1990, hotttness_mean_1990, hotttness_median_1990, tempo_mean_1990, tempo_median_1990)
    data_2000 = jsonifySongs(2000, hotttness_mean_2000, hotttness_median_2000, tempo_mean_2000, tempo_median_2000)
    data_2010 = jsonifySongs(2010, hotttness_mean_2010, hotttness_median_2010, tempo_mean_2010, tempo_median_2010)

    pprint(len(songs_IDK))

    doc = open("songStatistics.json", 'w')
    doc.write("[" + newline
                  + data_1970 + comma + newline
                  + data_1980 + comma + newline
                  + data_1990 + comma + newline
                  + data_2000 + comma + newline
                  + data_2010 + comma + newline +
                  "]")

    doc.close()
    json_data.close()
