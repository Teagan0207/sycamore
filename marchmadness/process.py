
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('NCAA_Tourney_2019.csv')


# In[3]:


slot=np.asarray(df['slot'])
for i in range(len(slot)):
    if 'R'==slot[i][0]:
        slot[i]=slot[i][1]
    else:
        slot[i]=0
df['slot']=slot


# In[4]:


df['exp_win1'] = (df['team1_adjoe']**2)/ ((df['team1_adjde']**2)+(df['team1_adjoe']**2))
df['exp_win2'] = (df['team2_adjoe']**2)/ ((df['team2_adjde']**2)+(df['team2_adjoe']**2))
df['exp_win']=df['exp_win1'] -df['exp_win2']


# In[5]:


df['dis1?']=np.sqrt((df['team1_lat']-df['host_lat'])**2+(df['team1_long']-df['host_long'])**2)
df['dis2?']=np.sqrt((df['team2_lat']-df['host_lat'])**2+(df['team2_long']-df['host_long'])**2)
df['distance']=df['dis1?']-df['dis2?']
df['nearer']=(df['dis1?']>df['dis2?']).astype(int)
df['nearer']=df['nearer'].where(df['nearer']!=0,-1)

# In[6]:


df=df.drop(['team1_id','team2_id',#'WLoc',
            'team1_position','team2_position','strongseed','weakseed','team1_teamname','team2_teamname','host','dis1?','dis2?','exp_win1','exp_win2',],axis=1)


# In[7]:


#---------------------------------------------------df['score']=df['team1_score']-df['team2_score']
df['seed']=df['team1_seed']-df['team2_seed']
df['region']=(df['team1_region']==df['team2_region']).astype(int)


# In[8]:


#-----------------------df=df.drop(['team1_score','team2_score','team1_seed','team2_seed','team1_region','team2_region'],axis=1)
df=df.drop(['team1_seed','team2_seed','team1_region','team2_region'],axis=1)

# In[9]:



df['lat']=(df['team1_lat']-df['host_lat']).abs()-(df['team2_lat']-df['host_lat']).abs()
df['long']=(df['team1_long']-df['host_long']).abs()-(df['team2_long']-df['host_long']).abs()


# In[10]:


df=df.drop(['team1_lat','host_lat','team2_lat','team1_long','host_long','team2_long','team1_coach_id','team2_coach_id'],axis=1)


# In[11]:


df['pt_school_ncaa']=df['team1_pt_school_ncaa']-df['team2_pt_school_ncaa']
df['pt_overall_ncaa']=df['team1_pt_overall_ncaa']-df['team2_pt_overall_ncaa']
df['pt_school_s16']=df['team1_pt_school_s16']-df['team2_pt_school_s16']
df['pt_overall_s16']=df['team1_pt_overall_s16']-df['team2_pt_overall_s16']
df['pt_school_ff']=df['team1_pt_school_ff']-df['team2_pt_school_ff']
df['pt_overall_ff']=df['team1_pt_overall_ff']-df['team2_pt_overall_ff']
df['pt_career_school_wins']=df['team1_pt_career_school_wins']-df['team2_pt_career_school_wins']
df['pt_career_school_losses']=df['team1_pt_career_school_losses']-df['team2_pt_career_school_losses']
df['pt_career_overall_wins']=df['team1_pt_career_overall_wins']-df['team2_pt_career_overall_wins']
df['pt_career_overall_losses']=df['team1_pt_career_overall_losses']-df['team2_pt_career_overall_losses']
df['pt_team_season_wins']=df['team1_pt_team_season_wins']-df['team2_pt_team_season_wins']
df['pt_team_season_losses']=df['team1_pt_team_season_losses']-df['team2_pt_team_season_losses']
df['pt_coach_season_wins']=df['team1_pt_coach_season_wins']-df['team2_pt_coach_season_wins']
df['pt_coach_season_losses']=df['team1_pt_coach_season_losses']-df['team2_pt_coach_season_losses']

