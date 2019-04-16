from chaleurculture.models import RosterStats,DefenseStats,BasicStats,AdvancedStats,HustleStats,UpdatesStats
from chaleurculture.nbatesting import heightcalc,weightcalc
def create_hustle_entries(hustle_list):
    #list of dictionaries
    #print(hustle_list)
        try: 
                for hustle in hustle_list:
                        
                                HustleStats.objects.create(
                                        
                                        PLAYER_NAME= hustle['PLAYER_NAME'], 
                                        CONTESTED_SHOTS_2PT= hustle['CONTESTED_SHOTS_2PT'],
                                        MIN= hustle['MIN'], 
                                        AGE= hustle['AGE'],
                                        CONTESTED_SHOTS_3PT= hustle['CONTESTED_SHOTS_3PT'],
                                        DEF_LOOSE_BALLS_RECOVERED= hustle['DEF_LOOSE_BALLS_RECOVERED'],
                                        CONTESTED_SHOTS= hustle['CONTESTED_SHOTS'],

                                        PCT_LOOSE_BALLS_RECOVERED_DEF=hustle['PCT_LOOSE_BALLS_RECOVERED_DEF'],

                                        CHARGES_DRAWN=hustle['CHARGES_DRAWN'],
                                        DEFLECTIONS=hustle['DEFLECTIONS'],

                                        OFF_LOOSE_BALLS_RECOVERED=hustle['OFF_LOOSE_BALLS_RECOVERED'],
                                        SCREEN_AST_PTS=hustle['SCREEN_AST_PTS'],
                                        TEAM_ABBREVIATION=hustle['TEAM_ABBREVIATION'],
                                        PCT_LOOSE_BALLS_RECOVERED_OFF=hustle['PCT_LOOSE_BALLS_RECOVERED_OFF'],
                                        PLAYER_ID=hustle['PLAYER_ID'], 

                                        SCREEN_ASSISTS=hustle['SCREEN_ASSISTS'],
                                        LOOSE_BALLS_RECOVERED=hustle['LOOSE_BALLS_RECOVERED'],
                                        G=hustle['G'],
                        )
                return "All Fine"
        except Exception as e:
                return str(e)
         
        
def create_roster_entries(roster_list):
    #list of dictionaries
        try:
                for roster in roster_list:
                
                        RosterStats.objects.create(
                        PLAYER_ID= roster['PLAYER_ID'], 
                        SCHOOL = roster['SCHOOL'], 
                        WEIGHT = roster['WEIGHT'], 
                        AGE = roster['AGE'], 
                        HEIGHT= roster['HEIGHT'],
                        EXP =roster['EXP'],
                        LeagueID =roster['LeagueID'], 
                        PLAYER =roster['PLAYER'] , 
                        POSITION =roster['POSITION'], 
                        NUM =roster['NUM'], 
                        TeamID =roster['TeamID'] ,
                        SEASON =roster['SEASON'],
                        BIRTH_DATE =roster['BIRTH_DATE'],
                        PCTDIFFWEIGHT=  round(
                                        weightcalc(
                                                heightcalc(roster['HEIGHT']),
                                                int(roster['WEIGHT'])
                                                ),2
                                                )
                        )
                return "All Fine"
        except Exception as e:
                return str(e) 
       
def create_defense_entries(defense_list):
        #list of dictionaries
        try:
                for defense in defense_list:
                        DefenseStats.objects.create(

                        OPP_PTS_PAINT=defense['OPP_PTS_PAINT'], 
                        OPP_PTS_OFF_TOV_RANK=defense['OPP_PTS_OFF_TOV_RANK'], 
                        PCT_STL=defense['PCT_STL'], 
                        OPP_PTS_2ND_CHANCE_RANK=defense['OPP_PTS_2ND_CHANCE_RANK'], 
                        PLAYER_ID=defense['PLAYER_ID'], 
                        MIN=defense['MIN'], 
                        DREB=defense['DREB'], 
                        PCT_STL_RANK=defense['PCT_STL_RANK'], 
                        MIN_RANK=defense['MIN_RANK'], 
                        DEF_RATING=defense['DEF_RATING'], 
                        DEF_WS_RANK=defense['DEF_WS_RANK'], 
                        W_RANK=defense['W_RANK'], 
                        DREB_RANK=defense['DREB_RANK'], 
                        PCT_BLK=defense['PCT_BLK'], 
                        GP_RANK=defense['GP_RANK'], 
                        DEF_RATING_RANK=defense['DEF_RATING_RANK'], 
                        OPP_PTS_OFF_TOV=defense['OPP_PTS_OFF_TOV'], 
                        OPP_PTS_FB_RANK=defense['OPP_PTS_FB_RANK'], 
                        STL=defense['STL'], 
                        DREB_PCT_RANK=defense['DREB_PCT_RANK'], 
                        CFPARAMS=defense['CFPARAMS'], 
                        L=defense['L'], 
                        CFID=defense['CFID'], 
                        L_RANK=defense['L_RANK'], 
                        W=defense['W'], 
                        PCT_DREB_RANK=defense['PCT_DREB_RANK'], 
                        DEF_WS=defense['DEF_WS'], 
                        PCT_DREB=defense['PCT_DREB'], 
                        BLK=defense['BLK'],  
                        GP=defense['GP'], 
                        BLK_RANK=defense['BLK_RANK'], 
                        OPP_PTS_2ND_CHANCE=defense['OPP_PTS_2ND_CHANCE'], 
                        PCT_BLK_RANK=defense['PCT_BLK_RANK'], 
                        DREB_PCT=defense['DREB_PCT'], 
                        TEAM_ID=defense['TEAM_ID'], 
                        AGE=defense['AGE'], 
                        OPP_PTS_FB=defense['OPP_PTS_FB'], 
                        W_PCT_RANK=defense['W_PCT_RANK'], 
                        W_PCT=defense['W_PCT'], 
                        STL_RANK=defense['STL_RANK'] ,
                        OPP_PTS_PAINT_RANK=defense['OPP_PTS_PAINT_RANK']
                        )
                return "All Fine"
        except Exception as e:
                return str(e)
