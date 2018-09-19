#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduKtBillingQueryModel(object):

    def __init__(self):
        self._isv_pid = None
        self._out_trade_no = None
        self._school_pid = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtBillingQueryModel()
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        return o


