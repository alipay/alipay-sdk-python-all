#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflinePaysaasOrderCancelModel(object):

    def __init__(self):
        self._biz_tid = None
        self._isv_out_order_no = None
        self._merchant_type = None
        self._sn = None
        self._supplier_id = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def isv_out_order_no(self):
        return self._isv_out_order_no

    @isv_out_order_no.setter
    def isv_out_order_no(self, value):
        self._isv_out_order_no = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.isv_out_order_no:
            if hasattr(self.isv_out_order_no, 'to_alipay_dict'):
                params['isv_out_order_no'] = self.isv_out_order_no.to_alipay_dict()
            else:
                params['isv_out_order_no'] = self.isv_out_order_no
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflinePaysaasOrderCancelModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'isv_out_order_no' in d:
            o.isv_out_order_no = d['isv_out_order_no']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


