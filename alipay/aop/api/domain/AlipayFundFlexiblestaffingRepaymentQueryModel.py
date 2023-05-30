#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundFlexiblestaffingRepaymentQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._fund_order_id = None
        self._loan_agreement_no = None
        self._out_biz_no = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def fund_order_id(self):
        return self._fund_order_id

    @fund_order_id.setter
    def fund_order_id(self, value):
        self._fund_order_id = value
    @property
    def loan_agreement_no(self):
        return self._loan_agreement_no

    @loan_agreement_no.setter
    def loan_agreement_no(self, value):
        self._loan_agreement_no = value
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
        if self.fund_order_id:
            if hasattr(self.fund_order_id, 'to_alipay_dict'):
                params['fund_order_id'] = self.fund_order_id.to_alipay_dict()
            else:
                params['fund_order_id'] = self.fund_order_id
        if self.loan_agreement_no:
            if hasattr(self.loan_agreement_no, 'to_alipay_dict'):
                params['loan_agreement_no'] = self.loan_agreement_no.to_alipay_dict()
            else:
                params['loan_agreement_no'] = self.loan_agreement_no
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
        o = AlipayFundFlexiblestaffingRepaymentQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'fund_order_id' in d:
            o.fund_order_id = d['fund_order_id']
        if 'loan_agreement_no' in d:
            o.loan_agreement_no = d['loan_agreement_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


