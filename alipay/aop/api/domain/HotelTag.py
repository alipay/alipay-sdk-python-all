#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelTag(object):

    def __init__(self):
        self._support_breakfast = None
        self._support_free_cancel = None
        self._support_prepay = None
        self._support_prepay_invoice = None
        self._support_self_pay = None
        self._support_special_invoice = None

    @property
    def support_breakfast(self):
        return self._support_breakfast

    @support_breakfast.setter
    def support_breakfast(self, value):
        self._support_breakfast = value
    @property
    def support_free_cancel(self):
        return self._support_free_cancel

    @support_free_cancel.setter
    def support_free_cancel(self, value):
        self._support_free_cancel = value
    @property
    def support_prepay(self):
        return self._support_prepay

    @support_prepay.setter
    def support_prepay(self, value):
        self._support_prepay = value
    @property
    def support_prepay_invoice(self):
        return self._support_prepay_invoice

    @support_prepay_invoice.setter
    def support_prepay_invoice(self, value):
        self._support_prepay_invoice = value
    @property
    def support_self_pay(self):
        return self._support_self_pay

    @support_self_pay.setter
    def support_self_pay(self, value):
        self._support_self_pay = value
    @property
    def support_special_invoice(self):
        return self._support_special_invoice

    @support_special_invoice.setter
    def support_special_invoice(self, value):
        self._support_special_invoice = value


    def to_alipay_dict(self):
        params = dict()
        if self.support_breakfast:
            if hasattr(self.support_breakfast, 'to_alipay_dict'):
                params['support_breakfast'] = self.support_breakfast.to_alipay_dict()
            else:
                params['support_breakfast'] = self.support_breakfast
        if self.support_free_cancel:
            if hasattr(self.support_free_cancel, 'to_alipay_dict'):
                params['support_free_cancel'] = self.support_free_cancel.to_alipay_dict()
            else:
                params['support_free_cancel'] = self.support_free_cancel
        if self.support_prepay:
            if hasattr(self.support_prepay, 'to_alipay_dict'):
                params['support_prepay'] = self.support_prepay.to_alipay_dict()
            else:
                params['support_prepay'] = self.support_prepay
        if self.support_prepay_invoice:
            if hasattr(self.support_prepay_invoice, 'to_alipay_dict'):
                params['support_prepay_invoice'] = self.support_prepay_invoice.to_alipay_dict()
            else:
                params['support_prepay_invoice'] = self.support_prepay_invoice
        if self.support_self_pay:
            if hasattr(self.support_self_pay, 'to_alipay_dict'):
                params['support_self_pay'] = self.support_self_pay.to_alipay_dict()
            else:
                params['support_self_pay'] = self.support_self_pay
        if self.support_special_invoice:
            if hasattr(self.support_special_invoice, 'to_alipay_dict'):
                params['support_special_invoice'] = self.support_special_invoice.to_alipay_dict()
            else:
                params['support_special_invoice'] = self.support_special_invoice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelTag()
        if 'support_breakfast' in d:
            o.support_breakfast = d['support_breakfast']
        if 'support_free_cancel' in d:
            o.support_free_cancel = d['support_free_cancel']
        if 'support_prepay' in d:
            o.support_prepay = d['support_prepay']
        if 'support_prepay_invoice' in d:
            o.support_prepay_invoice = d['support_prepay_invoice']
        if 'support_self_pay' in d:
            o.support_self_pay = d['support_self_pay']
        if 'support_special_invoice' in d:
            o.support_special_invoice = d['support_special_invoice']
        return o


