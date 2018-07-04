import requests
import json

class FortniteTrackerAPI : 
    Platform = ''
    Username = ''
    url = ''

    def __init__ (self, platform = '', username = ''):
        while True:
            if platform == '' :
                self.Platform = input('What platform? (pc, xbl, psn)').lower()
        else:
            self.Platform = platform

            if self.Platform == 'pc' or self.Platform == 'xbl' or self.Platform == 'psn' :
                break
            else :
                print ('Invalid platform')

        if username == '' :
            self.Username = input('What is the Epic Username?').lower()
        else:
            self.Username = username

    def SetUrl(self) :
        self.url = 'https://api.fortnitetracker.com/v1/profile/'
        self.url = self.url + self.Platform
        self.url = self.url + '/'
        self.url = self.url + self.Username
        return self.url
    
    def GetUrl(self) :
        return self.url
        
    def GetStats(self, file = 'FortniteTrackerStatistics.txt') :
        f = open(file , 'w+')
        FortniteTrackerAPI.SetUrl(FortniteTrackerAPI)
        r = requests.get(self.url, headers = {'TRN-Api-Key': '56483f66-82ed-4d24-9484-49ac38089be1'})
        f.write(r.text)
        f.close

    def GetUsername(self, file = 'FortniteTrackerStatistics.txt') :
        f = open(file)
        stats = f.read()
        stats = ast.literal_eval(stats)
        return (stats['epicUserHandle'])

    # def ValidateStats(self, file = 'FortniteTrackerStatistics.txt') :
        

