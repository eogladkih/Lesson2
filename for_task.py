from statistics import mean

asseeement=[
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '5a', 'scores': [5,5,3,4,4,5,2]},
{'school_class': '6a', 'scores': [3,3,3,3,4,5,]},
{'school_class': '7a', 'scores': [4,5,3,5,5]}
]


SUMM=0
Total_children=0


for a in asseeement:
    SUMM = SUMM + sum(a['scores'])
    Total_children=Total_children + len(a['scores'])
print("Средний балл по школе: " + str(SUMM/Total_children))


for a in asseeement:

    print("Средний балл в классе: " + (a['school_class']) +" - " + str(mean(a['scores'])))

