#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdAuthInfo import CrowdAuthInfo
from alipay.aop.api.domain.CrowdOperations import CrowdOperations
from alipay.aop.api.domain.CrowdTarget import CrowdTarget


class SyncCrowdInfo(object):

    def __init__(self):
        self._auth_info = None
        self._operations = None
        self._target = None

    @property
    def auth_info(self):
        return self._auth_info

    @auth_info.setter
    def auth_info(self, value):
        if isinstance(value, CrowdAuthInfo):
            self._auth_info = value
        else:
            self._auth_info = CrowdAuthInfo.from_alipay_dict(value)
    @property
    def operations(self):
        return self._operations

    @operations.setter
    def operations(self, value):
        if isinstance(value, list):
            self._operations = list()
            for i in value:
                if isinstance(i, CrowdOperations):
                    self._operations.append(i)
                else:
                    self._operations.append(CrowdOperations.from_alipay_dict(i))
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if isinstance(value, CrowdTarget):
            self._target = value
        else:
            self._target = CrowdTarget.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.auth_info:
            if hasattr(self.auth_info, 'to_alipay_dict'):
                params['auth_info'] = self.auth_info.to_alipay_dict()
            else:
                params['auth_info'] = self.auth_info
        if self.operations:
            if isinstance(self.operations, list):
                for i in range(0, len(self.operations)):
                    element = self.operations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operations[i] = element.to_alipay_dict()
            if hasattr(self.operations, 'to_alipay_dict'):
                params['operations'] = self.operations.to_alipay_dict()
            else:
                params['operations'] = self.operations
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SyncCrowdInfo()
        if 'auth_info' in d:
            o.auth_info = d['auth_info']
        if 'operations' in d:
            o.operations = d['operations']
        if 'target' in d:
            o.target = d['target']
        return o


