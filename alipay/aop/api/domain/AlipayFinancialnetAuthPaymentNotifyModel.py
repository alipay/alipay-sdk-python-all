#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthPaymentNotifyModel(object):

    def __init__(self):
        self._basic_amount = None
        self._benefit_amount = None
        self._biz_status = None
        self._commodity_type = None
        self._out_commodity_id = None
        self._out_order_no = None
        self._platform_id = None
        self._trade_no = None
        self._user_id = None
        self._validate_token = None

    @property
    def basic_amount(self):
        return self._basic_amount

    @basic_amount.setter
    def basic_amount(self, value):
        self._basic_amount = value
    @property
    def benefit_amount(self):
        return self._benefit_amount

    @benefit_amount.setter
    def benefit_amount(self, value):
        self._benefit_amount = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def commodity_type(self):
        return self._commodity_type

    @commodity_type.setter
    def commodity_type(self, value):
        self._commodity_type = value
    @property
    def out_commodity_id(self):
        return self._out_commodity_id

    @out_commodity_id.setter
    def out_commodity_id(self, value):
        self._out_commodity_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def validate_token(self):
        return self._validate_token

    @validate_token.setter
    def validate_token(self, value):
        self._validate_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.basic_amount:
            if hasattr(self.basic_amount, 'to_alipay_dict'):
                params['basic_amount'] = self.basic_amount.to_alipay_dict()
            else:
                params['basic_amount'] = self.basic_amount
        if self.benefit_amount:
            if hasattr(self.benefit_amount, 'to_alipay_dict'):
                params['benefit_amount'] = self.benefit_amount.to_alipay_dict()
            else:
                params['benefit_amount'] = self.benefit_amount
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.commodity_type:
            if hasattr(self.commodity_type, 'to_alipay_dict'):
                params['commodity_type'] = self.commodity_type.to_alipay_dict()
            else:
                params['commodity_type'] = self.commodity_type
        if self.out_commodity_id:
            if hasattr(self.out_commodity_id, 'to_alipay_dict'):
                params['out_commodity_id'] = self.out_commodity_id.to_alipay_dict()
            else:
                params['out_commodity_id'] = self.out_commodity_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.validate_token:
            if hasattr(self.validate_token, 'to_alipay_dict'):
                params['validate_token'] = self.validate_token.to_alipay_dict()
            else:
                params['validate_token'] = self.validate_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthPaymentNotifyModel()
        if 'basic_amount' in d:
            o.basic_amount = d['basic_amount']
        if 'benefit_amount' in d:
            o.benefit_amount = d['benefit_amount']
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'commodity_type' in d:
            o.commodity_type = d['commodity_type']
        if 'out_commodity_id' in d:
            o.out_commodity_id = d['out_commodity_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'validate_token' in d:
            o.validate_token = d['validate_token']
        return o


