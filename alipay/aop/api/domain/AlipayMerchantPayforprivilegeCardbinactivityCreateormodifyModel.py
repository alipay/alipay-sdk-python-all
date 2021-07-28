#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantPayforprivilegeCardbinactivityCreateormodifyModel(object):

    def __init__(self):
        self._bank_code = None
        self._card_bin = None
        self._out_biz_no = None

    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def card_bin(self):
        return self._card_bin

    @card_bin.setter
    def card_bin(self, value):
        self._card_bin = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.card_bin:
            if hasattr(self.card_bin, 'to_alipay_dict'):
                params['card_bin'] = self.card_bin.to_alipay_dict()
            else:
                params['card_bin'] = self.card_bin
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantPayforprivilegeCardbinactivityCreateormodifyModel()
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'card_bin' in d:
            o.card_bin = d['card_bin']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


