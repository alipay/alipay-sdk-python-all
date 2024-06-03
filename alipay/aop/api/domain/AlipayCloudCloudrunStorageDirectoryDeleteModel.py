#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunStorageDirectoryDeleteModel(object):

    def __init__(self):
        self._dir_name = None
        self._env = None
        self._path = None

    @property
    def dir_name(self):
        return self._dir_name

    @dir_name.setter
    def dir_name(self, value):
        self._dir_name = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value


    def to_alipay_dict(self):
        params = dict()
        if self.dir_name:
            if hasattr(self.dir_name, 'to_alipay_dict'):
                params['dir_name'] = self.dir_name.to_alipay_dict()
            else:
                params['dir_name'] = self.dir_name
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunStorageDirectoryDeleteModel()
        if 'dir_name' in d:
            o.dir_name = d['dir_name']
        if 'env' in d:
            o.env = d['env']
        if 'path' in d:
            o.path = d['path']
        return o


