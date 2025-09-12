#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorBankCardDTO(object):

    def __init__(self):
        self._bank_contract_id = None
        self._inst_id = None
        self._inst_name = None
        self._show_card_no = None

    @property
    def bank_contract_id(self):
        return self._bank_contract_id

    @bank_contract_id.setter
    def bank_contract_id(self, value):
        self._bank_contract_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def show_card_no(self):
        return self._show_card_no

    @show_card_no.setter
    def show_card_no(self, value):
        self._show_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_contract_id:
            if hasattr(self.bank_contract_id, 'to_alipay_dict'):
                params['bank_contract_id'] = self.bank_contract_id.to_alipay_dict()
            else:
                params['bank_contract_id'] = self.bank_contract_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.show_card_no:
            if hasattr(self.show_card_no, 'to_alipay_dict'):
                params['show_card_no'] = self.show_card_no.to_alipay_dict()
            else:
                params['show_card_no'] = self.show_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorBankCardDTO()
        if 'bank_contract_id' in d:
            o.bank_contract_id = d['bank_contract_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'show_card_no' in d:
            o.show_card_no = d['show_card_no']
        return o


