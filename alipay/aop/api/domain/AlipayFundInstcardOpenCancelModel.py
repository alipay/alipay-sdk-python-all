#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstInfo import InstInfo
from alipay.aop.api.domain.MerchantIdentityParams import MerchantIdentityParams


class AlipayFundInstcardOpenCancelModel(object):

    def __init__(self):
        self._biz_scene = None
        self._inst_info = None
        self._merchant_info = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def inst_info(self):
        return self._inst_info

    @inst_info.setter
    def inst_info(self, value):
        if isinstance(value, InstInfo):
            self._inst_info = value
        else:
            self._inst_info = InstInfo.from_alipay_dict(value)
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, MerchantIdentityParams):
            self._merchant_info = value
        else:
            self._merchant_info = MerchantIdentityParams.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.inst_info:
            if hasattr(self.inst_info, 'to_alipay_dict'):
                params['inst_info'] = self.inst_info.to_alipay_dict()
            else:
                params['inst_info'] = self.inst_info
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundInstcardOpenCancelModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'inst_info' in d:
            o.inst_info = d['inst_info']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


