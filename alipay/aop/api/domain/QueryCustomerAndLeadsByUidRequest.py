#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryCustomerAndLeadsByUidRequest(object):

    def __init__(self):
        self._passport_id = None
        self._platform_uid = None

    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def platform_uid(self):
        return self._platform_uid

    @platform_uid.setter
    def platform_uid(self, value):
        self._platform_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.platform_uid:
            if hasattr(self.platform_uid, 'to_alipay_dict'):
                params['platform_uid'] = self.platform_uid.to_alipay_dict()
            else:
                params['platform_uid'] = self.platform_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryCustomerAndLeadsByUidRequest()
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'platform_uid' in d:
            o.platform_uid = d['platform_uid']
        return o


