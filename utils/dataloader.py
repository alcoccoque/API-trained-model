import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder


class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()


    def load_data(self):
        # columns combination


        # Replace value
        self.dataset.loc[self.dataset['country'] == 'US', 'usd_pledged_real'] = self.dataset['usd pledged']

        # replace with most common value
        self.dataset['country'] = self.dataset['country'].replace(['N,0"'], 'US')

        # Drop columns
        self.dataset.drop(['goal'], axis=1, inplace=True)
        self.dataset.drop(['pledged'], axis=1, inplace=True)
        self.dataset.drop(['ID'], axis=1, inplace=True)
        self.dataset.drop(['name'], axis=1, inplace=True)
        self.dataset.drop(['usd pledged'], axis=1, inplace=True)
        self.dataset.drop(['currency'], axis=1, inplace=True)
        self.dataset.drop(['category'], axis=1, inplace=True)
        self.dataset.drop(['deadline'], axis=1, inplace=True)
        self.dataset.drop(['launched'], axis=1, inplace=True)

        # # Keep only successful and failed
        # self.dataset = self.dataset[self.dataset['state'].isin(['failed', 'successful'])]

        # # Removing highest 2 percentiles of dataset:
        # self.dataset = self.dataset[self.dataset['backers'] < np.quantile(self.dataset['backers'], 0.98)]
        #
        # # Removing bottom and top 1 percentiles:
        # df = self.dataset[
        #     (self.dataset['usd_pledged_real'] > np.quantile(self.dataset['usd_pledged_real'], 0.01)) &
        #     (self.dataset['usd_pledged_real'] < np.quantile(self.dataset['usd_pledged_real'], 0.99))]

        # Encodning labels
        le = LabelEncoder()

        le.fit(self.dataset['main_category'])
        self.dataset['main_category'] = le.transform(self.dataset['main_category'])

        le.fit(self.dataset['country'].values)
        self.dataset['country'] = le.transform(self.dataset['country'].values)

        return self.dataset