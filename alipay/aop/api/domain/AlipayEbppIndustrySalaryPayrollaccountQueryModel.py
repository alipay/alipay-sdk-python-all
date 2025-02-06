#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySalaryPayrollaccountQueryModel(object):

    def __init__(self):
        self._acct_type = None
        self._biz_scene = None
        self._ext_info = None
        self._merchant_id = None
        self._product_code = None
        self._sign_xml = None

    @property
    def acct_type(self):
        return self._acct_type

    @acct_type.setter
    def acct_type(self, value):
        self._acct_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value


    def to_alipay_dict(self):
        params = dict()
        if self.acct_type:
            if hasattr(self.acct_type, 'to_alipay_dict'):
                params['acct_type'] = self.acct_type.to_alipay_dict()
            else:
                params['acct_type'] = self.acct_type
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sign_xml:
            if hasattr(self.sign_xml, 'to_alipay_dict'):
                params['sign_xml'] = self.sign_xml.to_alipay_dict()
            else:
                params['sign_xml'] = self.sign_xml
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustrySalaryPayrollaccountQueryModel()
        if 'acct_type' in d:
            o.acct_type = d['acct_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sign_xml' in d:
            o.sign_xml = d['sign_xml']
        return o


