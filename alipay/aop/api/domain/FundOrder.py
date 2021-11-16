#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceId import ReferenceId
from alipay.aop.api.domain.ReferenceId import ReferenceId


class FundOrder(object):

    def __init__(self):
        self._order_amount = None
        self._order_create_time = None
        self._order_currency = None
        self._order_expiry_time = None
        self._order_type = None
        self._out_order_id = None
        self._payee_out_member_id = None
        self._payer_out_member_id = None
        self._remark = None

    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_currency(self):
        return self._order_currency

    @order_currency.setter
    def order_currency(self, value):
        self._order_currency = value
    @property
    def order_expiry_time(self):
        return self._order_expiry_time

    @order_expiry_time.setter
    def order_expiry_time(self, value):
        self._order_expiry_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def payee_out_member_id(self):
        return self._payee_out_member_id

    @payee_out_member_id.setter
    def payee_out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._payee_out_member_id = value
        else:
            self._payee_out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def payer_out_member_id(self):
        return self._payer_out_member_id

    @payer_out_member_id.setter
    def payer_out_member_id(self, value):
        if isinstance(value, ReferenceId):
            self._payer_out_member_id = value
        else:
            self._payer_out_member_id = ReferenceId.from_alipay_dict(value)
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_currency:
            if hasattr(self.order_currency, 'to_alipay_dict'):
                params['order_currency'] = self.order_currency.to_alipay_dict()
            else:
                params['order_currency'] = self.order_currency
        if self.order_expiry_time:
            if hasattr(self.order_expiry_time, 'to_alipay_dict'):
                params['order_expiry_time'] = self.order_expiry_time.to_alipay_dict()
            else:
                params['order_expiry_time'] = self.order_expiry_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.payee_out_member_id:
            if hasattr(self.payee_out_member_id, 'to_alipay_dict'):
                params['payee_out_member_id'] = self.payee_out_member_id.to_alipay_dict()
            else:
                params['payee_out_member_id'] = self.payee_out_member_id
        if self.payer_out_member_id:
            if hasattr(self.payer_out_member_id, 'to_alipay_dict'):
                params['payer_out_member_id'] = self.payer_out_member_id.to_alipay_dict()
            else:
                params['payer_out_member_id'] = self.payer_out_member_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundOrder()
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_currency' in d:
            o.order_currency = d['order_currency']
        if 'order_expiry_time' in d:
            o.order_expiry_time = d['order_expiry_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'payee_out_member_id' in d:
            o.payee_out_member_id = d['payee_out_member_id']
        if 'payer_out_member_id' in d:
            o.payer_out_member_id = d['payer_out_member_id']
        if 'remark' in d:
            o.remark = d['remark']
        return o


