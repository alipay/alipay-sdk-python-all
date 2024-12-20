#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode


class EvaluateResult(object):

    def __init__(self):
        self._actual_energy = None
        self._estimate_profit = None
        self._evaluate_adjustment = None
        self._evaluate_load = None
        self._ratio = None
        self._real_energy = None
        self._real_load = None
        self._response_end_time = None
        self._response_start_time = None
        self._target_energy = None
        self._target_load = None

    @property
    def actual_energy(self):
        return self._actual_energy

    @actual_energy.setter
    def actual_energy(self, value):
        self._actual_energy = value
    @property
    def estimate_profit(self):
        return self._estimate_profit

    @estimate_profit.setter
    def estimate_profit(self, value):
        self._estimate_profit = value
    @property
    def evaluate_adjustment(self):
        return self._evaluate_adjustment

    @evaluate_adjustment.setter
    def evaluate_adjustment(self, value):
        if isinstance(value, list):
            self._evaluate_adjustment = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._evaluate_adjustment.append(i)
                else:
                    self._evaluate_adjustment.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def evaluate_load(self):
        return self._evaluate_load

    @evaluate_load.setter
    def evaluate_load(self, value):
        if isinstance(value, list):
            self._evaluate_load = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._evaluate_load.append(i)
                else:
                    self._evaluate_load.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value
    @property
    def real_energy(self):
        return self._real_energy

    @real_energy.setter
    def real_energy(self, value):
        self._real_energy = value
    @property
    def real_load(self):
        return self._real_load

    @real_load.setter
    def real_load(self, value):
        self._real_load = value
    @property
    def response_end_time(self):
        return self._response_end_time

    @response_end_time.setter
    def response_end_time(self, value):
        self._response_end_time = value
    @property
    def response_start_time(self):
        return self._response_start_time

    @response_start_time.setter
    def response_start_time(self, value):
        self._response_start_time = value
    @property
    def target_energy(self):
        return self._target_energy

    @target_energy.setter
    def target_energy(self, value):
        self._target_energy = value
    @property
    def target_load(self):
        return self._target_load

    @target_load.setter
    def target_load(self, value):
        self._target_load = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_energy:
            if hasattr(self.actual_energy, 'to_alipay_dict'):
                params['actual_energy'] = self.actual_energy.to_alipay_dict()
            else:
                params['actual_energy'] = self.actual_energy
        if self.estimate_profit:
            if hasattr(self.estimate_profit, 'to_alipay_dict'):
                params['estimate_profit'] = self.estimate_profit.to_alipay_dict()
            else:
                params['estimate_profit'] = self.estimate_profit
        if self.evaluate_adjustment:
            if isinstance(self.evaluate_adjustment, list):
                for i in range(0, len(self.evaluate_adjustment)):
                    element = self.evaluate_adjustment[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.evaluate_adjustment[i] = element.to_alipay_dict()
            if hasattr(self.evaluate_adjustment, 'to_alipay_dict'):
                params['evaluate_adjustment'] = self.evaluate_adjustment.to_alipay_dict()
            else:
                params['evaluate_adjustment'] = self.evaluate_adjustment
        if self.evaluate_load:
            if isinstance(self.evaluate_load, list):
                for i in range(0, len(self.evaluate_load)):
                    element = self.evaluate_load[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.evaluate_load[i] = element.to_alipay_dict()
            if hasattr(self.evaluate_load, 'to_alipay_dict'):
                params['evaluate_load'] = self.evaluate_load.to_alipay_dict()
            else:
                params['evaluate_load'] = self.evaluate_load
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        if self.real_energy:
            if hasattr(self.real_energy, 'to_alipay_dict'):
                params['real_energy'] = self.real_energy.to_alipay_dict()
            else:
                params['real_energy'] = self.real_energy
        if self.real_load:
            if hasattr(self.real_load, 'to_alipay_dict'):
                params['real_load'] = self.real_load.to_alipay_dict()
            else:
                params['real_load'] = self.real_load
        if self.response_end_time:
            if hasattr(self.response_end_time, 'to_alipay_dict'):
                params['response_end_time'] = self.response_end_time.to_alipay_dict()
            else:
                params['response_end_time'] = self.response_end_time
        if self.response_start_time:
            if hasattr(self.response_start_time, 'to_alipay_dict'):
                params['response_start_time'] = self.response_start_time.to_alipay_dict()
            else:
                params['response_start_time'] = self.response_start_time
        if self.target_energy:
            if hasattr(self.target_energy, 'to_alipay_dict'):
                params['target_energy'] = self.target_energy.to_alipay_dict()
            else:
                params['target_energy'] = self.target_energy
        if self.target_load:
            if hasattr(self.target_load, 'to_alipay_dict'):
                params['target_load'] = self.target_load.to_alipay_dict()
            else:
                params['target_load'] = self.target_load
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvaluateResult()
        if 'actual_energy' in d:
            o.actual_energy = d['actual_energy']
        if 'estimate_profit' in d:
            o.estimate_profit = d['estimate_profit']
        if 'evaluate_adjustment' in d:
            o.evaluate_adjustment = d['evaluate_adjustment']
        if 'evaluate_load' in d:
            o.evaluate_load = d['evaluate_load']
        if 'ratio' in d:
            o.ratio = d['ratio']
        if 'real_energy' in d:
            o.real_energy = d['real_energy']
        if 'real_load' in d:
            o.real_load = d['real_load']
        if 'response_end_time' in d:
            o.response_end_time = d['response_end_time']
        if 'response_start_time' in d:
            o.response_start_time = d['response_start_time']
        if 'target_energy' in d:
            o.target_energy = d['target_energy']
        if 'target_load' in d:
            o.target_load = d['target_load']
        return o


