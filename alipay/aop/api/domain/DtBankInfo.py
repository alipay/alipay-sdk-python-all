#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankInstInfo import DtBankInstInfo


class DtBankInfo(object):

    def __init__(self):
        self._bank_inst_info_list = None
        self._card_bin_list = None

    @property
    def bank_inst_info_list(self):
        return self._bank_inst_info_list

    @bank_inst_info_list.setter
    def bank_inst_info_list(self, value):
        if isinstance(value, list):
            self._bank_inst_info_list = list()
            for i in value:
                if isinstance(i, DtBankInstInfo):
                    self._bank_inst_info_list.append(i)
                else:
                    self._bank_inst_info_list.append(DtBankInstInfo.from_alipay_dict(i))
    @property
    def card_bin_list(self):
        return self._card_bin_list

    @card_bin_list.setter
    def card_bin_list(self, value):
        if isinstance(value, list):
            self._card_bin_list = list()
            for i in value:
                self._card_bin_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.bank_inst_info_list:
            if isinstance(self.bank_inst_info_list, list):
                for i in range(0, len(self.bank_inst_info_list)):
                    element = self.bank_inst_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_inst_info_list[i] = element.to_alipay_dict()
            if hasattr(self.bank_inst_info_list, 'to_alipay_dict'):
                params['bank_inst_info_list'] = self.bank_inst_info_list.to_alipay_dict()
            else:
                params['bank_inst_info_list'] = self.bank_inst_info_list
        if self.card_bin_list:
            if isinstance(self.card_bin_list, list):
                for i in range(0, len(self.card_bin_list)):
                    element = self.card_bin_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_bin_list[i] = element.to_alipay_dict()
            if hasattr(self.card_bin_list, 'to_alipay_dict'):
                params['card_bin_list'] = self.card_bin_list.to_alipay_dict()
            else:
                params['card_bin_list'] = self.card_bin_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankInfo()
        if 'bank_inst_info_list' in d:
            o.bank_inst_info_list = d['bank_inst_info_list']
        if 'card_bin_list' in d:
            o.card_bin_list = d['card_bin_list']
        return o


