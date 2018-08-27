#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosOrderKey(object):

    def __init__(self):
        self._dv_sn = None
        self._merchant_id = None
        self._order_version = None
        self._out_biz_no = None

    @property
    def dv_sn(self):
        return self._dv_sn

    @dv_sn.setter
    def dv_sn(self, value):
        self._dv_sn = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def order_version(self):
        return self._order_version

    @order_version.setter
    def order_version(self, value):
        self._order_version = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.dv_sn:
            if hasattr(self.dv_sn, 'to_alipay_dict'):
                params['dv_sn'] = self.dv_sn.to_alipay_dict()
            else:
                params['dv_sn'] = self.dv_sn
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.order_version:
            if hasattr(self.order_version, 'to_alipay_dict'):
                params['order_version'] = self.order_version.to_alipay_dict()
            else:
                params['order_version'] = self.order_version
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosOrderKey()
        if 'dv_sn' in d:
            o.dv_sn = d['dv_sn']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'order_version' in d:
            o.order_version = d['order_version']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


