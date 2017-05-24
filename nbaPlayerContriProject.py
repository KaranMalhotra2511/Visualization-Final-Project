import sys
import csv
import numpy as np
import scipy.stats as ss
import pandas as pd
import random
import matplotlib.pyplot as plt



def calculateValPlayerForTeam(playersTemp):
    players = playersTemp
    players['val'] = (players['pts'] - 0.994 * players['fgm'] - 0.607 * players['ftm'] + players['asts']*1.13 + players ['oreb']*0.988 + players['dreb']*0.605 + players['stl']*1.651 + players['blk'] * 0.911 - players['turnover']*1.550 -players['pf']*0.221)/players['gp']
    players = players.sort_values(['val'], ascending=[False])
    print players.loc[:,['firstname','lastname','val']] #players[ 'firstname' ]
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career_val.csv", sep=',')

def calculateAllValPlayerForTeam(playersTemp):
    players = playersTemp
    players['shooterVal'] = (players['fga']/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))
    players['guardVal'] = ((players['asts']+players['stl'])/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))
    players['bigManVal'] = ((players['reb']+players['blk'])/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))

    shooterVal = players['shooterVal'].tolist()
    guardVal = players['guardVal'].tolist()
    bigManVal = players['bigManVal'].tolist()

    shooterVal.sort(reverse=1)
    guardVal.sort(reverse=1)
    bigManVal.sort(reverse=1)




    shooterVal = [x for x in shooterVal if str(x) != 'nan']
    guardVal = [x for x in guardVal if str(x) != 'nan']
    bigManVal = [x for x in bigManVal if str(x) != 'nan']

    # shooterVal = [x for x in shooterVal if str(x) != '0.0']
    # guardVal = [x for x in guardVal if str(x) != '0.0']
    # bigManVal = [x for x in bigManVal if str(x) != '0.0']


    # del shooterVal[-1]
    # del guardVal[-1]
    # del bigManVal[-1]

    print "shooterVal ",len(shooterVal),shooterVal
    print "guardVal ",len(guardVal),guardVal
    print "bigManVal ",len(bigManVal),bigManVal

    print "shootVal avg ",sum(float(i) for i in shooterVal)/float(len(shooterVal))
    print "guardVal avg ",sum(float(i) for i in guardVal)/float(len(guardVal))
    print "bigManVal avg ",sum(float(i) for i in bigManVal)/float(len(bigManVal))

    l = [1.0,2,3.0,4,5]
    print "bigManVal avg ",sum(l)
    players = players.sort_values(['val'], ascending=[False])
    # print players.loc[:,['firstname','lastname','shooterVal']] #players[ 'firstname' ]
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career_shooter_all_val.csv", sep=',')
    top100Players  = players.head(20)
    top100Players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career_shooter_all_20_val.csv", sep=',')



def calculateShooterValPlayerForTeam(playersTemp):
    players = playersTemp
    players['shooterVal'] = (players['fga']/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))
    players['guardVal'] = ((players['asts']+players['stl'])/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))
    players['bigManVal'] = ((players['reb']+players['blk'])/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))
    players = players.sort_values(['shooterVal'], ascending=[False])
    print players.loc[:,['firstname','lastname','shooterVal']] #players[ 'firstname' ]
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career_shooter_val.csv", sep=',')

    gp = players['gp'].tolist()
    gp.sort(reverse=1)
    print gp
    kArr = list(xrange(4052))
    plt.plot( kArr, gp,c='blue',label="test1")
    plt.xticks(np.arange(1, 4052, 1.0))
    plt.show()


def calculateGuardValPlayerForTeam(playersTemp):
    players = playersTemp
    players['guardVal'] = ((players['asts']+players['stl'])/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))
    players = players.sort_values(['guardVal'], ascending=[False])
    print players.loc[:,['firstname','lastname','guardVal']] #players[ 'firstname' ]
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career_guard_val.csv", sep=',')

def calculateBigManValPlayerForTeam(playersTemp):
    players = playersTemp
    players['bigManVal'] = ((players['reb']+players['blk'])/ (players['fga']+players['reb']+players['asts']+players['stl']+players['blk']))
    players = players.sort_values(['bigManVal'], ascending=[False])
    print players.loc[:,['firstname','lastname','bigManVal']] #players[ 'firstname' ]
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career_bigman_val.csv", sep=',')

def calculateNoOfAttributes(players):
    for i in range(0,len(players.columns)):
        list1 = players.ix[:, i].tolist()
        list1_set = set(list1)
        playersList = list(players)
        print (playersList[i]," ",len(list1_set))

