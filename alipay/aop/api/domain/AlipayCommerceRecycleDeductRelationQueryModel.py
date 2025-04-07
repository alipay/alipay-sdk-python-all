#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleDeductRelationQueryModel(object):

    def __init__(self):
        self._second_merchant_open_id = None
        self._second_merchant_pid = None

    @property
    def second_merchant_open_id(self):
        return self._second_merchant_open_id

    @second_merchant_open_id.setter
    def second_merchant_open_id(self, value):
        self._second_merchant_open_id = value
    @property
    def second_merchant_pid(self):
        return self._second_merchant_pid

    @second_merchant_pid.setter
    def second_merchant_pid(self, value):
        self._second_merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.second_merchant_open_id:
            if hasattr(self.second_merchant_open_id, 'to_alipay_dict'):
                params['second_merchant_open_id'] = self.second_merchant_open_id.to_alipay_dict()
            else:
                params['second_merchant_open_id'] = self.second_merchant_open_id
        if self.second_merchant_pid:
            if hasattr(self.second_merchant_pid, 'to_alipay_dict'):
                params['second_merchant_pid'] = self.second_merchant_pid.to_alipay_dict()
            else:
                params['second_merchant_pid'] = self.second_merchant_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleDeductRelationQueryModel()
        if 'second_merchant_open_id' in d:
            o.second_merchant_open_id = d['second_merchant_open_id']
        if 'second_merchant_pid' in d:
            o.second_merchant_pid = d['second_merchant_pid']
        return o


