#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiQualityTestCloudacptActivityQueryModel(object):

    def __init__(self):
        self._pid = None
        self._uid = None

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiQualityTestCloudacptActivityQueryModel()
        if 'pid' in d:
            o.pid = d['pid']
        if 'uid' in d:
            o.uid = d['uid']
        return o


