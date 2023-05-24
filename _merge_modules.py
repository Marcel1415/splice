# detect outliers
def find_outliers_IQR(df):
    
    q1=df.quantile(0.3)

    q3=df.quantile(1)

    IQR=q3-q1

    # for lower and upper outliers
#     outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
    
    # for only lower outliers
    outliers = df[(df<(q1-1.5*IQR))]
    
    return outliers

# drop outliers
def drop_outliers_IQR(df):

    q1=df.quantile(0.3)

    q3=df.quantile(1)

    IQR=q3-q1

    # as above
#     not_outliers = df[~((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
    
    # as above
    not_outliers = df[~(df<(q1-1.5*IQR))]
    
    outliers_dropped = not_outliers.dropna()#.reset_index()
    
    return outliers_dropped