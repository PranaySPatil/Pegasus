import CassandraHelper
import matplotlib.pyplot as plt

def visualize_annual_tag_trend(domain, tag):
    years = {2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0}
    for year in years:
        tags = CassandraHelper.get_annual_trend_tag_by_year(domain, year)
        if tags[0].tags.get(tag):
            years[year] = tags[0].tags.get(tag)
    
    years = sorted(years.items() ,  key=lambda x: x[0] )
    plt.plot([x[0] for x in years], [x[1] for x in years])
    plt.show()

visualize_annual_tag_trend("askubuntu", "software-recommendation")