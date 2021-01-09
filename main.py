import pandas 
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import random 
import statistics as stat

df = pandas.read_csv("medium_data.csv")
data = list(df["reading_time"])
pop_mean = stat.mean(data)
pop_dev = stat.stdev(data)
print("Population Mean = "+str(pop_mean))
print("Population Standard Deviation = "+str(pop_dev))

def show_graph(dataframe,title,mean):
    fig = ff.create_distplot([dataframe],[title],show_hist=False)
    fig.show()

def sample(n):
    dataset=[]
    for i in range(0,n):
        res = random.randint(0,len(data)-1)
        dataset.append(data[res])
    m = stat.mean(dataset)
    return m

def setup():
    new_data = []
    for i in range(1000):
        m = sample(1000)
        new_data.append(m)
    print("Sample mean = "+str(stat.mean(new_data)))
    print("Sample standard deviation = "+str(stat.stdev(new_data)))
    show_graph(new_data,"Average Reading Time",stat.mean(new_data))

setup()