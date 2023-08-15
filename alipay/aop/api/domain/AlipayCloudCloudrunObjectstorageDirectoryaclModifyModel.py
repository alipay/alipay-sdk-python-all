#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstorageDirectoryaclModifyModel(object):

    def __init__(self):
        self._acl = None
        self._assume_token = None
        self._env = None
        self._file_id = None

    @property
    def acl(self):
        return self._acl

    @acl.setter
    def acl(self, value):
        self._acl = value
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
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acl:
            if hasattr(self.acl, 'to_alipay_dict'):
                params['acl'] = self.acl.to_alipay_dict()
            else:
                params['acl'] = self.acl
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
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstorageDirectoryaclModifyModel()
        if 'acl' in d:
            o.acl = d['acl']
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'env' in d:
            o.env = d['env']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


