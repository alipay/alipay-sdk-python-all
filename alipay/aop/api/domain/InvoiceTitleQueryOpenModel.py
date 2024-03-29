#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceTitleQueryOpenModel(object):

    def __init__(self):
        self._open_id = None
        self._payer_address = None
        self._payer_bank_account = None
        self._payer_bank_name = None
        self._payer_register_no = None
        self._payer_tel = None
        self._title_name = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def payer_address(self):
        return self._payer_address

    @payer_address.setter
    def payer_address(self, value):
        self._payer_address = value
    @property
    def payer_bank_account(self):
        return self._payer_bank_account

    @payer_bank_account.setter
    def payer_bank_account(self, value):
        self._payer_bank_account = value
    @property
    def payer_bank_name(self):
        return self._payer_bank_name

    @payer_bank_name.setter
    def payer_bank_name(self, value):
        self._payer_bank_name = value
    @property
    def payer_register_no(self):
        return self._payer_register_no

    @payer_register_no.setter
    def payer_register_no(self, value):
        self._payer_register_no = value
    @property
    def payer_tel(self):
        return self._payer_tel

    @payer_tel.setter
    def payer_tel(self, value):
        self._payer_tel = value
    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self, value):
        self._title_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.payer_address:
            if hasattr(self.payer_address, 'to_alipay_dict'):
                params['payer_address'] = self.payer_address.to_alipay_dict()
            else:
                params['payer_address'] = self.payer_address
        if self.payer_bank_account:
            if hasattr(self.payer_bank_account, 'to_alipay_dict'):
                params['payer_bank_account'] = self.payer_bank_account.to_alipay_dict()
            else:
                params['payer_bank_account'] = self.payer_bank_account
        if self.payer_bank_name:
            if hasattr(self.payer_bank_name, 'to_alipay_dict'):
                params['payer_bank_name'] = self.payer_bank_name.to_alipay_dict()
            else:
                params['payer_bank_name'] = self.payer_bank_name
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = self.payer_register_no.to_alipay_dict()
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.payer_tel:
            if hasattr(self.payer_tel, 'to_alipay_dict'):
                params['payer_tel'] = self.payer_tel.to_alipay_dict()
            else:
                params['payer_tel'] = self.payer_tel
        if self.title_name:
            if hasattr(self.title_name, 'to_alipay_dict'):
                params['title_name'] = self.title_name.to_alipay_dict()
            else:
                params['title_name'] = self.title_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceTitleQueryOpenModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'payer_address' in d:
            o.payer_address = d['payer_address']
        if 'payer_bank_account' in d:
            o.payer_bank_account = d['payer_bank_account']
        if 'payer_bank_name' in d:
            o.payer_bank_name = d['payer_bank_name']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'payer_tel' in d:
            o.payer_tel = d['payer_tel']
        if 'title_name' in d:
            o.title_name = d['title_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


