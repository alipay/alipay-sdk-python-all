#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustrySalaryElectronicreceiptQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._merchant_id = None
        self._out_trade_no = None
        self._product_code = None
        self._receipt_no = None
        self._sign_xml = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def receipt_no(self):
        return self._receipt_no

    @receipt_no.setter
    def receipt_no(self, value):
        self._receipt_no = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.receipt_no:
            if hasattr(self.receipt_no, 'to_alipay_dict'):
                params['receipt_no'] = self.receipt_no.to_alipay_dict()
            else:
                params['receipt_no'] = self.receipt_no
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
        o = AlipayEbppIndustrySalaryElectronicreceiptQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'receipt_no' in d:
            o.receipt_no = d['receipt_no']
        if 'sign_xml' in d:
            o.sign_xml = d['sign_xml']
        return o


