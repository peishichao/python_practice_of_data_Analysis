#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd
inputfile = '../data/consumption_data.xls'
outputfile = '../tmp/data_type.xls'
data = pd.read_excel(inputfile,index_col='Id')
k =3
def jobs():

    iteration = 500
    data_zs = 1.0*(data-data.mean())/data.std()
    from sklearn.cluster import KMeans

    model = KMeans(n_clusters=k,n_jobs=4,max_iter = iteration)
    model.fit(data_zs)
    r1 = pd.Series(model.labels_).value_counts()#统计各个类别的数目
    r2 = pd.DataFrame(model.cluster_centers_)#找出聚类的中心

    r = pd.concat([r2,r1],axis=1)#横向连接，得到聚类中心对应的类别下得数目

    r.columns = list(data.columns) + [u'类别数目']#重命名表头

    print(r)

    r = pd.concat([data,pd.Series(model.labels_,index = data.index)],axis = 1)

    #r.columns = list(data.columns) + [u'聚类类别']
    print (r)
    r.to_excel(outputfile)

def density_plot(data,title):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure()
    for i in range(len(data.iloc[0])):
        (data.iloc[:,i].plot(kind='kde',label = data.columns[i],linewidth = 2))
    plt.ylabel(u'密度')
    plt.xlabel(u'人数')
    plt.title(u'聚类类别%s个属性的密度曲线' %title)

    plt.legend()
    return plt

def density_plot_(data):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    p = data.plot(kind = 'kde',linewidth = 2,subplots = True, sharex = False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend()
    return plt

if __name__ == '__main__':
    #jobs()
    iteration = 500
    data_zs = 1.0 * (data - data.mean()) / data.std()
    from sklearn.cluster import KMeans

    model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
    model.fit(data_zs)
    r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类的中心

    r = pd.concat([r2, r1], axis=1)  # 横向连接，得到聚类中心对应的类别下得数目

    r.columns = list(data.columns) + [u'类别数目']  # 重命名表头

    print(r)

    r = pd.concat([data, pd.Series(model.labels_, index=data.index)],axis = 1)

    r.columns = list(data.columns) + [u'聚类类别']
    print (r)
    r.to_excel(outputfile)
    pic_output = '../tmp/pd_'
    for i in range(k):
        density_plot_(data[r[u'聚类类别'] == i]).savefig(u'%s%s.png' %(pic_output,i))