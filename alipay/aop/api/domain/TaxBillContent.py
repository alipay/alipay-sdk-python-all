#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaxBillContent(object):

    def __init__(self):
        self._anti_fake_code = None
        self._checker = None
        self._clerk = None
        self._einv_amount = None
        self._einv_code = None
        self._einv_date = None
        self._einv_no = None
        self._payee = None
        self._payee_address = None
        self._payee_bank_name = None
        self._payee_name = None
        self._payee_register_no = None
        self._payer_address = None
        self._payer_bank_name = None
        self._payer_name = None
        self._payer_register_no = None
        self._sum_amount = None
        self._tax_amount = None
        self._without_tax_amount = None

    @property
    def anti_fake_code(self):
        return self._anti_fake_code

    @anti_fake_code.setter
    def anti_fake_code(self, value):
        self._anti_fake_code = value
    @property
    def checker(self):
        return self._checker

    @checker.setter
    def checker(self, value):
        self._checker = value
    @property
    def clerk(self):
        return self._clerk

    @clerk.setter
    def clerk(self, value):
        self._clerk = value
    @property
    def einv_amount(self):
        return self._einv_amount

    @einv_amount.setter
    def einv_amount(self, value):
        self._einv_amount = value
    @property
    def einv_code(self):
        return self._einv_code

    @einv_code.setter
    def einv_code(self, value):
        self._einv_code = value
    @property
    def einv_date(self):
        return self._einv_date

    @einv_date.setter
    def einv_date(self, value):
        self._einv_date = value
    @property
    def einv_no(self):
        return self._einv_no

    @einv_no.setter
    def einv_no(self, value):
        self._einv_no = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def payee_address(self):
        return self._payee_address

    @payee_address.setter
    def payee_address(self, value):
        self._payee_address = value
    @property
    def payee_bank_name(self):
        return self._payee_bank_name

    @payee_bank_name.setter
    def payee_bank_name(self, value):
        self._payee_bank_name = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
    @property
    def payer_address(self):
        return self._payer_address

    @payer_address.setter
    def payer_address(self, value):
        self._payer_address = value
    @property
    def payer_bank_name(self):
        return self._payer_bank_name

    @payer_bank_name.setter
    def payer_bank_name(self, value):
        self._payer_bank_name = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def payer_register_no(self):
        return self._payer_register_no

    @payer_register_no.setter
    def payer_register_no(self, value):
        self._payer_register_no = value
    @property
    def sum_amount(self):
        return self._sum_amount

    @sum_amount.setter
    def sum_amount(self, value):
        self._sum_amount = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def without_tax_amount(self):
        return self._without_tax_amount

    @without_tax_amount.setter
    def without_tax_amount(self, value):
        self._without_tax_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.anti_fake_code:
            if hasattr(self.anti_fake_code, 'to_alipay_dict'):
                params['anti_fake_code'] = self.anti_fake_code.to_alipay_dict()
            else:
                params['anti_fake_code'] = self.anti_fake_code
        if self.checker:
            if hasattr(self.checker, 'to_alipay_dict'):
                params['checker'] = self.checker.to_alipay_dict()
            else:
                params['checker'] = self.checker
        if self.clerk:
            if hasattr(self.clerk, 'to_alipay_dict'):
                params['clerk'] = self.clerk.to_alipay_dict()
            else:
                params['clerk'] = self.clerk
        if self.einv_amount:
            if hasattr(self.einv_amount, 'to_alipay_dict'):
                params['einv_amount'] = self.einv_amount.to_alipay_dict()
            else:
                params['einv_amount'] = self.einv_amount
        if self.einv_code:
            if hasattr(self.einv_code, 'to_alipay_dict'):
                params['einv_code'] = self.einv_code.to_alipay_dict()
            else:
                params['einv_code'] = self.einv_code
        if self.einv_date:
            if hasattr(self.einv_date, 'to_alipay_dict'):
                params['einv_date'] = self.einv_date.to_alipay_dict()
            else:
                params['einv_date'] = self.einv_date
        if self.einv_no:
            if hasattr(self.einv_no, 'to_alipay_dict'):
                params['einv_no'] = self.einv_no.to_alipay_dict()
            else:
                params['einv_no'] = self.einv_no
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.payee_address:
            if hasattr(self.payee_address, 'to_alipay_dict'):
                params['payee_address'] = self.payee_address.to_alipay_dict()
            else:
                params['payee_address'] = self.payee_address
        if self.payee_bank_name:
            if hasattr(self.payee_bank_name, 'to_alipay_dict'):
                params['payee_bank_name'] = self.payee_bank_name.to_alipay_dict()
            else:
                params['payee_bank_name'] = self.payee_bank_name
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = self.payee_register_no.to_alipay_dict()
            else:
                params['payee_register_no'] = self.payee_register_no
        if self.payer_address:
            if hasattr(self.payer_address, 'to_alipay_dict'):
                params['payer_address'] = self.payer_address.to_alipay_dict()
            else:
                params['payer_address'] = self.payer_address
        if self.payer_bank_name:
            if hasattr(self.payer_bank_name, 'to_alipay_dict'):
                params['payer_bank_name'] = self.payer_bank_name.to_alipay_dict()
            else:
                params['payer_bank_name'] = self.payer_bank_name
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = self.payer_register_no.to_alipay_dict()
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.sum_amount:
            if hasattr(self.sum_amount, 'to_alipay_dict'):
                params['sum_amount'] = self.sum_amount.to_alipay_dict()
            else:
                params['sum_amount'] = self.sum_amount
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.without_tax_amount:
            if hasattr(self.without_tax_amount, 'to_alipay_dict'):
                params['without_tax_amount'] = self.without_tax_amount.to_alipay_dict()
            else:
                params['without_tax_amount'] = self.without_tax_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaxBillContent()
        if 'anti_fake_code' in d:
            o.anti_fake_code = d['anti_fake_code']
        if 'checker' in d:
            o.checker = d['checker']
        if 'clerk' in d:
            o.clerk = d['clerk']
        if 'einv_amount' in d:
            o.einv_amount = d['einv_amount']
        if 'einv_code' in d:
            o.einv_code = d['einv_code']
        if 'einv_date' in d:
            o.einv_date = d['einv_date']
        if 'einv_no' in d:
            o.einv_no = d['einv_no']
        if 'payee' in d:
            o.payee = d['payee']
        if 'payee_address' in d:
            o.payee_address = d['payee_address']
        if 'payee_bank_name' in d:
            o.payee_bank_name = d['payee_bank_name']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'payer_address' in d:
            o.payer_address = d['payer_address']
        if 'payer_bank_name' in d:
            o.payer_bank_name = d['payer_bank_name']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'sum_amount' in d:
            o.sum_amount = d['sum_amount']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'without_tax_amount' in d:
            o.without_tax_amount = d['without_tax_amount']
        return o


