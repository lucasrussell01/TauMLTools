total = 250*n_batches

average_outer_hadron = outer_hadron_sum/total
average2_outer_hadron = outer_hadron_sum2/total
std_outer_hadron = np.sqrt(average2_outer_hadron - average_outer_hadron**2)


outer_hadron_stats = pd.DataFrame(hadron_feats, columns = ["outer hadron Feature"])
outer_hadron_stats["Avg"] = average_outer_hadron
outer_hadron_stats["Avg of ^2"]= average2_outer_hadron
outer_hadron_stats["Stand. Dev."] = std_outer_hadron
outer_hadron_stats["Max"] = outer_hadron_max
outer_hadron_stats["Min"] = outer_hadron_min

print(outer_hadron_stats)

outer_hadron_stats.to_csv('./outer_hadron_stats.csv', index=True)