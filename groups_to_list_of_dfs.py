# split df into multiple dfs based on group

group = df.groupby('A')
dfs = [group.get_group(x) for x in group.groups]
# dfs = [g for _,g in group]

# you can also do

dfs = dict(tuple(df.groupby('A')))

# then call each df by the value in A:

dfs[123]
