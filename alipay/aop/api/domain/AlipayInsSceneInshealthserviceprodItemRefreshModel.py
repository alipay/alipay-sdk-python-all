#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInshealthserviceprodItemRefreshModel(object):

    def __init__(self):
        self._ant_ser_prod_no = None
        self._merchant_item_code = None
        self._refresh_type = None

    @property
    def ant_ser_prod_no(self):
        return self._ant_ser_prod_no

    @ant_ser_prod_no.setter
    def ant_ser_prod_no(self, value):
        self._ant_ser_prod_no = value
    @property
    def merchant_item_code(self):
        return self._merchant_item_code

    @merchant_item_code.setter
    def merchant_item_code(self, value):
        self._merchant_item_code = value
    @property
    def refresh_type(self):
        return self._refresh_type

    @refresh_type.setter
    def refresh_type(self, value):
        self._refresh_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_prod_no:
            if hasattr(self.ant_ser_prod_no, 'to_alipay_dict'):
                params['ant_ser_prod_no'] = self.ant_ser_prod_no.to_alipay_dict()
            else:
                params['ant_ser_prod_no'] = self.ant_ser_prod_no
        if self.merchant_item_code:
            if hasattr(self.merchant_item_code, 'to_alipay_dict'):
                params['merchant_item_code'] = self.merchant_item_code.to_alipay_dict()
            else:
                params['merchant_item_code'] = self.merchant_item_code
        if self.refresh_type:
            if hasattr(self.refresh_type, 'to_alipay_dict'):
                params['refresh_type'] = self.refresh_type.to_alipay_dict()
            else:
                params['refresh_type'] = self.refresh_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInshealthserviceprodItemRefreshModel()
        if 'ant_ser_prod_no' in d:
            o.ant_ser_prod_no = d['ant_ser_prod_no']
        if 'merchant_item_code' in d:
            o.merchant_item_code = d['merchant_item_code']
        if 'refresh_type' in d:
            o.refresh_type = d['refresh_type']
        return o


