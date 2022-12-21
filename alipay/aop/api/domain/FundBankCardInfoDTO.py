#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundBankCardInfoDTO(object):

    def __init__(self):
        self._bank_card_no = None
        self._bank_name = None
        self._inst_account_name = None
        self._inst_id = None

    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def inst_account_name(self):
        return self._inst_account_name

    @inst_account_name.setter
    def inst_account_name(self, value):
        self._inst_account_name = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.inst_account_name:
            if hasattr(self.inst_account_name, 'to_alipay_dict'):
                params['inst_account_name'] = self.inst_account_name.to_alipay_dict()
            else:
                params['inst_account_name'] = self.inst_account_name
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundBankCardInfoDTO()
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'inst_account_name' in d:
            o.inst_account_name = d['inst_account_name']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        return o