def calculateTeamWinsAndCreateJson(teams):
    teams1 = list(teams['franchID'].unique())

    for team in teams1:
        temp = teams.loc[(teams['franchID'] == team)]
        temp = teams.loc[(teams['tmID'] == team)]
        temp = temp.loc[(temp['rank']==1)]
        temp = temp[['year','franchID']]
        print  team," - ",len(temp.index)#team," - ", temp.count


def calculateDraftAndCreatecsv(drafts):
    draftList = list(drafts['draftFrom'].unique())
    countList = []
    for draft in draftList:
        temp = drafts.loc[(drafts['draftFrom'] == draft)]
        count = len(temp.index)
        countList.append(int(count))
        print draft ," - ",count


    countList = map(int, countList)

    print countList

    draftCollege = pd.DataFrame(
    {'college': draftList,
     'count': countList
     })
    # draftCollege = pd.DataFrame(np.column_stack([draftList, countList]),
    #                            columns=['college', 'count'])
    draftCollege = draftCollege.sort_values('count', ascending=False)

    print draftCollege

    draftCollege.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_draft_college.csv", sep=',')

    draftYears = list(drafts['draftYear'].unique())
    countYearList = []
    for drafty in draftYears:
        temp = drafts.loc[(drafts['draftYear'] == drafty)]
        count = len(temp.index)
        countYearList.append(count)
        print drafty ," - ",count
    draftYear = pd.DataFrame(
    {'year': draftYears,
     'count': countYearList
     })
    draftYear.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_draft_year.csv", sep=',')



def calculateBigman35(players):

    playersTemp = players.loc[(players['bigManVal'] >= bigManAvg)]
    players = playersTemp.head(35)
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_bigMan_35_val.csv", sep=',')

def calculateGuard35(players):
    guardVal = players['guardVal'].tolist()

    guardVal = [x for x in guardVal if str(x) != 'nan']

    guardAvg = sum(guardVal)/len(guardVal)
    playersTemp = players.loc[(players['guardVal'] >= guardAvg)]
    players = playersTemp.head(35)
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_guard_35_val.csv", sep=',')

def calculateShooter35(players):

    shooterVal = players['shooterVal'].tolist()
    shooterVal = [x for x in shooterVal if str(x) != 'nan']
    shooterAvg = sum(shooterVal)/len(shooterVal)

    guardVal = players['guardVal'].tolist()
    guardVal = [x for x in guardVal if str(x) != 'nan']
    guardAvg = sum(guardVal)/len(guardVal)

    bigManVal = players['bigManVal'].tolist()
    bigManVal = [x for x in bigManVal if str(x) != 'nan']
    bigManAvg = sum(bigManVal)/len(bigManVal)

    print('s,g,b ',shooterAvg,guardAvg,bigManAvg)

    playersTemp = players.loc[(players['shooterVal'] >= shooterAvg) & (players['guardVal'] < guardAvg) & (players['bigManVal'] < bigManAvg)]
    playersTemp['type'] = 'shooter'
    playersShooter = playersTemp.head(35)

    playersShooter.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_shooter_35_val.csv", sep=',')

    playersTemp = players.loc[(players['guardVal'] >= guardAvg) & (players['shooterVal'] < shooterAvg) & (players['bigManVal'] < bigManAvg)]
    playersTemp['type'] = 'guard'
    playersGuard = playersTemp.head(35)
    playersGuard.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_guard_35_val.csv", sep=',')

    playersTemp = players.loc[(players['bigManVal'] >= bigManAvg) & (players['guardVal'] < guardAvg) & (players['shooterVal'] < shooterAvg)]
    playersTemp['type'] = 'bigMan'
    playersBigMan = playersTemp.head(35)
    playersBigMan.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_bigMan_35_val.csv", sep=',')

def calculateBigGuard35(players):
    guardVal = players['guardVal'].tolist()

    guardVal = [x for x in guardVal if str(x) != 'nan']

    guardAvg = sum(guardVal)/len(guardVal)
    bigManVal = players['bigManVal'].tolist()
    bigManVal = [x for x in bigManVal if str(x) != 'nan']
    bigManAvg = sum(bigManVal)/len(bigManVal)
    playersTemp = players.loc[(players['guardVal'] >= guardAvg)&(players['bigManVal'] >= bigManAvg)]
    playersTemp['type'] = 'bigGuard'
    players = playersTemp.head(35)
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_bigGuard_35_val.csv", sep=',')

