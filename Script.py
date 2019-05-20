import os
import seaborn as sns
import matplotlib.pyplot as plt
import math

mnemonics_short = ['1_TssA',
       '2_TssAFlnk',
       '3_TxFlnk',
       '4_Tx' ,
       '5_TxWk',
       '6_EnhG',
       '7_Enh' ,
       '8_ZNF',
       '9_Het',
       '10_TssBiv',
       '11_BivFlnk',
       '12_EnhBiv',
       '13_ReprPC',
       '14_ReprPCWk',
       '15_Quies']   

mnemonics = ['Active_TSS', 'Flanking_Active_TSS', 'gene_5_and_3', 'Strong_transcription', 'Weak_transcription', 'Genic_enhancers', 'Enhancers', 'ZNF_genes_and_repeats', 'Heterochromatin', 'Bivalent_Poised_TSS', 'Bivalent_TSS_Enh', 'Bivalent_Enhancer', 'Repressed_PolyComb', 'Weak_Repressed_PolyComb', 'Quiescent_Low']

roadmap = [
'1.iPSC',
'2.Thymus',
'3.smMuscle',
'4.Neurosh',
'5.Muscle',
'6.Mesench',
'7.Lung',
'8.Heart',
'9.Brain' ]


for x in roadmap:
    for i in range(len(mnemonics_short)):
            ind = 'giggle index -i "'+str(x)+'/bed/*'+str(mnemonics_short[i])+'.bed.gz" -o '+str(x)+'/index_'+str(mnemonics_short[i])+' -s -f' 
            os.system(ind)
            sea = 'giggle search -i '+str(x)+'/index_'+str(mnemonics_short[i])+' -q ' + str(mnemonics[i]) + '_all.bed.gz >> ' + str(mnemonics[i]) +'_search'
            os.system(sea)

            
dic = {}
for x in mnemonics:
    filename = str(x) + '_search'
    d = []
    with open(filename, 'r') as f:
        for i in f.readlines():
            d.append(int(i.split(':')[-1][:-1]))
    dic[str(x)] = d

    
    
# Heatmap

sns.heatmap(list(dic.values()), xticklabels = [], yticklabels = dic.keys())
plt.show()



# Heatmap with log-values

for i in list(dic.values()):
    for x in range(len(i)):
        i[x] = math.log10((i[x]))
        
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(list(dic.values()), xticklabels = [], yticklabels = dic.keys())
plt.show()
