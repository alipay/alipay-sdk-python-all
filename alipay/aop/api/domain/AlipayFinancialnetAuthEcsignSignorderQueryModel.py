#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthEcsignSignorderQueryModel(object):

    def __init__(self):
        self._out_order_no = None
        self._partner_id = None
        self._sign_product_id = None
        self._solution_code = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def sign_product_id(self):
        return self._sign_product_id

    @sign_product_id.setter
    def sign_product_id(self, value):
        self._sign_product_id = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.sign_product_id:
            if hasattr(self.sign_product_id, 'to_alipay_dict'):
                params['sign_product_id'] = self.sign_product_id.to_alipay_dict()
            else:
                params['sign_product_id'] = self.sign_product_id
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthEcsignSignorderQueryModel()
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'sign_product_id' in d:
            o.sign_product_id = d['sign_product_id']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


