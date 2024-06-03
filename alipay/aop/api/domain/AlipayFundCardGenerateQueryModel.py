#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundCardGenerateQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._fund_card_generate_no = None
        self._out_request_no = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def fund_card_generate_no(self):
        return self._fund_card_generate_no

    @fund_card_generate_no.setter
    def fund_card_generate_no(self, value):
        self._fund_card_generate_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
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
        if self.fund_card_generate_no:
            if hasattr(self.fund_card_generate_no, 'to_alipay_dict'):
                params['fund_card_generate_no'] = self.fund_card_generate_no.to_alipay_dict()
            else:
                params['fund_card_generate_no'] = self.fund_card_generate_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        o = AlipayFundCardGenerateQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'fund_card_generate_no' in d:
            o.fund_card_generate_no = d['fund_card_generate_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


