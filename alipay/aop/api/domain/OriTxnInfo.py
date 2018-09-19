#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OriTxnInfo(object):

    def __init__(self):
        self._category_type = None
        self._category_value = None
        self._txn_info = None

    @property
    def category_type(self):
        return self._category_type

    @category_type.setter
    def category_type(self, value):
        self._category_type = value
    @property
    def category_value(self):
        return self._category_value

    @category_value.setter
    def category_value(self, value):
        self._category_value = value
    @property
    def txn_info(self):
        return self._txn_info

    @txn_info.setter
    def txn_info(self, value):
        self._txn_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_type:
            if hasattr(self.category_type, 'to_alipay_dict'):
                params['category_type'] = self.category_type.to_alipay_dict()
            else:
                params['category_type'] = self.category_type
        if self.category_value:
            if hasattr(self.category_value, 'to_alipay_dict'):
                params['category_value'] = self.category_value.to_alipay_dict()
            else:
                params['category_value'] = self.category_value
        if self.txn_info:
            if hasattr(self.txn_info, 'to_alipay_dict'):
                params['txn_info'] = self.txn_info.to_alipay_dict()
            else:
                params['txn_info'] = self.txn_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OriTxnInfo()
        if 'category_type' in d:
            o.category_type = d['category_type']
        if 'category_value' in d:
            o.category_value = d['category_value']
        if 'txn_info' in d:
            o.txn_info = d['txn_info']
        return o


