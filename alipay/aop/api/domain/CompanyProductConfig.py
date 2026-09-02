#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankQuotaResult import BankQuotaResult


class CompanyProductConfig(object):

    def __init__(self):
        self._bank_quota_list = None
        self._invite_suppliers_after_order_confirm = None
        self._invoice_kind = None
        self._natural_person_bankcard_receive_status = None
        self._order_audit = None
        self._tax_method = None
        self._tax_rate = None

    @property
    def bank_quota_list(self):
        return self._bank_quota_list

    @bank_quota_list.setter
    def bank_quota_list(self, value):
        if isinstance(value, list):
            self._bank_quota_list = list()
            for i in value:
                if isinstance(i, BankQuotaResult):
                    self._bank_quota_list.append(i)
                else:
                    self._bank_quota_list.append(BankQuotaResult.from_alipay_dict(i))
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
    def natural_person_bankcard_receive_status(self):
        return self._natural_person_bankcard_receive_status

    @natural_person_bankcard_receive_status.setter
    def natural_person_bankcard_receive_status(self, value):
        self._natural_person_bankcard_receive_status = value
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
        if self.bank_quota_list:
            if isinstance(self.bank_quota_list, list):
                for i in range(0, len(self.bank_quota_list)):
                    element = self.bank_quota_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_quota_list[i] = element.to_alipay_dict()
            if hasattr(self.bank_quota_list, 'to_alipay_dict'):
                params['bank_quota_list'] = self.bank_quota_list.to_alipay_dict()
            else:
                params['bank_quota_list'] = self.bank_quota_list
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
        if self.natural_person_bankcard_receive_status:
            if hasattr(self.natural_person_bankcard_receive_status, 'to_alipay_dict'):
                params['natural_person_bankcard_receive_status'] = self.natural_person_bankcard_receive_status.to_alipay_dict()
            else:
                params['natural_person_bankcard_receive_status'] = self.natural_person_bankcard_receive_status
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
        if 'bank_quota_list' in d:
            o.bank_quota_list = d['bank_quota_list']
        if 'invite_suppliers_after_order_confirm' in d:
            o.invite_suppliers_after_order_confirm = d['invite_suppliers_after_order_confirm']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'natural_person_bankcard_receive_status' in d:
            o.natural_person_bankcard_receive_status = d['natural_person_bankcard_receive_status']
        if 'order_audit' in d:
            o.order_audit = d['order_audit']
        if 'tax_method' in d:
            o.tax_method = d['tax_method']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


