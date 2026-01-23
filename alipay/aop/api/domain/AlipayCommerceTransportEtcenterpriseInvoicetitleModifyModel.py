#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcenterpriseInvoicetitleModifyModel(object):

    def __init__(self):
        self._apply_id = None
        self._buyer_addr = None
        self._buyer_bank = None
        self._buyer_bank_account = None
        self._buyer_name = None
        self._buyer_tax_num = None
        self._buyer_tel = None
        self._corp_id = None
        self._email = None
        self._open_id = None
        self._title_type = None
        self._user_id = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def buyer_addr(self):
        return self._buyer_addr

    @buyer_addr.setter
    def buyer_addr(self, value):
        self._buyer_addr = value
    @property
    def buyer_bank(self):
        return self._buyer_bank

    @buyer_bank.setter
    def buyer_bank(self, value):
        self._buyer_bank = value
    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_tax_num(self):
        return self._buyer_tax_num

    @buyer_tax_num.setter
    def buyer_tax_num(self, value):
        self._buyer_tax_num = value
    @property
    def buyer_tel(self):
        return self._buyer_tel

    @buyer_tel.setter
    def buyer_tel(self, value):
        self._buyer_tel = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def title_type(self):
        return self._title_type

    @title_type.setter
    def title_type(self, value):
        self._title_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.buyer_addr:
            if hasattr(self.buyer_addr, 'to_alipay_dict'):
                params['buyer_addr'] = self.buyer_addr.to_alipay_dict()
            else:
                params['buyer_addr'] = self.buyer_addr
        if self.buyer_bank:
            if hasattr(self.buyer_bank, 'to_alipay_dict'):
                params['buyer_bank'] = self.buyer_bank.to_alipay_dict()
            else:
                params['buyer_bank'] = self.buyer_bank
        if self.buyer_bank_account:
            if hasattr(self.buyer_bank_account, 'to_alipay_dict'):
                params['buyer_bank_account'] = self.buyer_bank_account.to_alipay_dict()
            else:
                params['buyer_bank_account'] = self.buyer_bank_account
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_tax_num:
            if hasattr(self.buyer_tax_num, 'to_alipay_dict'):
                params['buyer_tax_num'] = self.buyer_tax_num.to_alipay_dict()
            else:
                params['buyer_tax_num'] = self.buyer_tax_num
        if self.buyer_tel:
            if hasattr(self.buyer_tel, 'to_alipay_dict'):
                params['buyer_tel'] = self.buyer_tel.to_alipay_dict()
            else:
                params['buyer_tel'] = self.buyer_tel
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.title_type:
            if hasattr(self.title_type, 'to_alipay_dict'):
                params['title_type'] = self.title_type.to_alipay_dict()
            else:
                params['title_type'] = self.title_type
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
        o = AlipayCommerceTransportEtcenterpriseInvoicetitleModifyModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'buyer_addr' in d:
            o.buyer_addr = d['buyer_addr']
        if 'buyer_bank' in d:
            o.buyer_bank = d['buyer_bank']
        if 'buyer_bank_account' in d:
            o.buyer_bank_account = d['buyer_bank_account']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_tax_num' in d:
            o.buyer_tax_num = d['buyer_tax_num']
        if 'buyer_tel' in d:
            o.buyer_tel = d['buyer_tel']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'email' in d:
            o.email = d['email']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'title_type' in d:
            o.title_type = d['title_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


