teamScore = {}
def create_teamScore(ls):
    i_ls = ls.split(';')
    if i_ls[0] not in teamScore:
        teamScore[i_ls[0]] = {'play' : 0, 'win' : 0, 'draw' : 0, 'lose' : 0, 'score' : 0}

    if i_ls[2] not in teamScore:
        teamScore[i_ls[2]] = {'play': 0, 'win': 0, 'draw': 0, 'lose': 0, 'score': 0}
    teamScore[i_ls[0]]['play'] += 1
    teamScore[i_ls[2]]['play'] += 1
    if i_ls[1] == i_ls[3]:
        teamScore[i_ls[0]]['draw'] += 1
        teamScore[i_ls[2]]['draw'] += 1
    elif i_ls[1] > i_ls[3]:
        teamScore[i_ls[0]]['win'] += 1
        teamScore[i_ls[2]]['lose'] += 1
    else:
        teamScore[i_ls[2]]['win'] += 1
        teamScore[i_ls[0]]['lose'] += 1

    teamScore[i_ls[0]]['score'] = teamScore[i_ls[0]]['win']*3 + teamScore[i_ls[0]]['draw']
    teamScore[i_ls[2]]['score'] = teamScore[i_ls[2]]['win']*3 + teamScore[i_ls[2]]['draw']
n_plays = int(input())

for i in range(n_plays):
    ls = input()
    create_teamScore(ls)
for key in teamScore:
    print(key+':'+str(teamScore[key]['play'])+' '+str(teamScore[key]['win'])+' '+str(teamScore[key]['draw'])+' '+str(teamScore[key]['lose'])+' '+str(teamScore[key]['score']))
# ls_teams = []
# ls_teams += input().split(';')
# ls2_teams = []
# for l in range(0,len(ls_teams),2):
#     ls2_teams += [ls_teams[l]]
# key_teams = set(ls2_teams)
# print(key_teams)
# dic_ls_teams = {}
