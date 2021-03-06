import pytest

import numpy as np
from collections import OrderedDict

from torchmeta.transforms.splitters import ClassSplitter
from torchmeta.toy import Sinusoid


def test_seed_class_splitter():
    dataset_transform = ClassSplitter(shuffle=True,
        num_train_per_class=5, num_test_per_class=5)
    dataset = Sinusoid(10, num_tasks=1000, noise_std=0.1,
        dataset_transform=dataset_transform)
    dataset.seed(1)

    expected_train_inputs = np.array([1.08565437,-1.56211897,4.62078213,-2.03870077,0.76977846])
    expected_train_targets = np.array([-0.00309463,-1.37650356,-0.9346262,-0.1031986,-0.4698061])

    expected_test_inputs = np.array([-2.48340416,3.75388738,-3.15504396,0.09898378,0.32922559])
    expected_test_targets = np.array([0.73113509,0.91773121,1.86656819,-1.61885041,-1.52508997])

    task = dataset[0]
    train_dataset, test_dataset = task['train'], task['test']

    assert len(train_dataset) == 5
    assert len(test_dataset) == 5

    for i, (train_input, train_target) in enumerate(train_dataset):
        assert np.isclose(train_input, expected_train_inputs[i])
        assert np.isclose(train_target, expected_train_targets[i])

    for i, (test_input, test_target) in enumerate(test_dataset):
        assert np.isclose(test_input, expected_test_inputs[i])
        assert np.isclose(test_target, expected_test_targets[i])
