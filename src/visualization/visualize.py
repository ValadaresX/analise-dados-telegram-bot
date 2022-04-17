import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def barv_npsmean_by(dataframe, axisX):
    axisX_labels = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].index
    nps_mean_by_axisX = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].values

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.bar(axisX_labels, nps_mean_by_axisX)
    ax.set_ylabel("NPS interno mensal médio")
    ax.set_yticks(np.array(range(0,11,1)))
    ax.set_title(f"Média de NPS Interno Mensal por {axisX}")
    fig.savefig('grapg_last_generated.png')
    return plt.close(fig)

def his_nps(dataframe):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hist(dataframe["NPS interno"])
    ax.set_title("Distribuição do NPS interno Mensal")
    ax.set_xlabel("NPS interno")
    fig.savefig('grapg_last_generated.png')
    return plt.close(fig)

