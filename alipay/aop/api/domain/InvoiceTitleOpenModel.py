#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceTitleOpenModel(object):

    def __init__(self):
        self._payer_address_tel = None
        self._payer_bank_name_account = None
        self._payer_register_no = None
        self._title_name = None

    @property
    def payer_address_tel(self):
        return self._payer_address_tel

    @payer_address_tel.setter
    def payer_address_tel(self, value):
        self._payer_address_tel = value
    @property
    def payer_bank_name_account(self):
        return self._payer_bank_name_account

    @payer_bank_name_account.setter
    def payer_bank_name_account(self, value):
        self._payer_bank_name_account = value
    @property
    def payer_register_no(self):
        return self._payer_register_no

    @payer_register_no.setter
    def payer_register_no(self, value):
        self._payer_register_no = value
    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self, value):
        self._title_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.payer_address_tel:
            if hasattr(self.payer_address_tel, 'to_alipay_dict'):
                params['payer_address_tel'] = self.payer_address_tel.to_alipay_dict()
            else:
                params['payer_address_tel'] = self.payer_address_tel
        if self.payer_bank_name_account:
            if hasattr(self.payer_bank_name_account, 'to_alipay_dict'):
                params['payer_bank_name_account'] = self.payer_bank_name_account.to_alipay_dict()
            else:
                params['payer_bank_name_account'] = self.payer_bank_name_account
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = self.payer_register_no.to_alipay_dict()
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.title_name:
            if hasattr(self.title_name, 'to_alipay_dict'):
                params['title_name'] = self.title_name.to_alipay_dict()
            else:
                params['title_name'] = self.title_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTitleOpenModel()
        if 'payer_address_tel' in d:
            o.payer_address_tel = d['payer_address_tel']
        if 'payer_bank_name_account' in d:
            o.payer_bank_name_account = d['payer_bank_name_account']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'title_name' in d:
            o.title_name = d['title_name']
        return o


