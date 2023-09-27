#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstoragePermissionModifyModel(object):

    def __init__(self):
        self._env = None
        self._read_permission = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def read_permission(self):
        return self._read_permission

    @read_permission.setter
    def read_permission(self, value):
        self._read_permission = value


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.read_permission:
            if hasattr(self.read_permission, 'to_alipay_dict'):
                params['read_permission'] = self.read_permission.to_alipay_dict()
            else:
                params['read_permission'] = self.read_permission
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstoragePermissionModifyModel()
        if 'env' in d:
            o.env = d['env']
        if 'read_permission' in d:
            o.read_permission = d['read_permission']
        return o


