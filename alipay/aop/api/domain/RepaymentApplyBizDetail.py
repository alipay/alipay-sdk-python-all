#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepaymentApplyBizDetail(object):

    def __init__(self):
        self._current_amt = None
        self._install_num = None
        self._trade_no = None

    @property
    def current_amt(self):
        return self._current_amt

    @current_amt.setter
    def current_amt(self, value):
        self._current_amt = value
    @property
    def install_num(self):
        return self._install_num

    @install_num.setter
    def install_num(self, value):
        self._install_num = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_amt:
            if hasattr(self.current_amt, 'to_alipay_dict'):
                params['current_amt'] = self.current_amt.to_alipay_dict()
            else:
                params['current_amt'] = self.current_amt
        if self.install_num:
            if hasattr(self.install_num, 'to_alipay_dict'):
                params['install_num'] = self.install_num.to_alipay_dict()
            else:
                params['install_num'] = self.install_num
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
        o = RepaymentApplyBizDetail()
        if 'current_amt' in d:
            o.current_amt = d['current_amt']
        if 'install_num' in d:
            o.install_num = d['install_num']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


