from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load and preprocess
dataset = CompasDataset()
privileged_groups = [{'race': 1}]  # Caucasian
unprivileged_groups = [{'race': 0}]  # African-American

# Original bias metrics
metric = BinaryLabelDatasetMetric(dataset, unprivileged_groups, privileged_groups)
print("Difference in positive outcome rate:", metric.mean_difference())

# Reweighing to mitigate bias
RW = Reweighing(unprivileged_groups=unprivileged_groups,
                privileged_groups=privileged_groups)
dataset_transf = RW.fit_transform(dataset)

# Train model
X = dataset_transf.features
y = dataset_transf.labels.ravel()
model = LogisticRegression()
model.fit(X, y)

# Evaluate bias post-training
classified_metric = ClassificationMetric(dataset_transf, dataset_transf,
                                         unprivileged_groups=unprivileged_groups,
                                         privileged_groups=privileged_groups)
print("Disparate Impact:", classified_metric.disparate_impact())
