            import pandas as pd
            from sklearn.metrics import mean_absolute_error
            from sklearn.tree import DecisionTreeRegressor

            def max_mae(max_leaf_nodes, trainx, testx, trainy, testy):
                modal = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 0)
                modal.fit(trainx, trainy)
                prediction = modal.predict(testx)
                mae = mean_absolute_error(testy, prediction)
                return mae

            filePath = input("Enter file path: ")
            data = pd.read_csv(filePath)
            data.dropna(axis=0)
            y = data.Price
            features = list(map(str, input("Enter space seperated inputs: ").split()))
            X = data[features]
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
            maeModal = {}
            rangee = int(input("Enter testing range [2:?]: "))
            for i in range(2, rangee+1):
                maeModal[i] = int(max_mae(i, X_train, X_test, y_train, y_test))
                print(i, "done with approx mean absolute error: ", maeModal[i])
            print("Minimum MAE:",min(maeModal.values()))
            print("Minimum or best number of 'Max leaf nodes':",list(maeModal.keys())[list(maeModal.values()).index(min(maeModal.values()))])
            while True:
                cho = int(input("Choose a number from 1 to 500(to check the MAE): "))
                print(maeModal[cho])