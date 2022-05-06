#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetCardDepositModel(object):

    def __init__(self):
        self._amount = None
        self._asset_amount = None
        self._biz_dt = None
        self._biz_no = None
        self._extend_info = None
        self._fund_scence = None
        self._product_code = None
        self._template_id = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def asset_amount(self):
        return self._asset_amount

    @asset_amount.setter
    def asset_amount(self, value):
        self._asset_amount = value
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
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def fund_scence(self):
        return self._fund_scence

    @fund_scence.setter
    def fund_scence(self, value):
        self._fund_scence = value
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
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.asset_amount:
            if hasattr(self.asset_amount, 'to_alipay_dict'):
                params['asset_amount'] = self.asset_amount.to_alipay_dict()
            else:
                params['asset_amount'] = self.asset_amount
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
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.fund_scence:
            if hasattr(self.fund_scence, 'to_alipay_dict'):
                params['fund_scence'] = self.fund_scence.to_alipay_dict()
            else:
                params['fund_scence'] = self.fund_scence
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
        o = AlipayAssetCardDepositModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'asset_amount' in d:
            o.asset_amount = d['asset_amount']
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'fund_scence' in d:
            o.fund_scence = d['fund_scence']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


