#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetCardDepositbackModel(object):

    def __init__(self):
        self._biz_dt = None
        self._biz_no = None
        self._depositback_amount = None
        self._extend_info = None
        self._fund_scene = None
        self._original_bill_no = None
        self._product_code = None
        self._template_id = None
        self._user_id = None

    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def depositback_amount(self):
        return self._depositback_amount

    @depositback_amount.setter
    def depositback_amount(self, value):
        self._depositback_amount = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def fund_scene(self):
        return self._fund_scene

    @fund_scene.setter
    def fund_scene(self, value):
        self._fund_scene = value
    @property
    def original_bill_no(self):
        return self._original_bill_no

    @original_bill_no.setter
    def original_bill_no(self, value):
        self._original_bill_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.depositback_amount:
            if hasattr(self.depositback_amount, 'to_alipay_dict'):
                params['depositback_amount'] = self.depositback_amount.to_alipay_dict()
            else:
                params['depositback_amount'] = self.depositback_amount
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.fund_scene:
            if hasattr(self.fund_scene, 'to_alipay_dict'):
                params['fund_scene'] = self.fund_scene.to_alipay_dict()
            else:
                params['fund_scene'] = self.fund_scene
        if self.original_bill_no:
            if hasattr(self.original_bill_no, 'to_alipay_dict'):
                params['original_bill_no'] = self.original_bill_no.to_alipay_dict()
            else:
                params['original_bill_no'] = self.original_bill_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetCardDepositbackModel()
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'depositback_amount' in d:
            o.depositback_amount = d['depositback_amount']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'fund_scene' in d:
            o.fund_scene = d['fund_scene']
        if 'original_bill_no' in d:
            o.original_bill_no = d['original_bill_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


