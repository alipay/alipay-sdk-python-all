#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentOrderSettleTargetDTO import RentOrderSettleTargetDTO


class RentOrderSettleInfoDTO(object):

    def __init__(self):
        self._out_trade_no = None
        self._settle_amount = None
        self._settle_target = None
        self._trade_no = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_target(self):
        return self._settle_target

    @settle_target.setter
    def settle_target(self, value):
        if isinstance(value, RentOrderSettleTargetDTO):
            self._settle_target = value
        else:
            self._settle_target = RentOrderSettleTargetDTO.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_target:
            if hasattr(self.settle_target, 'to_alipay_dict'):
                params['settle_target'] = self.settle_target.to_alipay_dict()
            else:
                params['settle_target'] = self.settle_target
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
        o = RentOrderSettleInfoDTO()
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_target' in d:
            o.settle_target = d['settle_target']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


