#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditTradePayExtendParams(object):

    def __init__(self):
        self._credit_trade_phase = None
        self._credit_trade_scene = None
        self._pay_solution = None
        self._pay_solution_config = None

    @property
    def credit_trade_phase(self):
        return self._credit_trade_phase

    @credit_trade_phase.setter
    def credit_trade_phase(self, value):
        self._credit_trade_phase = value
    @property
    def credit_trade_scene(self):
        return self._credit_trade_scene

    @credit_trade_scene.setter
    def credit_trade_scene(self, value):
        self._credit_trade_scene = value
    @property
    def pay_solution(self):
        return self._pay_solution

    @pay_solution.setter
    def pay_solution(self, value):
        self._pay_solution = value
    @property
    def pay_solution_config(self):
        return self._pay_solution_config

    @pay_solution_config.setter
    def pay_solution_config(self, value):
        self._pay_solution_config = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_trade_phase:
            if hasattr(self.credit_trade_phase, 'to_alipay_dict'):
                params['credit_trade_phase'] = self.credit_trade_phase.to_alipay_dict()
            else:
                params['credit_trade_phase'] = self.credit_trade_phase
        if self.credit_trade_scene:
            if hasattr(self.credit_trade_scene, 'to_alipay_dict'):
                params['credit_trade_scene'] = self.credit_trade_scene.to_alipay_dict()
            else:
                params['credit_trade_scene'] = self.credit_trade_scene
        if self.pay_solution:
            if hasattr(self.pay_solution, 'to_alipay_dict'):
                params['pay_solution'] = self.pay_solution.to_alipay_dict()
            else:
                params['pay_solution'] = self.pay_solution
        if self.pay_solution_config:
            if hasattr(self.pay_solution_config, 'to_alipay_dict'):
                params['pay_solution_config'] = self.pay_solution_config.to_alipay_dict()
            else:
                params['pay_solution_config'] = self.pay_solution_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditTradePayExtendParams()
        if 'credit_trade_phase' in d:
            o.credit_trade_phase = d['credit_trade_phase']
        if 'credit_trade_scene' in d:
            o.credit_trade_scene = d['credit_trade_scene']
        if 'pay_solution' in d:
            o.pay_solution = d['pay_solution']
        if 'pay_solution_config' in d:
            o.pay_solution_config = d['pay_solution_config']
        return o


