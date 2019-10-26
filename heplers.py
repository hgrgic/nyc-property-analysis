# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.metrics import r2_score

models = [
    RandomForestRegressor(n_estimators=200,criterion='mse',max_depth=20,random_state=42),
    DecisionTreeRegressor(criterion='mse',max_depth=11,random_state=42),
    GradientBoostingRegressor(n_estimators=200,max_depth=12)
]
learning_mods = pd.DataFrame()
temp = {}

#run through models
for model in models:
    print(model)
    m = str(model)
    temp['Model'] = m[:m.index('(')]
    model.fit(X_train, y_train)
    temp['R2_Price'] = r2_score(y_test, model.predict(X_test))
    print('score on training',model.score(X_train, y_train))
    print('r2 score',r2_score(y_test, model.predict(X_test)))
    learning_mods = learning_mods.append([temp])
learning_mods.set_index('Model', inplace=True)
 
fig, axes = plt.subplots(ncols=1, figsize=(10, 4))
learning_mods.R2_Price.plot(ax=axes, kind='bar', title='R2_Price')
plt.show()



# Feature importance
treshold = 25

df_feature_importance = pd.DataFrame()
df_feature_importance['features'] = list(property_data)
df_feature_importance['importance'] = rf_2.feature_importances_

df_feature_importance = df_feature_importance.sort_values('importance').tail(treshold)

plt.figure(figsize=(16,4))
plt.yscale('log',nonposy='clip')
plt.bar(range(treshold),df_feature_importance['importance'][:treshold].values[::-1],align='center')

plt.xticks(range(treshold),df_feature_importance['features'][:treshold].values[::-1],rotation='vertical')
plt.title('Feature Importance')
plt.ylabel('Importance')
plt.xlabel('Features')
plt.show()