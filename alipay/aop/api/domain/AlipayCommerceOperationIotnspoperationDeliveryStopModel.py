#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationIotnspoperationDeliveryStopModel(object):

    def __init__(self):
        self._merchant_access_mode = None
        self._n_delivery_id = None
        self._out_biz_no = None

    @property
    def merchant_access_mode(self):
        return self._merchant_access_mode

    @merchant_access_mode.setter
    def merchant_access_mode(self, value):
        self._merchant_access_mode = value
    @property
    def n_delivery_id(self):
        return self._n_delivery_id

    @n_delivery_id.setter
    def n_delivery_id(self, value):
        self._n_delivery_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_access_mode:
            if hasattr(self.merchant_access_mode, 'to_alipay_dict'):
                params['merchant_access_mode'] = self.merchant_access_mode.to_alipay_dict()
            else:
                params['merchant_access_mode'] = self.merchant_access_mode
        if self.n_delivery_id:
            if hasattr(self.n_delivery_id, 'to_alipay_dict'):
                params['n_delivery_id'] = self.n_delivery_id.to_alipay_dict()
            else:
                params['n_delivery_id'] = self.n_delivery_id
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
        o = AlipayCommerceOperationIotnspoperationDeliveryStopModel()
        if 'merchant_access_mode' in d:
            o.merchant_access_mode = d['merchant_access_mode']
        if 'n_delivery_id' in d:
            o.n_delivery_id = d['n_delivery_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


