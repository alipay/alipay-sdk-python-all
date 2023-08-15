#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstorageDirectoryDeleteModel(object):

    def __init__(self):
        self._assume_token = None
        self._env = None
        self._file_id_list = None

    @property
    def assume_token(self):
        return self._assume_token

    @assume_token.setter
    def assume_token(self, value):
        self._assume_token = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def file_id_list(self):
        return self._file_id_list

    @file_id_list.setter
    def file_id_list(self, value):
        if isinstance(value, list):
            self._file_id_list = list()
            for i in value:
                self._file_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.assume_token:
            if hasattr(self.assume_token, 'to_alipay_dict'):
                params['assume_token'] = self.assume_token.to_alipay_dict()
            else:
                params['assume_token'] = self.assume_token
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.file_id_list:
            if isinstance(self.file_id_list, list):
                for i in range(0, len(self.file_id_list)):
                    element = self.file_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_id_list[i] = element.to_alipay_dict()
            if hasattr(self.file_id_list, 'to_alipay_dict'):
                params['file_id_list'] = self.file_id_list.to_alipay_dict()
            else:
                params['file_id_list'] = self.file_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstorageDirectoryDeleteModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'env' in d:
            o.env = d['env']
        if 'file_id_list' in d:
            o.file_id_list = d['file_id_list']
        return o


