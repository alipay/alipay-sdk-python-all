#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyProductConfig(object):

    def __init__(self):
        self._invite_suppliers_after_order_confirm = None
        self._invoice_kind = None
        self._order_audit = None
        self._tax_method = None
        self._tax_rate = None

    @property
    def invite_suppliers_after_order_confirm(self):
        return self._invite_suppliers_after_order_confirm

    @invite_suppliers_after_order_confirm.setter
    def invite_suppliers_after_order_confirm(self, value):
        self._invite_suppliers_after_order_confirm = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def order_audit(self):
        return self._order_audit

    @order_audit.setter
    def order_audit(self, value):
        self._order_audit = value
    @property
    def tax_method(self):
        return self._tax_method

    @tax_method.setter
    def tax_method(self, value):
        self._tax_method = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.invite_suppliers_after_order_confirm:
            if hasattr(self.invite_suppliers_after_order_confirm, 'to_alipay_dict'):
                params['invite_suppliers_after_order_confirm'] = self.invite_suppliers_after_order_confirm.to_alipay_dict()
            else:
                params['invite_suppliers_after_order_confirm'] = self.invite_suppliers_after_order_confirm
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.order_audit:
            if hasattr(self.order_audit, 'to_alipay_dict'):
                params['order_audit'] = self.order_audit.to_alipay_dict()
            else:
                params['order_audit'] = self.order_audit
        if self.tax_method:
            if hasattr(self.tax_method, 'to_alipay_dict'):
                params['tax_method'] = self.tax_method.to_alipay_dict()
            else:
                params['tax_method'] = self.tax_method
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyProductConfig()
        if 'invite_suppliers_after_order_confirm' in d:
            o.invite_suppliers_after_order_confirm = d['invite_suppliers_after_order_confirm']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'order_audit' in d:
            o.order_audit = d['order_audit']
        if 'tax_method' in d:
            o.tax_method = d['tax_method']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


