class Univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype == "O"):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual

    def Univariate(quan,dataset):
        descriptive = pd.DataFrame(index=["Mean","Median","Mode","25%","50%","75%","100%","IQR","1.5*IQR","Q1:25","Q1:50","Q1:75","Q1:100","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"] = dataset[columnName].mean()
            descriptive[columnName]["Median"] = dataset[columnName].median()
            descriptive[columnName]["Mode"] = dataset[columnName].mode()[0]
            descriptive[columnName]["25%"] = dataset.describe()[columnName]["25%"]
            descriptive[columnName]["50%"] = dataset.describe()[columnName]["50%"]
            descriptive[columnName]["75%"] = dataset.describe()[columnName]["75%"]
            descriptive[columnName]["100%"] = dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"] = descriptive[columnName]["75%"] - descriptive[columnName]["25%"]
            descriptive[columnName]["1.5*IQR"] = 1.5 * descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"] = descriptive[columnName]["25%"] - descriptive[columnName]["1.5*IQR"]
            descriptive[columnName]["Greater"] = descriptive[columnName]["75%"] + descriptive[columnName]["1.5*IQR"]
            descriptive[columnName]["Min"] = dataset[columnName].min()
            descriptive[columnName]["Max"] = dataset[columnName].max()
        return descriptive