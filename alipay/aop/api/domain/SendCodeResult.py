#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SendCodeResult(object):

    def __init__(self):
        self._code = None
        self._code_url = None
        self._item_id = None
        self._merchant_order_url = None
        self._out_item_id = None
        self._out_sku_id = None
        self._qr_code = None
        self._sku_id = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def code_url(self):
        return self._code_url

    @code_url.setter
    def code_url(self, value):
        self._code_url = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def merchant_order_url(self):
        return self._merchant_order_url

    @merchant_order_url.setter
    def merchant_order_url(self, value):
        self._merchant_order_url = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.code_url:
            if hasattr(self.code_url, 'to_alipay_dict'):
                params['code_url'] = self.code_url.to_alipay_dict()
            else:
                params['code_url'] = self.code_url
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.merchant_order_url:
            if hasattr(self.merchant_order_url, 'to_alipay_dict'):
                params['merchant_order_url'] = self.merchant_order_url.to_alipay_dict()
            else:
                params['merchant_order_url'] = self.merchant_order_url
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SendCodeResult()
        if 'code' in d:
            o.code = d['code']
        if 'code_url' in d:
            o.code_url = d['code_url']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'merchant_order_url' in d:
            o.merchant_order_url = d['merchant_order_url']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