df['career_school_wins_team1']=df['team1_pt_career_school_wins']/(df['team1_pt_career_school_losses']+df['team1_pt_career_school_wins'])
df['career_school_wins_team2']=df['team2_pt_career_school_wins']/(df['team2_pt_career_school_losses']+df['team2_pt_career_school_wins'])
df['career_overall_wins_team1']=df['team1_pt_career_overall_wins']/(df['team1_pt_career_overall_wins']+df['team1_pt_career_overall_losses'])
df['career_overall_wins_team2']=df['team2_pt_career_overall_wins']/(df['team2_pt_career_overall_wins']+df['team2_pt_career_overall_losses'])
df['team_season_wins_team1']=df['team1_pt_team_season_wins']/(df['team1_pt_team_season_wins']+df['team1_pt_team_season_losses'])
df['team_season_wins_team2']=df['team2_pt_team_season_wins']/(df['team2_pt_team_season_wins']+df['team2_pt_team_season_losses'])
df['coach_season_wins_team1']=df['team1_pt_coach_season_wins']/(df['team1_pt_coach_season_wins']+df['team1_pt_coach_season_losses'])
df['coach_season_wins_team2']=df['team2_pt_coach_season_wins']/(df['team2_pt_coach_season_wins']+df['team2_pt_coach_season_losses'])

df['career_school_wins']=df['career_school_wins_team1']-df['career_school_wins_team2']
df['career_overall_wins']=df['career_overall_wins_team1']-df['career_overall_wins_team2']
df['team_season_wins']=df['team_season_wins_team1']-df['team_season_wins_team2']
df['coach_season_wins']=df['coach_season_wins_team1']-df['coach_season_wins_team2']


# In[12]:


df['overall_ff_ptg']=df['team1_pt_overall_ff']/(df['team1_pt_career_overall_wins']+df['team1_pt_career_overall_losses'])-(df['team2_pt_overall_ff']/(df['team2_pt_career_overall_wins']+df['team2_pt_career_overall_losses']))
df['school_ff_ptg']=df['team1_pt_overall_ff']/(df['team1_pt_career_school_wins']+df['team1_pt_career_school_losses'])-df['team2_pt_overall_ff']/(df['team2_pt_career_school_wins']+df['team2_pt_career_school_losses'])
df['overall_ncaa_ptg']=df['team1_pt_overall_ncaa']/(df['team1_pt_career_overall_wins']+df['team1_pt_career_overall_losses'])-df['team2_pt_overall_ncaa']/(df['team2_pt_career_overall_wins']+df['team2_pt_career_overall_losses'])
df['overall_s16_ptg']=df['team1_pt_school_s16']/(df['team1_pt_career_overall_wins']+df['team1_pt_career_overall_losses'])-df['team2_pt_school_s16']/(df['team2_pt_career_overall_wins']+df['team2_pt_career_overall_losses'])
df['school_ncaa_ptg']=df['team1_pt_school_ncaa']/(df['team1_pt_career_school_wins']+df['team1_pt_career_school_losses'])-df['team2_pt_school_ncaa']/(df['team2_pt_career_school_wins']+df['team2_pt_career_school_losses'])
df['school_s16_ptg']=df['team1_pt_school_s16']/(df['team1_pt_career_school_wins']+df['team1_pt_career_school_losses'])-df['team2_pt_school_s16']/(df['team2_pt_career_school_wins']+df['team2_pt_career_school_losses'])


# In[13]:


df=df.drop(['team1_pt_school_ncaa','team2_pt_school_ncaa','team1_pt_overall_ncaa','team2_pt_overall_ncaa','team1_pt_school_s16','team2_pt_school_s16',
           'team1_pt_overall_s16','team2_pt_overall_s16','team1_pt_school_ff','team2_pt_school_ff','team1_pt_overall_ff','team2_pt_overall_ff',
           'team1_pt_career_school_wins','team2_pt_career_school_wins','team1_pt_career_school_losses','team2_pt_career_school_losses',
           'team1_pt_career_overall_wins','team2_pt_career_overall_wins','team1_pt_career_overall_losses','team2_pt_career_overall_losses',
           'team1_pt_team_season_wins','team2_pt_team_season_wins','team1_pt_team_season_losses','team2_pt_team_season_losses',
           'team1_pt_coach_season_wins','team2_pt_coach_season_wins','team1_pt_coach_season_losses','team2_pt_coach_season_losses',
           'career_school_wins_team1','career_school_wins_team2','career_overall_wins_team1','career_overall_wins_team2',
           'team_season_wins_team2','team_season_wins_team1','coach_season_wins_team1','coach_season_wins_team2'],axis=1)


