#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInstserviceContractdeductSignModel(object):

    def __init__(self):
        self._bill_key = None
        self._user_id = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInstserviceContractdeductSignModel()
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


