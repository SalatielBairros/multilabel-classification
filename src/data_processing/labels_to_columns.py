import pandas as pd

class LabelsToColumns:
    """
    Class to convert labels to columns
    """
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def execute(self) -> pd.DataFrame:
        labels = {}
        for tag in self.dataset['Tags'].unique():
            tags = tag.split(' ')
            for tag in tags:
                if(tag not in labels):
                    labels[tag] = []

        self.dataset['array_tags'] = self.dataset['Tags'].str.split(' ')
        for tags in self.dataset['array_tags']:
            for label in labels:
                if(label in tags):
                    labels[label].append(1)
                else:
                    labels[label].append(0)
        
        tag_labels = []
        for tag in labels:
            self.dataset[tag] = labels[tag]
            tag_labels.append(labels[tag])

        self.dataset['all_tags'] = list(zip(*tag_labels))

        self.dataset = self.dataset.drop(columns=['array_tags'])
        return self.dataset