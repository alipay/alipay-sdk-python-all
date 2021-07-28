#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserTwostageCommonUseModel(object):

    def __init__(self):
        self._dynamic_id = None
        self._pay_check_strategy = None
        self._pay_pid = None
        self._sence_no = None

    @property
    def dynamic_id(self):
        return self._dynamic_id

    @dynamic_id.setter
    def dynamic_id(self, value):
        self._dynamic_id = value
    @property
    def pay_check_strategy(self):
        return self._pay_check_strategy

    @pay_check_strategy.setter
    def pay_check_strategy(self, value):
        self._pay_check_strategy = value
    @property
    def pay_pid(self):
        return self._pay_pid

    @pay_pid.setter
    def pay_pid(self, value):
        self._pay_pid = value
    @property
    def sence_no(self):
        return self._sence_no

    @sence_no.setter
    def sence_no(self, value):
        self._sence_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.dynamic_id:
            if hasattr(self.dynamic_id, 'to_alipay_dict'):
                params['dynamic_id'] = self.dynamic_id.to_alipay_dict()
            else:
                params['dynamic_id'] = self.dynamic_id
        if self.pay_check_strategy:
            if hasattr(self.pay_check_strategy, 'to_alipay_dict'):
                params['pay_check_strategy'] = self.pay_check_strategy.to_alipay_dict()
            else:
                params['pay_check_strategy'] = self.pay_check_strategy
        if self.pay_pid:
            if hasattr(self.pay_pid, 'to_alipay_dict'):
                params['pay_pid'] = self.pay_pid.to_alipay_dict()
            else:
                params['pay_pid'] = self.pay_pid
        if self.sence_no:
            if hasattr(self.sence_no, 'to_alipay_dict'):
                params['sence_no'] = self.sence_no.to_alipay_dict()
            else:
                params['sence_no'] = self.sence_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserTwostageCommonUseModel()
        if 'dynamic_id' in d:
            o.dynamic_id = d['dynamic_id']
        if 'pay_check_strategy' in d:
            o.pay_check_strategy = d['pay_check_strategy']
        if 'pay_pid' in d:
            o.pay_pid = d['pay_pid']
        if 'sence_no' in d:
            o.sence_no = d['sence_no']
        return o


