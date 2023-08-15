#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmEpAePrepayExtParam import ZmEpAePrepayExtParam


class ZhimaCreditEpAeprepayOrderSendModel(object):

    def __init__(self):
        self._ext_param = None
        self._order_amount = None
        self._order_currency = None
        self._order_time_millis = None
        self._reference_code = None
        self._seller_login_id = None
        self._stage = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        if isinstance(value, ZmEpAePrepayExtParam):
            self._ext_param = value
        else:
            self._ext_param = ZmEpAePrepayExtParam.from_alipay_dict(value)
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_currency(self):
        return self._order_currency

    @order_currency.setter
    def order_currency(self, value):
        self._order_currency = value
    @property
    def order_time_millis(self):
        return self._order_time_millis

    @order_time_millis.setter
    def order_time_millis(self, value):
        self._order_time_millis = value
    @property
    def reference_code(self):
        return self._reference_code

    @reference_code.setter
    def reference_code(self, value):
        self._reference_code = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_currency:
            if hasattr(self.order_currency, 'to_alipay_dict'):
                params['order_currency'] = self.order_currency.to_alipay_dict()
            else:
                params['order_currency'] = self.order_currency
        if self.order_time_millis:
            if hasattr(self.order_time_millis, 'to_alipay_dict'):
                params['order_time_millis'] = self.order_time_millis.to_alipay_dict()
            else:
                params['order_time_millis'] = self.order_time_millis
        if self.reference_code:
            if hasattr(self.reference_code, 'to_alipay_dict'):
                params['reference_code'] = self.reference_code.to_alipay_dict()
            else:
                params['reference_code'] = self.reference_code
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAeprepayOrderSendModel()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_currency' in d:
            o.order_currency = d['order_currency']
        if 'order_time_millis' in d:
            o.order_time_millis = d['order_time_millis']
        if 'reference_code' in d:
            o.reference_code = d['reference_code']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'stage' in d:
            o.stage = d['stage']
        return o


