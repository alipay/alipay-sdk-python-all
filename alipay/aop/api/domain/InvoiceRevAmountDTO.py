#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class InvoiceRevAmountDTO(object):

    def __init__(self):
        self._bill_no = None
        self._no_vat_receiveable_amount = None
        self._no_vat_tax_loss_amount = None
        self._no_vat_tax_loss_rate = None
        self._out_bill_no = None
        self._receiveable_amount = None
        self._vat_nomal_receiveable_amount = None
        self._vat_nomal_tax_loss_amount = None
        self._vat_nomal_tax_loss_rate = None
        self._vat_special_receiveable_amount = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def no_vat_receiveable_amount(self):
        return self._no_vat_receiveable_amount

    @no_vat_receiveable_amount.setter
    def no_vat_receiveable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._no_vat_receiveable_amount = value
        else:
            self._no_vat_receiveable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def no_vat_tax_loss_amount(self):
        return self._no_vat_tax_loss_amount

    @no_vat_tax_loss_amount.setter
    def no_vat_tax_loss_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._no_vat_tax_loss_amount = value
        else:
            self._no_vat_tax_loss_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def no_vat_tax_loss_rate(self):
        return self._no_vat_tax_loss_rate

    @no_vat_tax_loss_rate.setter
    def no_vat_tax_loss_rate(self, value):
        self._no_vat_tax_loss_rate = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def receiveable_amount(self):
        return self._receiveable_amount

    @receiveable_amount.setter
    def receiveable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._receiveable_amount = value
        else:
            self._receiveable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def vat_nomal_receiveable_amount(self):
        return self._vat_nomal_receiveable_amount

    @vat_nomal_receiveable_amount.setter
    def vat_nomal_receiveable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._vat_nomal_receiveable_amount = value
        else:
            self._vat_nomal_receiveable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def vat_nomal_tax_loss_amount(self):
        return self._vat_nomal_tax_loss_amount

    @vat_nomal_tax_loss_amount.setter
    def vat_nomal_tax_loss_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._vat_nomal_tax_loss_amount = value
        else:
            self._vat_nomal_tax_loss_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def vat_nomal_tax_loss_rate(self):
        return self._vat_nomal_tax_loss_rate

    @vat_nomal_tax_loss_rate.setter
    def vat_nomal_tax_loss_rate(self, value):
        self._vat_nomal_tax_loss_rate = value
    @property
    def vat_special_receiveable_amount(self):
        return self._vat_special_receiveable_amount

    @vat_special_receiveable_amount.setter
    def vat_special_receiveable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._vat_special_receiveable_amount = value
        else:
            self._vat_special_receiveable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.no_vat_receiveable_amount:
            if hasattr(self.no_vat_receiveable_amount, 'to_alipay_dict'):
                params['no_vat_receiveable_amount'] = self.no_vat_receiveable_amount.to_alipay_dict()
            else:
                params['no_vat_receiveable_amount'] = self.no_vat_receiveable_amount
        if self.no_vat_tax_loss_amount:
            if hasattr(self.no_vat_tax_loss_amount, 'to_alipay_dict'):
                params['no_vat_tax_loss_amount'] = self.no_vat_tax_loss_amount.to_alipay_dict()
            else:
                params['no_vat_tax_loss_amount'] = self.no_vat_tax_loss_amount
        if self.no_vat_tax_loss_rate:
            if hasattr(self.no_vat_tax_loss_rate, 'to_alipay_dict'):
                params['no_vat_tax_loss_rate'] = self.no_vat_tax_loss_rate.to_alipay_dict()
            else:
                params['no_vat_tax_loss_rate'] = self.no_vat_tax_loss_rate
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
        if self.receiveable_amount:
            if hasattr(self.receiveable_amount, 'to_alipay_dict'):
                params['receiveable_amount'] = self.receiveable_amount.to_alipay_dict()
            else:
                params['receiveable_amount'] = self.receiveable_amount
        if self.vat_nomal_receiveable_amount:
            if hasattr(self.vat_nomal_receiveable_amount, 'to_alipay_dict'):
                params['vat_nomal_receiveable_amount'] = self.vat_nomal_receiveable_amount.to_alipay_dict()
            else:
                params['vat_nomal_receiveable_amount'] = self.vat_nomal_receiveable_amount
        if self.vat_nomal_tax_loss_amount:
            if hasattr(self.vat_nomal_tax_loss_amount, 'to_alipay_dict'):
                params['vat_nomal_tax_loss_amount'] = self.vat_nomal_tax_loss_amount.to_alipay_dict()
            else:
                params['vat_nomal_tax_loss_amount'] = self.vat_nomal_tax_loss_amount
        if self.vat_nomal_tax_loss_rate:
            if hasattr(self.vat_nomal_tax_loss_rate, 'to_alipay_dict'):
                params['vat_nomal_tax_loss_rate'] = self.vat_nomal_tax_loss_rate.to_alipay_dict()
            else:
                params['vat_nomal_tax_loss_rate'] = self.vat_nomal_tax_loss_rate
        if self.vat_special_receiveable_amount:
            if hasattr(self.vat_special_receiveable_amount, 'to_alipay_dict'):
                params['vat_special_receiveable_amount'] = self.vat_special_receiveable_amount.to_alipay_dict()
            else:
                params['vat_special_receiveable_amount'] = self.vat_special_receiveable_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceRevAmountDTO()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'no_vat_receiveable_amount' in d:
            o.no_vat_receiveable_amount = d['no_vat_receiveable_amount']
        if 'no_vat_tax_loss_amount' in d:
            o.no_vat_tax_loss_amount = d['no_vat_tax_loss_amount']
        if 'no_vat_tax_loss_rate' in d:
            o.no_vat_tax_loss_rate = d['no_vat_tax_loss_rate']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'receiveable_amount' in d:
            o.receiveable_amount = d['receiveable_amount']
        if 'vat_nomal_receiveable_amount' in d:
            o.vat_nomal_receiveable_amount = d['vat_nomal_receiveable_amount']
        if 'vat_nomal_tax_loss_amount' in d:
            o.vat_nomal_tax_loss_amount = d['vat_nomal_tax_loss_amount']
        if 'vat_nomal_tax_loss_rate' in d:
            o.vat_nomal_tax_loss_rate = d['vat_nomal_tax_loss_rate']
        if 'vat_special_receiveable_amount' in d:
            o.vat_special_receiveable_amount = d['vat_special_receiveable_amount']
        return o