# In[14]:


df['fg2pct']=df['team1_fg2pct']-df['team2_fg2pct']
df['fg3pct']=df['team1_fg3pct']-df['team2_fg3pct']
df['ftpct']=df['team1_ftpct']-df['team2_ftpct']
df['blockpct']=df['team1_blockpct']-df['team2_blockpct']
df['oppfg2pct']=df['team1_oppfg2pct']-df['team2_oppfg2pct']
df[ 'oppfg3pct']=df[ 'team1_oppfg3pct']-df[ 'team2_oppfg3pct']
df['oppftpct']=df['team1_oppftpct']-df['team2_oppftpct']
df['oppblockpct']=df['team1_oppblockpct']-df['team2_oppblockpct']

df['f3grate']=df['team1_f3grate']-df['team2_f3grate']
df['oppf3grate']=df['team1_oppf3grate']-df['team2_oppf3grate']
df['arate']=df['team1_arate']-df['team2_arate']
df['opparate']=df['team1_opparate']-df['team2_opparate']
df[ 'stlrate']=df[ 'team1_stlrate']-df[ 'team2_stlrate']
df['oppstlrate']=df['team1_oppstlrate']-df['team2_oppstlrate']
df['tempo']=df['team1_tempo']-df['team2_tempo']
df['adjtempo']=df['team1_adjtempo']-df['team2_adjtempo']
df['oe']=df['team1_oe']-df['team2_oe']
df['adjoe']=df['team1_adjoe']-df['team2_adjoe']
df['de']=df['team1_de']-df['team2_de']
df['adjde']=df['team1_adjde']-df['team2_adjde']

df['stlrate_dis']=(df[ 'team1_stlrate']-df['team1_oppstlrate'])-(df[ 'team2_stlrate']-df['team2_oppstlrate'])
df['arate_dis']=(df['team1_arate']-df['team1_opparate'])-(df['team2_arate']-df['team2_opparate'])


df['f3_score']=(df['team1_tempo']+df['team1_adjtempo'])*df['team1_f3grate']*df[ 'team1_fg3pct']-(df['team2_tempo']+df['team2_adjtempo'])*df['team2_f3grate']*df[ 'team2_fg3pct']
df['f3_dis']=(df['team1_f3grate']*df[ 'team1_fg3pct']-df['team1_oppf3grate']*df[ 'team1_oppfg3pct'])-(df['team2_f3grate']*df[ 'team2_fg3pct']-df['team2_oppf3grate']*df[ 'team2_oppfg3pct'])
df['de_score']=df['team1_de']*(df['team1_tempo']+df['team1_adjtempo'])-df['team2_de']*(df['team2_tempo']+df['team2_adjtempo'])
df['oe_score']=df['team1_oe']*(df['team1_tempo']+df['team1_adjtempo'])-df['team2_oe']*(df['team2_tempo']+df['team2_adjtempo'])


df['pctscore_team1']=(2*df['team1_fg2pct']*3.894+3*df['team1_fg3pct']*1.366+df['team1_ftpct']+2*df['team1_oppblockpct']*0.22)*(df['team1_tempo']+df['team1_adjtempo'])
df['pctscore_team2']=(2*df['team2_fg2pct']*3.894+3*df['team2_fg3pct']*1.366+df['team2_ftpct']+2*df['team2_oppblockpct']*0.22)*(df['team2_tempo']+df['team2_adjtempo'])
df['pct_score']=df['pctscore_team1']**5-df['pctscore_team2']**5

