#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# Download and build the data if it does not exist.

import os

from parlai.core import build_data


TASK_FOLDER_NAME = 'style_gen'
STYLE_LABELED_DATASETS_RESOURCES = [
    build_data.DownloadableFile(
        'http://parl.ai/downloads/style_gen/style_labeled_datasets.tar.gz',
        'style_labeled_datasets.tar.gz',
        'ADD THIS',
    )
]
PERSONALITY_LIST_RESOURCES = [
    build_data.DownloadableFile(
        'http://parl.ai/downloads/style_gen/personality_list.txt',
        'personality_list.txt',
        'ADD THIS',
        zipped=False,
    )
]


def build_style_labeled_datasets(opt):
    dpath = os.path.join(opt['datapath'], TASK_FOLDER_NAME)
    version = 'v1.0'

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data
        for downloadable_file in STYLE_LABELED_DATASETS_RESOURCES:
            downloadable_file.download_file(dpath)

        # Mark the data as built
        build_data.mark_done(dpath, version_string=version)


def build_personality_list(opt):
    dpath = os.path.join(opt['datapath'], TASK_FOLDER_NAME)
    version = 'v1.0'

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data
        for downloadable_file in PERSONALITY_LIST_RESOURCES:
            downloadable_file.download_file(dpath)

        # Mark the data as built
        build_data.mark_done(dpath, version_string=version)
