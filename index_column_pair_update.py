# find (index, col) pair where a condtion is met then update column values to column name

# sample data
df = pd.DataFrame({'cat_list':list('ABCDE'),
                   'col2':[0]*5,
                   'col2':[0,0,1,0,1],
                   'col3':[1,1,0,0,0],
                   'col4':[0,0,0,1,0]})

# index,col values where df==1
new = pd.DataFrame(list(df[df ==1 ].stack().index)).set_index(0).rename(columns={1:'cat_list'})
df.update(new)