def calculateBigShooter35(players):
    shooterVal = players['shooterVal'].tolist()
    shooterVal = [x for x in shooterVal if str(x) != 'nan']
    bigManVal = players['bigManVal'].tolist()
    bigManVal = [x for x in bigManVal if str(x) != 'nan']
    bigManAvg = sum(bigManVal)/len(bigManVal)
    shooterAvg = sum(shooterVal)/len(shooterVal)
    playersTemp = players.loc[(players['shooterVal'] >= shooterAvg)&(players['bigManVal'] >= bigManAvg)]
    playersTemp['type'] = 'bigShooter'
    players = playersTemp.head(35)
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_bigShooter_35_val.csv", sep=',')

def calculateGuardShooter35(players):
    shooterVal = players['shooterVal'].tolist()
    shooterVal = [x for x in shooterVal if str(x) != 'nan']
    guardVal = players['guardVal'].tolist()
    guardVal = [x for x in guardVal if str(x) != 'nan']
    guardAvg = sum(guardVal)/len(guardVal)
    shooterAvg = sum(shooterVal)/len(shooterVal)
    playersTemp = players.loc[(players['shooterVal'] >= shooterAvg)&(players['guardVal'] >= guardAvg)]
    playersTemp['type'] = 'guardShooter'
    players = playersTemp.head(35)
    players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_guardShooter_35_val.csv", sep=',')

# def calculateALL35(players):






def main():

    # teams = pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/basketball_teams.csv")
    #
    # # calculateTeamWinsAndCreateJson(teams)
    #
    drafts = pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/basketball_draft.csv")
    #
    calculateDraftAndCreatecsv(drafts)

    coreln = pd.read_csv("/Users/kedarsankarbehera/Documents/Projects/web copy 2/data/player_all_100_corelation.csv")
    #
    coreln = coreln.sort_values("val",ascending=False)
    coreln = coreln.head(10)
    coreln.to_csv("/Users/kedarsankarbehera/Documents/Projects/web copy 2/data/player_all_10_corelation.csv",sep=',')



    # players = players.loc[(players['gp'] >= 250)]
    #
    #
    # calculateShooter35(players)
    # calculateBigGuard35(players)
    # calculateBigShooter35(players)
    # calculateGuardShooter35(players)


    # players = players.head(35)
    # players.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career_shooter_all_35_val.csv", sep=',')



    print "----------------------------------------------------------------------------"

    # focus_cols = ['val']
    # list1 = players.corr().filter(focus_cols).drop(focus_cols)
    # # print list1
    # list1 = list1.sort_values('val', ascending=False)
    # # list1.sort('val', ascending=False)
    # list1 = list1.head(17)
    # list1.to_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_all_100_corelation.csv", sep=',')




    # players =  pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_career.csv")
    # # teams =  pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/teams.csv")
    # # draft =  pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/draft.csv")
    # player_allstar =  pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_allstar.csv")
    # player_playoffs =  pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_playoffs.csv")
    # # player_regular_season = pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/player_regular_season.csv")
    # team_season = pd.read_csv("/Users/kedarsankarbehera/Downloads/databasebasketball_2009_v1/team_season.csv")
    # print "-------------------------------------------- players --------------------------------------------------------------------------------"
    # calculateNoOfAttributes(players)
    # print "-------------------------------------------- teams --------------------------------------------------------------------------------"
    # calculateNoOfAttributes(teams)
    # # print "----------------------------------------------------------------------------------------------------------------------------"
    # # calculateNoOfAttributes(draft)
    # print "------------------------------------------------ player_allstar ----------------------------------------------------------------------------"
    # calculateNoOfAttributes(player_allstar)
    # print "----------------------------------------------------- player_playoffs -----------------------------------------------------------------------"
    # calculateNoOfAttributes(player_playoffs)
    # # print "----------------------------------------------------------------------------------------------------------------------------"
    # # calculateNoOfAttributes(player_regular_season)
    # print "-------------------------------------------------------- team_season --------------------------------------------------------------------"
    # calculateNoOfAttributes(team_season)
    # calculateValPlayerForTeam(players)
    # # print "----------SHOOTER----------------------------"
    # # # calculateShooterValPlayerForTeam(players)
    # # # print "----------GUARD----------------------------"
    # # # calculateGuardValPlayerForTeam(players)
    # # # print "----------BIGMAN----------------------------"
    # # # calculateBigManValPlayerForTeam(players)
    # # print "----------ALL----------------------------"
    # calculateAllValPlayerForTeam(players)

main()
