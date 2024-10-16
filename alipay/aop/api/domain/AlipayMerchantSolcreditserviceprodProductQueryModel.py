#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantSolcreditserviceprodProductQueryModel(object):

    def __init__(self):
        self._out_product_no = None
        self._product_no = None
        self._smid = None

    @property
    def out_product_no(self):
        return self._out_product_no

    @out_product_no.setter
    def out_product_no(self, value):
        self._out_product_no = value
    @property
    def product_no(self):
        return self._product_no

    @product_no.setter
    def product_no(self, value):
        self._product_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_product_no:
            if hasattr(self.out_product_no, 'to_alipay_dict'):
                params['out_product_no'] = self.out_product_no.to_alipay_dict()
            else:
                params['out_product_no'] = self.out_product_no
        if self.product_no:
            if hasattr(self.product_no, 'to_alipay_dict'):
                params['product_no'] = self.product_no.to_alipay_dict()
            else:
                params['product_no'] = self.product_no
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolcreditserviceprodProductQueryModel()
        if 'out_product_no' in d:
            o.out_product_no = d['out_product_no']
        if 'product_no' in d:
            o.product_no = d['product_no']
        if 'smid' in d:
            o.smid = d['smid']
        return o


