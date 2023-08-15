#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmEpAePrepayExtParam import ZmEpAePrepayExtParam


class ZhimaCreditEpAeprepayOrderRefundModel(object):

    def __init__(self):
        self._advance_amount = None
        self._advance_currency = None
        self._ext_param = None
        self._order_id = None
        self._order_time_millis = None
        self._refund_amount = None
        self._refund_balance_amount = None
        self._refund_currency = None
        self._refund_time = None
        self._seller_login_id = None
        self._son_order_id = None
        self._sub_out_order_id = None

    @property
    def advance_amount(self):
        return self._advance_amount

    @advance_amount.setter
    def advance_amount(self, value):
        self._advance_amount = value
    @property
    def advance_currency(self):
        return self._advance_currency

    @advance_currency.setter
    def advance_currency(self, value):
        self._advance_currency = value
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
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_time_millis(self):
        return self._order_time_millis

    @order_time_millis.setter
    def order_time_millis(self, value):
        self._order_time_millis = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_balance_amount(self):
        return self._refund_balance_amount

    @refund_balance_amount.setter
    def refund_balance_amount(self, value):
        self._refund_balance_amount = value
    @property
    def refund_currency(self):
        return self._refund_currency

    @refund_currency.setter
    def refund_currency(self, value):
        self._refund_currency = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def son_order_id(self):
        return self._son_order_id

    @son_order_id.setter
    def son_order_id(self, value):
        self._son_order_id = value
    @property
    def sub_out_order_id(self):
        return self._sub_out_order_id

    @sub_out_order_id.setter
    def sub_out_order_id(self, value):
        self._sub_out_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_amount:
            if hasattr(self.advance_amount, 'to_alipay_dict'):
                params['advance_amount'] = self.advance_amount.to_alipay_dict()
            else:
                params['advance_amount'] = self.advance_amount
        if self.advance_currency:
            if hasattr(self.advance_currency, 'to_alipay_dict'):
                params['advance_currency'] = self.advance_currency.to_alipay_dict()
            else:
                params['advance_currency'] = self.advance_currency
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_time_millis:
            if hasattr(self.order_time_millis, 'to_alipay_dict'):
                params['order_time_millis'] = self.order_time_millis.to_alipay_dict()
            else:
                params['order_time_millis'] = self.order_time_millis
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_balance_amount:
            if hasattr(self.refund_balance_amount, 'to_alipay_dict'):
                params['refund_balance_amount'] = self.refund_balance_amount.to_alipay_dict()
            else:
                params['refund_balance_amount'] = self.refund_balance_amount
        if self.refund_currency:
            if hasattr(self.refund_currency, 'to_alipay_dict'):
                params['refund_currency'] = self.refund_currency.to_alipay_dict()
            else:
                params['refund_currency'] = self.refund_currency
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.son_order_id:
            if hasattr(self.son_order_id, 'to_alipay_dict'):
                params['son_order_id'] = self.son_order_id.to_alipay_dict()
            else:
                params['son_order_id'] = self.son_order_id
        if self.sub_out_order_id:
            if hasattr(self.sub_out_order_id, 'to_alipay_dict'):
                params['sub_out_order_id'] = self.sub_out_order_id.to_alipay_dict()
            else:
                params['sub_out_order_id'] = self.sub_out_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAeprepayOrderRefundModel()
        if 'advance_amount' in d:
            o.advance_amount = d['advance_amount']
        if 'advance_currency' in d:
            o.advance_currency = d['advance_currency']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_time_millis' in d:
            o.order_time_millis = d['order_time_millis']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_balance_amount' in d:
            o.refund_balance_amount = d['refund_balance_amount']
        if 'refund_currency' in d:
            o.refund_currency = d['refund_currency']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'son_order_id' in d:
            o.son_order_id = d['son_order_id']
        if 'sub_out_order_id' in d:
            o.sub_out_order_id = d['sub_out_order_id']
        return o


