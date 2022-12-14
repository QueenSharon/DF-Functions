def downcast(df, verbose=True):​

    size_before = np.round(df.memory_usage().sum()/(1024*1024), 1)​
    cols = df.dtypes.index.tolist()​

    types = df.dtypes.values.tolist()​

    for i,t in enumerate(types):​

        if 'int' in str(t):​

            if df[cols[i]].min() > np.iinfo(np.int8).min and df[cols[i]].max() < np.iinfo(np.int8).max:​

                df[cols[i]] = df[cols[i]].astype(np.int8)​

            elif df[cols[i]].min() > np.iinfo(np.int16).min and df[cols[i]].max() < np.iinfo(np.int16).max:​

                df[cols[i]] = df[cols[i]].astype(np.int16)​

            elif df[cols[i]].min() > np.iinfo(np.int32).min and df[cols[i]].max() < np.iinfo(np.int32).max:​

                df[cols[i]] = df[cols[i]].astype(np.int32)​

            else:​

                df[cols[i]] = df[cols[i]].astype(np.int64)​

        elif 'float' in str(t):​

            if df[cols[i]].min() > np.finfo(np.float16).min and df[cols[i]].max() < np.finfo(np.float16).max:​

                df[cols[i]] = df[cols[i]].astype(np.float16)​

            elif df[cols[i]].min() > np.finfo(np.float32).min and df[cols[i]].max() < np.finfo(np.float32).max:​

                df[cols[i]] = df[cols[i]].astype(np.float32)​

            else:​

                df[cols[i]] = df[cols[i]].astype(np.float64)​

        elif t == np.object:​

            if cols[i] == 'date':​

                df[cols[i]] = pd.to_datetime(df[cols[i]], format='%Y-%m-%d')​

            else:​

                df[cols[i]] = df[cols[i]].astype('category')​

    if verbose:​

        size_after = np.round(df.memory_usage().sum()/(1024*1024), 1)​

        print(f'Size of dataframe before downcasting: {size_before} MB')​

        print(f'Size of dataframe after downcasting: {size_after} MB')​

    return df