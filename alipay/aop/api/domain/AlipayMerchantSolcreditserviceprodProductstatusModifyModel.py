#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantSolcreditserviceprodProductstatusModifyModel(object):

    def __init__(self):
        self._product_no = None
        self._product_status = None

    @property
    def product_no(self):
        return self._product_no

    @product_no.setter
    def product_no(self, value):
        self._product_no = value
    @property
    def product_status(self):
        return self._product_status

    @product_status.setter
    def product_status(self, value):
        self._product_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_no:
            if hasattr(self.product_no, 'to_alipay_dict'):
                params['product_no'] = self.product_no.to_alipay_dict()
            else:
                params['product_no'] = self.product_no
        if self.product_status:
            if hasattr(self.product_status, 'to_alipay_dict'):
                params['product_status'] = self.product_status.to_alipay_dict()
            else:
                params['product_status'] = self.product_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolcreditserviceprodProductstatusModifyModel()
        if 'product_no' in d:
            o.product_no = d['product_no']
        if 'product_status' in d:
            o.product_status = d['product_status']
        return o


