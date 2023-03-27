#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupervisionBillInfo(object):

    def __init__(self):
        self._amount = None
        self._currency = None
        self._order_no = None
        self._payee_card_name = None
        self._payee_card_no = None
        self._payer_card_name = None
        self._payer_card_no = None
        self._remark = None
        self._vostro_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def payee_card_name(self):
        return self._payee_card_name

    @payee_card_name.setter
    def payee_card_name(self, value):
        self._payee_card_name = value
    @property
    def payee_card_no(self):
        return self._payee_card_no

    @payee_card_no.setter
    def payee_card_no(self, value):
        self._payee_card_no = value
    @property
    def payer_card_name(self):
        return self._payer_card_name

    @payer_card_name.setter
    def payer_card_name(self, value):
        self._payer_card_name = value
    @property
    def payer_card_no(self):
        return self._payer_card_no

    @payer_card_no.setter
    def payer_card_no(self, value):
        self._payer_card_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def vostro_time(self):
        return self._vostro_time

    @vostro_time.setter
    def vostro_time(self, value):
        self._vostro_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.payee_card_name:
            if hasattr(self.payee_card_name, 'to_alipay_dict'):
                params['payee_card_name'] = self.payee_card_name.to_alipay_dict()
            else:
                params['payee_card_name'] = self.payee_card_name
        if self.payee_card_no:
            if hasattr(self.payee_card_no, 'to_alipay_dict'):
                params['payee_card_no'] = self.payee_card_no.to_alipay_dict()
            else:
                params['payee_card_no'] = self.payee_card_no
        if self.payer_card_name:
            if hasattr(self.payer_card_name, 'to_alipay_dict'):
                params['payer_card_name'] = self.payer_card_name.to_alipay_dict()
            else:
                params['payer_card_name'] = self.payer_card_name
        if self.payer_card_no:
            if hasattr(self.payer_card_no, 'to_alipay_dict'):
                params['payer_card_no'] = self.payer_card_no.to_alipay_dict()
            else:
                params['payer_card_no'] = self.payer_card_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.vostro_time:
            if hasattr(self.vostro_time, 'to_alipay_dict'):
                params['vostro_time'] = self.vostro_time.to_alipay_dict()
            else:
                params['vostro_time'] = self.vostro_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupervisionBillInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'payee_card_name' in d:
            o.payee_card_name = d['payee_card_name']
        if 'payee_card_no' in d:
            o.payee_card_no = d['payee_card_no']
        if 'payer_card_name' in d:
            o.payer_card_name = d['payer_card_name']
        if 'payer_card_no' in d:
            o.payer_card_no = d['payer_card_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'vostro_time' in d:
            o.vostro_time = d['vostro_time']
        return o


