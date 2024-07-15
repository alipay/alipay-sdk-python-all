#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoOrderQueryModel(object):

    def __init__(self):
        self._busi_platform = None
        self._eco_code = None
        self._out_order_id = None
        self._shop_code = None

    @property
    def busi_platform(self):
        return self._busi_platform

    @busi_platform.setter
    def busi_platform(self, value):
        self._busi_platform = value
    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.busi_platform:
            if hasattr(self.busi_platform, 'to_alipay_dict'):
                params['busi_platform'] = self.busi_platform.to_alipay_dict()
            else:
                params['busi_platform'] = self.busi_platform
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoOrderQueryModel()
        if 'busi_platform' in d:
            o.busi_platform = d['busi_platform']
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        return o


