#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsPayeeDTO(object):

    def __init__(self):
        self._alipay_id = None
        self._alipay_open_id = None
        self._bank_card_holder_name = None
        self._bank_card_no = None
        self._bank_id = None
        self._bank_name = None
        self._bill_account_type = None
        self._payee_user_id = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def bank_card_holder_name(self):
        return self._bank_card_holder_name

    @bank_card_holder_name.setter
    def bank_card_holder_name(self, value):
        self._bank_card_holder_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bill_account_type(self):
        return self._bill_account_type

    @bill_account_type.setter
    def bill_account_type(self, value):
        self._bill_account_type = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.bank_card_holder_name:
            if hasattr(self.bank_card_holder_name, 'to_alipay_dict'):
                params['bank_card_holder_name'] = self.bank_card_holder_name.to_alipay_dict()
            else:
                params['bank_card_holder_name'] = self.bank_card_holder_name
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_id:
            if hasattr(self.bank_id, 'to_alipay_dict'):
                params['bank_id'] = self.bank_id.to_alipay_dict()
            else:
                params['bank_id'] = self.bank_id
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.bill_account_type:
            if hasattr(self.bill_account_type, 'to_alipay_dict'):
                params['bill_account_type'] = self.bill_account_type.to_alipay_dict()
            else:
                params['bill_account_type'] = self.bill_account_type
        if self.payee_user_id:
            if hasattr(self.payee_user_id, 'to_alipay_dict'):
                params['payee_user_id'] = self.payee_user_id.to_alipay_dict()
            else:
                params['payee_user_id'] = self.payee_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPayeeDTO()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'bank_card_holder_name' in d:
            o.bank_card_holder_name = d['bank_card_holder_name']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_id' in d:
            o.bank_id = d['bank_id']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'bill_account_type' in d:
            o.bill_account_type = d['bill_account_type']
        if 'payee_user_id' in d:
            o.payee_user_id = d['payee_user_id']
        return o


