#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtBankInstInfo(object):

    def __init__(self):
        self._bank_card_type_list = None
        self._bank_name = None

    @property
    def bank_card_type_list(self):
        return self._bank_card_type_list

    @bank_card_type_list.setter
    def bank_card_type_list(self, value):
        if isinstance(value, list):
            self._bank_card_type_list = list()
            for i in value:
                self._bank_card_type_list.append(i)
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_type_list:
            if isinstance(self.bank_card_type_list, list):
                for i in range(0, len(self.bank_card_type_list)):
                    element = self.bank_card_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_card_type_list[i] = element.to_alipay_dict()
            if hasattr(self.bank_card_type_list, 'to_alipay_dict'):
                params['bank_card_type_list'] = self.bank_card_type_list.to_alipay_dict()
            else:
                params['bank_card_type_list'] = self.bank_card_type_list
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankInstInfo()
        if 'bank_card_type_list' in d:
            o.bank_card_type_list = d['bank_card_type_list']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        return o