def create_advanced_entries(advanced_list):
        try:
                for advanced in advanced_list:
                        AdvancedStats.objects.create(
                        PLAYER_ID= advanced['PLAYER_ID'], 
                        TEAM_ID =                 advanced['TEAM_ID'],
                        FG_PCT_RANK= advanced['FG_PCT_RANK'], 
                        FGA=advanced['FGA'], 
                        TM_TOV_PCT_RANK=advanced['TM_TOV_PCT_RANK'], 
                        PLAYER_NAME= advanced['PLAYER_NAME'],
                        L=advanced['L'], 
                        eDEF_RATING_RANK=advanced['eDEF_RATING_RANK'],
                        sp_work_NET_RATING=advanced['sp_work_NET_RATING'],
                        FGA_PG_RANK=advanced['FGA_PG_RANK'],
                        FGM_PG=advanced['FGM_PG'],
                        DEF_RATING= advanced['DEF_RATING'],
                        AST_RATIO=advanced['AST_RATIO'], 
                        TS_PCT=advanced['TS_PCT'],
                        EFG_PCT_RANK=advanced['EFG_PCT_RANK'],
                        eDEF_RATING= advanced['eDEF_RATING'],
                        FG_PCT =advanced['FG_PCT'] ,
                        OFF_RATING_RANK= advanced['OFF_RATING_RANK'],
                        AST_PCT= advanced['AST_PCT'],
                        FGM =advanced['FGM'], 
                        FGM_RANK =advanced['FGM_RANK'], 
                        sp_work_OFF_RATING= advanced['sp_work_OFF_RATING'],
                        sp_work_PACE = advanced['sp_work_PACE'],
                        eNET_RATING_RANK = advanced['eNET_RATING_RANK'], 
                        eOFF_RATING_RANK = advanced['eOFF_RATING_RANK'], 
                        eNET_RATING= advanced['eNET_RATING'], 
                        REB_PCT_RANK= advanced['REB_PCT_RANK'],
                        sp_work_DEF_RATING_RANK =advanced['sp_work_DEF_RATING_RANK'], 

                        EFG_PCT= advanced['EFG_PCT'], 
                        W_PCT =advanced['W_PCT'],
                        MIN_RANK = advanced['MIN_RANK'], 
                        OFF_RATING =advanced['OFF_RATING'],
                        TS_PCT_RANK = advanced['TS_PCT_RANK'], 
                        sp_work_DEF_RATING =advanced['sp_work_DEF_RATING'], 
                        DEF_RATING_RANK= advanced['DEF_RATING_RANK'], 
                        AST_RATIO_RANK= advanced['AST_RATIO_RANK'], 
                        TM_TOV_PCT =    advanced['TM_TOV_PCT'],
                        W_RANK= advanced['W_RANK'],
                        PIE=     advanced['PIE'],
                        sp_work_PACE_RANK=advanced['sp_work_PACE_RANK'], 
                        GP =advanced['GP'], 
                        W_PCT_RANK=  advanced['W_PCT_RANK'],
                        DREB_PCT = advanced['DREB_PCT'],
                        MIN = advanced['MIN'], 
                        AST_TO_RANK= advanced['AST_TO_RANK'],   
                        PIE_RANK=  advanced['PIE_RANK'], 
                        L_RANK =advanced['L_RANK'], 
                        OREB_PCT_RANK =  advanced['OREB_PCT_RANK'],
                        PACE= advanced['PACE'],
                        USG_PCT_RANK= advanced['USG_PCT_RANK'], 
                        sp_work_NET_RATING_RANK= advanced['sp_work_NET_RATING_RANK'], 
                        CFID = advanced['CFID'], 
                        FGA_PG = advanced['FGA_PG'],
                        OREB_PCT =advanced['OREB_PCT'], 
                        ePACE = advanced['ePACE'],
                        NET_RATING = advanced['NET_RATING'] , 
                        GP_RANK = advanced['GP_RANK'], 
                        USG_PCT = advanced['USG_PCT'], 
                        DREB_PCT_RANK = advanced['DREB_PCT_RANK'], 
                        ePACE_RANK = advanced['ePACE_RANK'], 
                        REB_PCT=                   advanced['REB_PCT'], 
                        NET_RATING_RANK =                advanced['NET_RATING_RANK'] , 
                        PACE_RANK =               advanced['PACE_RANK'],
                        FGA_RANK =                advanced['FGA_RANK'],
                        AST_PCT_RANK =                advanced['AST_PCT_RANK'],
                        W =                  advanced['W'],
                        
                        sp_work_OFF_RATING_RANK  =                advanced['sp_work_OFF_RATING_RANK'],
                        eOFF_RATING =                advanced['eOFF_RATING'],
                        FGM_PG_RANK  =                   advanced['FGM_PG_RANK'],
                        AST_TO   =                   advanced['AST_TO'],
                        )
                return "All Fine"
        except Exception as e:
                return str(e)

