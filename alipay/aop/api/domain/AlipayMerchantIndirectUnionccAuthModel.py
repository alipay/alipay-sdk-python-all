#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantIndirectUnionccAuthModel(object):

    def __init__(self):
        self._org_name = None
        self._org_pid = None

    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def org_pid(self):
        return self._org_pid

    @org_pid.setter
    def org_pid(self, value):
        self._org_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.org_pid:
            if hasattr(self.org_pid, 'to_alipay_dict'):
                params['org_pid'] = self.org_pid.to_alipay_dict()
            else:
                params['org_pid'] = self.org_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantIndirectUnionccAuthModel()
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'org_pid' in d:
            o.org_pid = d['org_pid']
        return o


