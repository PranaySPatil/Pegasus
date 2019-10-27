import CassandraHelper
import matplotlib.pyplot as plt
import numpy as np

def visualize_trending_topics(domain, year, k):
    tags = CassandraHelper.get_annual_trend_tag_by_year(domain, year)
    if tags[0].tags:
        all_tags = tags[0].tags.items()
        all_tags = sorted(all_tags, key=lambda x: x[1])
        all_tags.reverse()
        all_tags = all_tags[0:k]

        x_pos = np.arange(len(all_tags))
        plt.bar(x_pos, [x[1] for x in all_tags], align='center', alpha=0.5)
        plt.xticks(x_pos, [x[0] for x in all_tags])
        plt.ylabel('Usage')
        plt.title('Top '+ str(k) +' Topics')

        plt.show()
    else:
        print("No topics found for the given domain and year.")

def visualize_annual_tag_trend(domain, tag):
    years = {2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0}
    for year in years:
        tags = CassandraHelper.get_annual_trend_tag_by_year(domain, year)
        if tags[0].tags.get(tag):
            years[year] = tags[0].tags.get(tag)
    
    years = sorted(years.items() ,  key=lambda x: x[0] )
    x_pos = np.arange(len(years))
    plt.plot(x_pos, [x[1] for x in years])
    plt.xticks(x_pos, [x[0] for x in years])
    plt.ylabel('Usage')
    plt.xlabel('Year')
    plt.title('Topic Trend - ' + tag)

    plt.show()

if __name__ == "__main__":
    domains = CassandraHelper.get_all_domains()
    result_set = []
    for domain in domains.current_rows:
        result_set.append(domain.domain)
    domains = set(result_set)
    print('Available domains: ')
    print('\n'.join(domains))
    while True:
        domain = raw_input("Enter the domain you want to analyze topics in: ").strip()
        option = raw_input("Do you want to see trending tags or tag trent across years? \n1. Get top k trending topics for a year (2015 to 2019)\n2. Get the trend for a topic over years (2015 to 2019)\n").strip()
        if option == '1':
            year = int(raw_input("Enter year: ").strip())
            k = int(raw_input("Enter k: ").strip())
            visualize_trending_topics(domain, year, k)
        if option == '2':
            tag = raw_input("Enter topic to visualize: ").strip()
            visualize_annual_tag_trend(domain, tag)