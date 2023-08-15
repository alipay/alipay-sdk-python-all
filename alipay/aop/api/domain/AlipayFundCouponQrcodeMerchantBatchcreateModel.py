#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCouponQrcodeMerchantBatchcreateModel(object):

    def __init__(self):
        self._biz_product = None
        self._code_count = None
        self._code_group_count = None
        self._out_biz_no = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def code_count(self):
        return self._code_count

    @code_count.setter
    def code_count(self, value):
        self._code_count = value
    @property
    def code_group_count(self):
        return self._code_group_count

    @code_group_count.setter
    def code_group_count(self, value):
        self._code_group_count = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.code_count:
            if hasattr(self.code_count, 'to_alipay_dict'):
                params['code_count'] = self.code_count.to_alipay_dict()
            else:
                params['code_count'] = self.code_count
        if self.code_group_count:
            if hasattr(self.code_group_count, 'to_alipay_dict'):
                params['code_group_count'] = self.code_group_count.to_alipay_dict()
            else:
                params['code_group_count'] = self.code_group_count
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
        o = AlipayFundCouponQrcodeMerchantBatchcreateModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'code_count' in d:
            o.code_count = d['code_count']
        if 'code_group_count' in d:
            o.code_group_count = d['code_group_count']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