def create_update_entry(update_dict):
      UpdatesStats.objects.create(
        HustleStatsStatus=update_dict['HustleStatsStatus'],
        AdvancedStatsStatus=   update_dict['AdvancedStatsStatus'],
        RegStatsStatus=    update_dict['RegStatsStatus'],
        DefenseStatsStatus=update_dict['DefenseStatsStatus'],
        RosterStatsStatus=  update_dict['RosterStatsStatus'],
      )
def create_regular_entries(regular_list):   
        try:         
                for regular in regular_list:
                        BasicStats.objects.create(
                                TEAM_ID = regular['TEAM_ID'],
                                GP  = regular['GP'], 
                                FTA = regular['FTA'] ,
                                FG3M_RANK = regular['FG3M_RANK'],
                                FG3M = regular['FG3M'],
                                FT_PCT_RANK = regular['FT_PCT_RANK'],
                                PTS_RANK = regular['PTS_RANK'],
                                STL = regular['STL'],
                                MIN_RANK = regular['MIN_RANK'],
                                L = regular['L'],
                                BLKA = regular['BLKA'],
                                PLAYER_ID = regular['PLAYER_ID'],
                                AST_RANK = regular['AST_RANK'],
                                FTM_RANK = regular['FTM_RANK'],
                                FG3A = regular['FG3A'],
                                CFPARAMS = regular['CFPARAMS'], 

                                DD2_RANK= regular['DD2_RANK'],
                                MIN =regular['MIN'],
                                TOV = regular['TOV'],
                                FGA = regular['FGA'],
                                FG3A_RANK = regular['FG3A_RANK'], 
                                PLUS_MINUS = regular['PLUS_MINUS'],
                                FTA_RANK  =regular['FTA_RANK'],
                                BLK_RANK =regular['BLK_RANK'],
                                W_RANK = regular['W_RANK'],
                                NBA_FANTASY_PTS =regular['NBA_FANTASY_PTS'],
                                REB_RANK = regular['REB_RANK'],
                                AGE =regular['AGE'],
                                TD3_RANK = regular['TD3_RANK'],
                                TD3 =regular['TD3'],
                                PF_RANK =regular['PF_RANK'],
                                L_RANK =regular['L_RANK'],
                                FT_PCT =regular['FT_PCT'],
                                FGA_RANK =regular['FGA_RANK'],
                                REB = regular['REB'],
                                W_PCT =regular['W_PCT'], 
                                NBA_FANTASY_PTS_RANK= regular['NBA_FANTASY_PTS_RANK'], 
                                BLK = regular['BLK'] ,
                                PLUS_MINUS_RANK= regular['PLUS_MINUS_RANK'] ,
                                OREB = regular['OREB'],
                                FGM = regular['FGM'], 
                                FG_PCT = regular['FG_PCT'] , 
                                DREB = regular['DREB'] ,
                                DREB_RANK = regular['DREB_RANK'] ,
                                PF =regular['PF'] , 
                                PTS = regular['PTS'],
                                DD2 = regular['DD2'],
                                AST = regular['AST'],
                                OREB_RANK = regular['OREB_RANK'],
                                W = regular['W'], 
                                CFID = regular['CFID'],
                                PFD_RANK = regular['PFD_RANK'], 
                                FTM =regular['FTM'] , 
                                TOV_RANK = regular['TOV_RANK'] ,
                                FG3_PCT = regular['FG3_PCT'] , 
                                PFD = regular['PFD'] ,
                                W_PCT_RANK = regular['W_PCT_RANK'] , 
                                FG_PCT_RANK =  regular['FG_PCT_RANK'] , 
                                GP_RANK =  regular['GP_RANK'], 
                                FG3_PCT_RANK =  regular['FG3_PCT_RANK'],
                                FGM_RANK =  regular['FGM_RANK'], 
                                BLKA_RANK =  regular['BLKA_RANK'],
                                STL_RANK = regular['STL_RANK']
                                )
                return "All Fine"
        except Exception as e:
                return str(e)
        