#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DownloadUrlRequest import DownloadUrlRequest


class AlipayCloudCloudrunObjectstorageDownloadurlGetModel(object):

    def __init__(self):
        self._assume_token = None
        self._env = None
        self._file_list = None

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
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, DownloadUrlRequest):
                    self._file_list.append(i)
                else:
                    self._file_list.append(DownloadUrlRequest.from_alipay_dict(i))


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
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstorageDownloadurlGetModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'env' in d:
            o.env = d['env']
        if 'file_list' in d:
            o.file_list = d['file_list']
        return o


