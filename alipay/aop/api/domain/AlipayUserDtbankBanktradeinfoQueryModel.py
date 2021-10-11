#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankBanktradeinfoQueryModel(object):

    def __init__(self):
        self._bank_inst_id = None
        self._trade_no = None

    @property
    def bank_inst_id(self):
        return self._bank_inst_id

    @bank_inst_id.setter
    def bank_inst_id(self, value):
        self._bank_inst_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_inst_id:
            if hasattr(self.bank_inst_id, 'to_alipay_dict'):
                params['bank_inst_id'] = self.bank_inst_id.to_alipay_dict()
            else:
                params['bank_inst_id'] = self.bank_inst_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDtbankBanktradeinfoQueryModel()
        if 'bank_inst_id' in d:
            o.bank_inst_id = d['bank_inst_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


