#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillEreceiptApplyModel(object):

    def __init__(self):
        self._bill_user_id = None
        self._key = None
        self._type = None

    @property
    def bill_user_id(self):
        return self._bill_user_id

    @bill_user_id.setter
    def bill_user_id(self, value):
        self._bill_user_id = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_user_id:
            if hasattr(self.bill_user_id, 'to_alipay_dict'):
                params['bill_user_id'] = self.bill_user_id.to_alipay_dict()
            else:
                params['bill_user_id'] = self.bill_user_id
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillEreceiptApplyModel()
        if 'bill_user_id' in d:
            o.bill_user_id = d['bill_user_id']
        if 'key' in d:
            o.key = d['key']
        if 'type' in d:
            o.type = d['type']
        return o


