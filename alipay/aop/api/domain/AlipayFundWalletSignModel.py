#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundWalletSignModel(object):

    def __init__(self):
        self._biz_scene = None
        self._identity_name = None
        self._identity_no = None
        self._out_biz_no = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def identity_name(self):
        return self._identity_name

    @identity_name.setter
    def identity_name(self, value):
        self._identity_name = value
    @property
    def identity_no(self):
        return self._identity_no

    @identity_no.setter
    def identity_no(self, value):
        self._identity_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        if self.identity_name:
            if hasattr(self.identity_name, 'to_alipay_dict'):
                params['identity_name'] = self.identity_name.to_alipay_dict()
            else:
                params['identity_name'] = self.identity_name
        if self.identity_no:
            if hasattr(self.identity_no, 'to_alipay_dict'):
                params['identity_no'] = self.identity_no.to_alipay_dict()
            else:
                params['identity_no'] = self.identity_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayFundWalletSignModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'identity_name' in d:
            o.identity_name = d['identity_name']
        if 'identity_no' in d:
            o.identity_no = d['identity_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


