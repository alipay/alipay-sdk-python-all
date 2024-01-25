#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceBaseInfo import InvoiceBaseInfo


class AlipayFundMbpcardInvoiceprocessModifyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._invoice_list = None
        self._merchant_id = None
        self._process_id = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def invoice_list(self):
        return self._invoice_list

    @invoice_list.setter
    def invoice_list(self, value):
        if isinstance(value, list):
            self._invoice_list = list()
            for i in value:
                if isinstance(i, InvoiceBaseInfo):
                    self._invoice_list.append(i)
                else:
                    self._invoice_list.append(InvoiceBaseInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
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
        if self.invoice_list:
            if isinstance(self.invoice_list, list):
                for i in range(0, len(self.invoice_list)):
                    element = self.invoice_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_list, 'to_alipay_dict'):
                params['invoice_list'] = self.invoice_list.to_alipay_dict()
            else:
                params['invoice_list'] = self.invoice_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
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
        o = AlipayFundMbpcardInvoiceprocessModifyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'invoice_list' in d:
            o.invoice_list = d['invoice_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


