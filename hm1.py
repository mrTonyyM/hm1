teamScore = {'?' : {'play' : '0', 'win' : '0', 'draw' : '0', 'lose' : '0', 'score' : '0'}}

def create_teamScore(ls):
    i_ls = ls.split(';')
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

