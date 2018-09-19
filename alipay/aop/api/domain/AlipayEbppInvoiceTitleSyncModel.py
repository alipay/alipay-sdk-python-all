#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceTitleSyncModel(object):

    def __init__(self):
        self._open_bank_account = None
        self._open_bank_name = None
        self._tax_register_no = None
        self._title_name = None
        self._user_address = None
        self._user_id = None
        self._user_mobile = None

    @property
    def open_bank_account(self):
        return self._open_bank_account

    @open_bank_account.setter
    def open_bank_account(self, value):
        self._open_bank_account = value
    @property
    def open_bank_name(self):
        return self._open_bank_name

    @open_bank_name.setter
    def open_bank_name(self, value):
        self._open_bank_name = value
    @property
    def tax_register_no(self):
        return self._tax_register_no

    @tax_register_no.setter
    def tax_register_no(self, value):
        self._tax_register_no = value
    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self, value):
        self._title_name = value
    @property
    def user_address(self):
        return self._user_address

    @user_address.setter
    def user_address(self, value):
        self._user_address = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_bank_account:
            if hasattr(self.open_bank_account, 'to_alipay_dict'):
                params['open_bank_account'] = self.open_bank_account.to_alipay_dict()
            else:
                params['open_bank_account'] = self.open_bank_account
        if self.open_bank_name:
            if hasattr(self.open_bank_name, 'to_alipay_dict'):
                params['open_bank_name'] = self.open_bank_name.to_alipay_dict()
            else:
                params['open_bank_name'] = self.open_bank_name
        if self.tax_register_no:
            if hasattr(self.tax_register_no, 'to_alipay_dict'):
                params['tax_register_no'] = self.tax_register_no.to_alipay_dict()
            else:
                params['tax_register_no'] = self.tax_register_no
        if self.title_name:
            if hasattr(self.title_name, 'to_alipay_dict'):
                params['title_name'] = self.title_name.to_alipay_dict()
            else:
                params['title_name'] = self.title_name
        if self.user_address:
            if hasattr(self.user_address, 'to_alipay_dict'):
                params['user_address'] = self.user_address.to_alipay_dict()
            else:
                params['user_address'] = self.user_address
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_mobile:
            if hasattr(self.user_mobile, 'to_alipay_dict'):
                params['user_mobile'] = self.user_mobile.to_alipay_dict()
            else:
                params['user_mobile'] = self.user_mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceTitleSyncModel()
        if 'open_bank_account' in d:
            o.open_bank_account = d['open_bank_account']
        if 'open_bank_name' in d:
            o.open_bank_name = d['open_bank_name']
        if 'tax_register_no' in d:
            o.tax_register_no = d['tax_register_no']
        if 'title_name' in d:
            o.title_name = d['title_name']
        if 'user_address' in d:
            o.user_address = d['user_address']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        return o