df['pctscore_team1_opp']=(2*df['team1_oppfg2pct']*3.894+3*df['team1_oppfg3pct']*1.366+df['team1_oppftpct']+2*df['team1_blockpct']*0.22)*(df['team1_tempo']+df['team1_adjtempo'])
df['pctscore_team2_opp']=(2*df['team2_oppfg2pct']*3.894+3*df['team2_oppfg3pct']*1.366+df['team2_oppftpct']+2*df['team2_blockpct']*0.22)*(df['team2_tempo']+df['team2_adjtempo'])

df['score_dis']=(df['pctscore_team1']-df['pctscore_team1_opp'])-(df['pctscore_team2']-df['pctscore_team2_opp'])


# In[15]:


df=df.drop(['team1_fg2pct','team2_fg2pct','team2_fg3pct','team1_fg3pct','team1_ftpct','team2_ftpct','team1_blockpct','team2_blockpct',
           'team1_oppfg2pct','team2_oppfg2pct','team1_oppfg3pct','team2_oppfg3pct','team1_oppftpct','team2_oppftpct','team1_oppblockpct','team2_oppblockpct',
           'team1_f3grate','team2_f3grate','team1_oppf3grate','team2_oppf3grate','team1_arate','team2_arate','team1_opparate','team2_opparate',
           'team1_stlrate','team2_stlrate','team1_oppstlrate','team2_oppstlrate','team1_tempo','team2_tempo','team1_adjtempo','team2_adjtempo',
           'team1_oe','team2_oe','team1_adjoe','team2_adjoe','team1_de','team2_de','team1_adjde','team2_adjde','pctscore_team1','pctscore_team2','pctscore_team1_opp','pctscore_team1_opp','pctscore_team2_opp',
           'de_score','oe_score'],axis=1)


# In[16]:


df.columns


# In[17]:


df.isnull().any()


# In[18]:


df.columns


# In[19]:


df=df.fillna(26)


# In[20]:


df['ap_final']=df['team1_ap_final']-df['team2_ap_final']
df['ap_preseason']=df['team1_ap_preseason']-df['team2_ap_preseason']
df['coaches_before_final']=df['team1_coaches_before_final']-df['team2_coaches_before_final']
df['coaches_preseason']=df['team1_coaches_preseason']-df['team2_coaches_preseason']

df['ap_progress']=df['team1_ap_final']-df['team1_ap_preseason']-(df['team2_ap_final']-df['team2_ap_preseason'])
df['coaches_progress']=df['team1_coaches_before_final']-df['team1_coaches_preseason']-(df['team2_coaches_before_final']-df['team2_coaches_preseason'])


# In[21]:


a=['team1_ap_final','team1_ap_preseason','team1_coaches_before_final','team1_coaches_preseason', 'team2_ap_final','team2_ap_preseason','team2_coaches_before_final','team2_coaches_preseason']
subdf=df[['team1_ap_final','team1_ap_preseason','team1_coaches_before_final','team1_coaches_preseason', 'team2_ap_final','team2_ap_preseason','team2_coaches_before_final','team2_coaches_preseason']]
     # a行大于0的列
sub=(df[a]!=26).astype(int)
df['ex_ap_final']=sub['team1_ap_final']-sub['team2_ap_final']
df['ex_ap_preseason']=sub['team1_ap_preseason']-sub['team2_ap_preseason']
df['ex_coaches_before_final']=sub['team1_coaches_before_final']-sub['team2_coaches_before_final']
df['ex_coaches_preseason']=sub['team1_coaches_preseason']-sub['team2_coaches_preseason']
df=df.drop(['team1_coaches_preseason','team2_coaches_preseason','team1_coaches_before_final','team2_coaches_before_final',
        'team1_ap_preseason','team2_ap_preseason','team1_ap_final','team2_ap_final'],axis=1)


# In[22]:


df=df.drop(['season','game_id'],axis=1)


# In[23]:


#df=pd.get_dummies(df, prefix=['slot'], columns=['slot'])


# In[24]:


#---------------------------df['result']=(df['score']>0).astype(int)
df.to_csv('processed-test.csv')


# In[25]:


df.columns


# In[ ]:




