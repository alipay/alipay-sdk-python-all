#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeRepaybillOrderCreateModel(object):

    def __init__(self):
        self._bill_no = None
        self._out_order_no = None
        self._passback_params = None
        self._payer_user_id = None
        self._repay_amount = None
        self._repay_payee_name = None
        self._repay_product_code = None
        self._repay_remark = None
        self._repay_timeout_express = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def passback_params(self):
        return self._passback_params

    @passback_params.setter
    def passback_params(self, value):
        self._passback_params = value
    @property
    def payer_user_id(self):
        return self._payer_user_id

    @payer_user_id.setter
    def payer_user_id(self, value):
        self._payer_user_id = value
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_payee_name(self):
        return self._repay_payee_name

    @repay_payee_name.setter
    def repay_payee_name(self, value):
        self._repay_payee_name = value
    @property
    def repay_product_code(self):
        return self._repay_product_code

    @repay_product_code.setter
    def repay_product_code(self, value):
        self._repay_product_code = value
    @property
    def repay_remark(self):
        return self._repay_remark

    @repay_remark.setter
    def repay_remark(self, value):
        self._repay_remark = value
    @property
    def repay_timeout_express(self):
        return self._repay_timeout_express

    @repay_timeout_express.setter
    def repay_timeout_express(self, value):
        self._repay_timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.passback_params:
            if hasattr(self.passback_params, 'to_alipay_dict'):
                params['passback_params'] = self.passback_params.to_alipay_dict()
            else:
                params['passback_params'] = self.passback_params
        if self.payer_user_id:
            if hasattr(self.payer_user_id, 'to_alipay_dict'):
                params['payer_user_id'] = self.payer_user_id.to_alipay_dict()
            else:
                params['payer_user_id'] = self.payer_user_id
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.repay_payee_name:
            if hasattr(self.repay_payee_name, 'to_alipay_dict'):
                params['repay_payee_name'] = self.repay_payee_name.to_alipay_dict()
            else:
                params['repay_payee_name'] = self.repay_payee_name
        if self.repay_product_code:
            if hasattr(self.repay_product_code, 'to_alipay_dict'):
                params['repay_product_code'] = self.repay_product_code.to_alipay_dict()
            else:
                params['repay_product_code'] = self.repay_product_code
        if self.repay_remark:
            if hasattr(self.repay_remark, 'to_alipay_dict'):
                params['repay_remark'] = self.repay_remark.to_alipay_dict()
            else:
                params['repay_remark'] = self.repay_remark
        if self.repay_timeout_express:
            if hasattr(self.repay_timeout_express, 'to_alipay_dict'):
                params['repay_timeout_express'] = self.repay_timeout_express.to_alipay_dict()
            else:
                params['repay_timeout_express'] = self.repay_timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeRepaybillOrderCreateModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'passback_params' in d:
            o.passback_params = d['passback_params']
        if 'payer_user_id' in d:
            o.payer_user_id = d['payer_user_id']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_payee_name' in d:
            o.repay_payee_name = d['repay_payee_name']
        if 'repay_product_code' in d:
            o.repay_product_code = d['repay_product_code']
        if 'repay_remark' in d:
            o.repay_remark = d['repay_remark']
        if 'repay_timeout_express' in d:
            o.repay_timeout_express = d['repay_timeout_express']
        return o


