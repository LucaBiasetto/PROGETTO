
import axelrod as axl
from icecream import ic
import pprint
import csv
import matplotlib.pyplot as plt
"""
players=[axl.Cooperator(),axl.Alternator()]
match=axl.Match(players=players,turns=5,noise=0.1)
ic(match.play())
ic((match.sparklines(c_symbol='🤝 ', d_symbol='❌ ')))
ic(match.scores())
ic(match.final_score())
ic(match.final_score_per_turn())
ic(match.winner())
ic(match.cooperation())  # The count of cooperations
ic(match.normalised_cooperation())  # The count of cooperations per turn

"""
'''
players2=[axl.Alternator(),axl.TitForTat(),axl.RandomTitForTat(),axl.Random(),axl.Cooperator(),axl.AdaptiveTitForTat()]
tournament=axl.Tournament(players=players2,noise=0.1,prob_end=0.15,turns=20)
results=tournament.play()



plot = axl.Plot(results)
p = plot.boxplot()
p2 = plot.winplot()
p3 = plot.payoff()

#The axelrod.Plot class has a method: save_all_plots that will save all the above plots to file.
axl.Plot.save_all_plots(self=plot)
p.show()
p2.show()
p3.show()
""""
import matplotlib.pyplot as plt
_, ax = plt.subplots()
title = ax.set_title('Payoff')
xlabel = ax.set_xlabel('Strategies')
p = plot.boxplot(ax=ax)
p.show()
plt.savefig()
"""



summary = results.summarise()
#pprint.pprint(summary)


results.write_summary('summary.csv')
with open('summary.csv', 'r') as outfile:
    csvreader = csv.reader(outfile)
    for row in csvreader:
        print(row)
"""
ic(results.scores)
ic(results.payoff_matrix)
ic(results.ranking)
ic(results.ranked_names)
ic(results.progress_bar)
ic(results.wins)                           

"""
'''
players33 = [s() for s in axl.basic_strategies]
tournament = axl.Tournament(players33, turns=4, repetitions=2)
results = tournament.play(filename="basic_tournament.csv")

interactions = axl.interaction_utils.read_interactions_from_file("basic_tournament.csv")
interactions[(0, 1)]
#This should allow for easy manipulation of data outside of the capabilities within the library.


#continuo moran process




