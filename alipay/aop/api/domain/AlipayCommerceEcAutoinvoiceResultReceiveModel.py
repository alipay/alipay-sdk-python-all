#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcAutoinvoiceResultReceiveModel(object):

    def __init__(self):
        self._biz_product = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._fail_code = None
        self._fail_message = None
        self._invoice_result = None
        self._out_biz_no = None
        self._trade_no = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_message(self):
        return self._fail_message

    @fail_message.setter
    def fail_message(self, value):
        self._fail_message = value
    @property
    def invoice_result(self):
        return self._invoice_result

    @invoice_result.setter
    def invoice_result(self, value):
        self._invoice_result = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.fail_message:
            if hasattr(self.fail_message, 'to_alipay_dict'):
                params['fail_message'] = self.fail_message.to_alipay_dict()
            else:
                params['fail_message'] = self.fail_message
        if self.invoice_result:
            if hasattr(self.invoice_result, 'to_alipay_dict'):
                params['invoice_result'] = self.invoice_result.to_alipay_dict()
            else:
                params['invoice_result'] = self.invoice_result
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcAutoinvoiceResultReceiveModel()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'fail_message' in d:
            o.fail_message = d['fail_message']
        if 'invoice_result' in d:
            o.invoice_result = d['invoice_result']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


