#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MyBkAccountVO(object):

    def __init__(self):
        self._account_ext_no = None
        self._account_fip_branch_code = None
        self._account_fip_code = None
        self._account_fip_name = None
        self._account_no = None
        self._account_type = None
        self._available = None
        self._bank_card_category = None
        self._card_holder_name = None
        self._grant_channel = None
        self._refuse_code = None

    @property
    def account_ext_no(self):
        return self._account_ext_no

    @account_ext_no.setter
    def account_ext_no(self, value):
        self._account_ext_no = value
    @property
    def account_fip_branch_code(self):
        return self._account_fip_branch_code

    @account_fip_branch_code.setter
    def account_fip_branch_code(self, value):
        self._account_fip_branch_code = value
    @property
    def account_fip_code(self):
        return self._account_fip_code

    @account_fip_code.setter
    def account_fip_code(self, value):
        self._account_fip_code = value
    @property
    def account_fip_name(self):
        return self._account_fip_name

    @account_fip_name.setter
    def account_fip_name(self, value):
        self._account_fip_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
    @property
    def bank_card_category(self):
        return self._bank_card_category

    @bank_card_category.setter
    def bank_card_category(self, value):
        self._bank_card_category = value
    @property
    def card_holder_name(self):
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value):
        self._card_holder_name = value
    @property
    def grant_channel(self):
        return self._grant_channel

    @grant_channel.setter
    def grant_channel(self, value):
        self._grant_channel = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_ext_no:
            if hasattr(self.account_ext_no, 'to_alipay_dict'):
                params['account_ext_no'] = self.account_ext_no.to_alipay_dict()
            else:
                params['account_ext_no'] = self.account_ext_no
        if self.account_fip_branch_code:
            if hasattr(self.account_fip_branch_code, 'to_alipay_dict'):
                params['account_fip_branch_code'] = self.account_fip_branch_code.to_alipay_dict()
            else:
                params['account_fip_branch_code'] = self.account_fip_branch_code
        if self.account_fip_code:
            if hasattr(self.account_fip_code, 'to_alipay_dict'):
                params['account_fip_code'] = self.account_fip_code.to_alipay_dict()
            else:
                params['account_fip_code'] = self.account_fip_code
        if self.account_fip_name:
            if hasattr(self.account_fip_name, 'to_alipay_dict'):
                params['account_fip_name'] = self.account_fip_name.to_alipay_dict()
            else:
                params['account_fip_name'] = self.account_fip_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.available:
            if hasattr(self.available, 'to_alipay_dict'):
                params['available'] = self.available.to_alipay_dict()
            else:
                params['available'] = self.available
        if self.bank_card_category:
            if hasattr(self.bank_card_category, 'to_alipay_dict'):
                params['bank_card_category'] = self.bank_card_category.to_alipay_dict()
            else:
                params['bank_card_category'] = self.bank_card_category
        if self.card_holder_name:
            if hasattr(self.card_holder_name, 'to_alipay_dict'):
                params['card_holder_name'] = self.card_holder_name.to_alipay_dict()
            else:
                params['card_holder_name'] = self.card_holder_name
        if self.grant_channel:
            if hasattr(self.grant_channel, 'to_alipay_dict'):
                params['grant_channel'] = self.grant_channel.to_alipay_dict()
            else:
                params['grant_channel'] = self.grant_channel
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MyBkAccountVO()
        if 'account_ext_no' in d:
            o.account_ext_no = d['account_ext_no']
        if 'account_fip_branch_code' in d:
            o.account_fip_branch_code = d['account_fip_branch_code']
        if 'account_fip_code' in d:
            o.account_fip_code = d['account_fip_code']
        if 'account_fip_name' in d:
            o.account_fip_name = d['account_fip_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'available' in d:
            o.available = d['available']
        if 'bank_card_category' in d:
            o.bank_card_category = d['bank_card_category']
        if 'card_holder_name' in d:
            o.card_holder_name = d['card_holder_name']
        if 'grant_channel' in d:
            o.grant_channel = d['grant_channel']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        return o