# https://api.fortnitetracker.com/v1/profile/{Platform}/{Username} , headers = {'TRN-Api-Key': '56483f66-82ed-4d24-9484-49ac38089be1'})
# print (stats['epicUserHandle'], 'has', stats['stats']['p2']['top1']['valueInt'], 'solo wins.')
# {'accountId': 'dba76bb6-87c5-4fd8-a65e-662298bd3c36', 'platformId': 1, 'platformName': 'xbox', 'platformNameLong': 'Xbox One', 'epicUserHandle': 'AarashJ', 'stats': {'p2': {'trnRating': {'label': 'TRN Rating', 'field': 'TRNRating', 'category': 'Rating', 'valueInt': 1948, 'value': '1948', 'rank': 519657, 'percentile': 4.2, 'displayValue': '1,948'}, 'score': {'label': 'Score', 'field': 'Score', 'category': 'General', 'valueInt': 289454, 'value': '289454', 'rank': 214570, 'percentile': 0.1, 'displayValue': '289,454'}, 'top1': {'label': 'Wins', 'field': 'Top1', 'category': 'Tops', 'valueInt': 106, 'value': '106', 'rank': 82979, 'percentile': 0.2, 'displayValue': '106'}, 'top3': {'label': 'Top 3', 'field': 'Top3', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top5': {'label': 'Top 5', 'field': 'Top5', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top6': {'label': 'Top 6', 'field': 'Top6', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top10': {'label': 'Top 10', 'field': 'Top10', 'category': 'Tops', 'valueInt': 290, 'value': '290', 'rank': 190740, 'percentile': 0.1, 'displayValue': '290'}, 'top12': {'label': 'Top 12', 'field': 'Top12', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top25': {'label': 'Top 25', 'field': 'Top25', 'category': 'Tops', 'valueInt': 504, 'value': '504', 'rank': 300244, 'percentile': 0.1, 'displayValue': '504'}, 'kd': {'label': 'K/d', 'field': 'KD', 'category': 'General', 'valueDec': 2.51, 'value': '2.51', 'rank': 830569, 'percentile': 7.0, 'displayValue': '2.51'}, 'winRatio': {'label': 'Win %', 'field': 'WinRatio', 'category': 'General', 'valueDec': 7.0, 'value': '7', 'rank': 682509, 'percentile': 6.0, 'displayValue': '7.00'}, 'matches': {'label': 'Matches', 'field': 'Matches', 'category': 'General', 'valueInt': 1517, 'value': '1517', 'rank': 509233, 'percentile': 0.2, 'displayValue': '1,517'}, 'kills': {'label': 'Kills', 'field': 'Kills', 'category': 'General', 'valueInt': 3547, 'value': '3547', 'rank': 133033, 'percentile': 0.1, 'displayValue': '3,547'}, 'kpg': {'label': 'Kills Per Match', 'field': 'KPG', 'category': 'General', 'valueDec': 2.34, 'value': '2.34', 'rank': 871680, 'percentile': 7.0, 'displayValue': '2.34'}, 'scorePerMatch': {'label': 'Score per Match', 'field': 'ScorePerMatch', 'category': 'General', 'valueDec': 190.81, 'value': '190.81', 'rank': 1665274, 'percentile': 14.0, 'displayValue': '190.81'}}, 'p10': {'trnRating': {'label': 'TRN Rating', 'field': 'TRNRating', 'category': 'Rating', 'valueInt': 1142, 'value': '1142', 'rank': 1424171, 'percentile': 55.0, 'displayValue': '1,142'}, 'score': {'label': 'Score', 'field': 'Score', 'category': 'General', 'valueInt': 184579, 'value': '184579', 'rank': 14116064, 'percentile': 0.4, 'displayValue': '184,579'}, 'top1': {'label': 'Wins', 'field': 'Top1', 'category': 'Tops', 'valueInt': 42, 'value': '42', 'rank': 9502495, 'percentile': 2.0, 'displayValue': '42'}, 'top3': {'label': 'Top 3', 'field': 'Top3', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top5': {'label': 'Top 5', 'field': 'Top5', 'category': 'Tops', 'valueInt': 124, 'value': '124', 'rank': 12105818, 'percentile': 1.1, 'displayValue': '124'}, 'top6': {'label': 'Top 6', 'field': 'Top6', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top10': {'label': 'Top 10', 'field': 'Top10', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top12': {'label': 'Top 12', 'field': 'Top12', 'category': 'Tops', 'valueInt': 279, 'value': '279', 'rank': 12996330, 'percentile': 0.4, 'displayValue': '279'}, 'top25': {'label': 'Top 25', 'field': 'Top25', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'kd': {'label': 'K/d', 'field': 'KD', 'category': 'General', 'valueDec': 1.55, 'value': '1.55', 'rank': 2350228, 'percentile':
# 22.0, 'displayValue': '1.55'}, 'winRatio': {'label': 'Win %', 'field': 'WinRatio', 'category': 'General', 'valueDec': 3.8, 'value': '3.8', 'rank': 9502406, 'percentile': 24.0, 'displayValue': '3.80'}, 'matches': {'label':
# 'Matches', 'field': 'Matches', 'category': 'General', 'valueInt': 1119, 'value': '1119', 'rank': 14839098, 'percentile': 0.2, 'displayValue': '1,119'}, 'kills': {'label': 'Kills', 'field': 'Kills', 'category': 'General', 'valueInt': 1669, 'value': '1669', 'rank': 13366216, 'percentile': 0.7, 'displayValue': '1,669'}, 'kpg': {'label': 'Kills Per Match', 'field': 'KPG', 'category': 'General', 'valueDec': 1.49, 'value': '1.49', 'rank': 2110056, 'percentile': 23.0, 'displayValue': '1.49'}, 'scorePerMatch': {'label': 'Score per Match', 'field': 'ScorePerMatch', 'category': 'General', 'valueDec': 164.95, 'value': '164.95', 'rank': 701439, 'percentile': 44.0, 'displayValue': '164.95'}}, 'p9': {'trnRating': {'label': 'TRN Rating', 'field': 'TRNRating', 'category': 'Rating', 'valueInt': 1156, 'value': '1156', 'rank': 11976885, 'percentile': 53.0, 'displayValue': '1,156'}, 'score': {'label': 'Score', 'field': 'Score', 'category': 'General', 'valueInt': 342734, 'value': '342734', 'rank': 725807, 'percentile': 0.4, 'displayValue': '342,734'}, 'top1': {'label': 'Wins', 'field': 'Top1', 'category': 'Tops',
# 'valueInt': 126, 'value': '126', 'rank': 517155, 'percentile': 0.7, 'displayValue': '126'}, 'top3': {'label': 'Top 3', 'field': 'Top3', 'category': 'Tops', 'valueInt': 230, 'value': '230', 'rank': 676070, 'percentile': 0.5, 'displayValue': '230'}, 'top5': {'label': 'Top 5', 'field': 'Top5', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top6': {'label': 'Top 6', 'field': 'Top6', 'category': 'Tops', 'valueInt': 380, 'value': '380', 'rank': 709518, 'percentile': 0.4, 'displayValue': '380'}, 'top10': {'label': 'Top 10', 'field': 'Top10', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top12': {'label': 'Top 12', 'field': 'Top12', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top25': {'label': 'Top 25', 'field': 'Top25', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'kd': {'label': 'K/d', 'field': 'KD', 'category': 'General', 'valueDec': 1.8, 'value': '1.8', 'rank': 2202708, 'percentile': 18.0, 'displayValue': '1.80'}, 'winRatio': {'label': 'Win %', 'field': 'WinRatio', 'category': 'General', 'valueDec': 8.9, 'value': '8.9', 'rank': 1746687, 'percentile': 14.0, 'displayValue': '8.90'}, 'matches': {'label': 'Matches', 'field': 'Matches', 'category': 'General', 'valueInt': 1409, 'value': '1409', 'rank': 1072028, 'percentile': 0.4, 'displayValue': '1,409'}, 'kills': {'label': 'Kills', 'field': 'Kills', 'category': 'General', 'valueInt': 2309, 'value': '2309', 'rank': 761274, 'percentile': 0.8,
# 'displayValue': '2,309'}, 'kpg': {'label': 'Kills Per Match', 'field': 'KPG', 'category': 'General', 'valueDec': 1.64, 'value': '1.64', 'rank': 2314878, 'percentile': 18.0, 'displayValue': '1.64'}, 'scorePerMatch': {'label': 'Score per Match', 'field': 'ScorePerMatch', 'category': 'General', 'valueDec': 243.25, 'value': '243.25', 'rank': 2210546, 'percentile': 20.0, 'displayValue': '243.25'}}, 'curr_p2': {'trnRating': {'label': 'TRN Rating', 'field': 'TRNRating', 'category': 'Rating', 'valueInt': 1948, 'value': '1948', 'rank': 519657, 'percentile': 4.5, 'displayValue': '1,948'}, 'score': {'label': 'Score', 'field': 'Score', 'category': 'General', 'valueInt': 57567, 'value': '57567', 'rank': 759490, 'percentile': 6.0, 'displayValue': '57,567'}, 'top1': {'label': 'Wins', 'field': 'Top1', 'category': 'Tops', 'valueInt': 21, 'value': '21', 'rank': 260096, 'percentile': 1.7, 'displayValue': '21'}, 'top3': {'label': 'Top 3', 'field': 'Top3', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top5': {'label': 'Top 5', 'field': 'Top5', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top6': {'label': 'Top 6', 'field': 'Top6', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top10': {'label': 'Top 10', 'field': 'Top10', 'category': 'Tops', 'valueInt': 63, 'value': '63', 'rank': 578194, 'percentile': 4.7, 'displayValue': '63'}, 'top12': {'label': 'Top 12', 'field': 'Top12', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top25': {'label': 'Top 25', 'field': 'Top25', 'category': 'Tops', 'valueInt': 103, 'value': '103', 'rank': 947191, 'percentile': 8.0, 'displayValue': '103'}, 'kd': {'label': 'K/d', 'field': 'KD', 'category': 'General', 'valueDec': 2.38, 'value': '2.38', 'rank': 1136632, 'percentile': 10.0, 'displayValue': '2.38'}, 'winRatio': {'label': 'Win %', 'field': 'WinRatio', 'category': 'General', 'valueDec': 6.1, 'value': '6.1', 'rank': 1018963, 'percentile': 11.0, 'displayValue': '6.10'}, 'matches': {'label': 'Matches', 'field': 'Matches', 'category': 'General', 'valueInt': 342, 'value': '342', 'rank': 1121929, 'percentile': 9.0, 'displayValue': '342'}, 'kills': {'label': 'Kills', 'field': 'Kills', 'category': 'General', 'valueInt': 763, 'value': '763', 'rank': 410197, 'percentile': 3.3, 'displayValue': '763'}, 'kpg': {'label': 'Kills Per Match', 'field': 'KPG', 'category': 'General', 'valueDec': 2.23, 'value': '2.23', 'rank': 1175700, 'percentile': 11.0, 'displayValue': '2.23'}, 'scorePerMatch': {'label': 'Score per Match', 'field': 'ScorePerMatch', 'category': 'General', 'valueDec':
# 168.32, 'value': '168.32', 'rank': 2617121, 'percentile': 23.0, 'displayValue': '168.32'}}, 'curr_p10': {'trnRating': {'label': 'TRN Rating', 'field': 'TRNRating', 'category': 'Rating', 'valueInt': 1142, 'value': '1142', 'rank': 1424171, 'percentile': 60.0, 'displayValue': '1,142'}, 'score': {'label': 'Score', 'field': 'Score', 'category': 'General', 'valueInt': 45510, 'value': '45510', 'rank': 9789104, 'displayValue': '45,510'}, 'top1': {'label': 'Wins', 'field': 'Top1', 'category': 'Tops', 'valueInt': 17, 'value': '17', 'rank': 6124821, 'percentile': 4.4, 'displayValue': '17'}, 'top3': {'label': 'Top 3', 'field': 'Top3', 'category': 'Tops', 'valueInt': 0,
# 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top5': {'label': 'Top 5', 'field': 'Top5', 'category': 'Tops', 'valueInt': 32, 'value': '32', 'rank': 7962678, 'percentile': 10.0, 'displayValue': '32'}, 'top6': {'label': 'Top 6', 'field': 'Top6', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top10': {'label': 'Top 10', 'field': 'Top10', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'top12': {'label': 'Top 12', 'field': 'Top12', 'category': 'Tops', 'valueInt': 60, 'value': '60', 'rank': 8697239, 'percentile': 11.0, 'displayValue': '60'}, 'top25': {'label': 'Top 25', 'field': 'Top25', 'category': 'Tops', 'valueInt': 0, 'value': '0', 'rank': 1, 'displayValue': '0'}, 'kd': {'label': 'K/d', 'field': 'KD', 'category': 'General', 'valueDec': 1.49, 'value': '1.49', 'rank': 2445161, 'percentile': 31.0, 'displayValue': '1.49'}, 'winRatio': {'label': 'Win %', 'field': 'WinRatio', 'category': 'General', 'valueDec': 6.2, 'value': '6.2', 'rank': 6124817, 'percentile': 18.0, 'displayValue': '6.20'}, 'matches': {'label': 'Matches', 'field': 'Matches', 'category': 'General', 'valueInt': 276, 'value': '276', 'rank': 10261243, 'percentile': 6.0, 'displayValue': '276'}, 'kills': {'label': 'Kills', 'field': 'Kills', 'category': 'General', 'valueInt': 385, 'value': '385', 'rank': 9211528, 'percentile': 8.0, 'displayValue': '385'}, 'kpg': {'label': 'Kills Per Match', 'field': 'KPG', 'category': 'General', 'valueDec': 1.39, 'value': '1.39', 'rank': 2223995, 'percentile': 33.0, 'displayValue': '1.39'}, 'scorePerMatch': {'label': 'Score per Match', 'field': 'ScorePerMatch', 'category': 'General', 'valueDec': 164.89, 'value': '164.89', 'rank': 800857, 'percentile': 45.0, 'displayValue': '164.89'}}, 'curr_p9': {'trnRating': {'label': 'TRN Rating', 'field': 'TRNRating', 'category': 'Rating', 'valueInt': 1156, 'value': '1156', 'rank': 11976885, 'percentile': 46.0, 'displayValue': '1,156'}, 'score': {'label': 'Score', 'field': 'Score', 'category': 'General', 'valueInt': 122103, 'value': '122103', 'rank': 408075, 'percentil
