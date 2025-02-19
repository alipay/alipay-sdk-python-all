#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistSrcfgestagelendOutordermappingSyncModel(object):

    def __init__(self):
        self._credit_apply_no = None
        self._ip_id = None
        self._out_order_no = None
        self._prod_code = None

    @property
    def credit_apply_no(self):
        return self._credit_apply_no

    @credit_apply_no.setter
    def credit_apply_no(self, value):
        self._credit_apply_no = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_apply_no:
            if hasattr(self.credit_apply_no, 'to_alipay_dict'):
                params['credit_apply_no'] = self.credit_apply_no.to_alipay_dict()
            else:
                params['credit_apply_no'] = self.credit_apply_no
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistSrcfgestagelendOutordermappingSyncModel()
        if 'credit_apply_no' in d:
            o.credit_apply_no = d['credit_apply_no']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        return o


