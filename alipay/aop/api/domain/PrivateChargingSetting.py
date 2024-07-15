#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrivateChargingSetting(object):

    def __init__(self):
        self._cycle_mode = None
        self._end_time = None
        self._mode = None
        self._reservation_flag = None
        self._start_time = None
        self._strategy = None

    @property
    def cycle_mode(self):
        return self._cycle_mode

    @cycle_mode.setter
    def cycle_mode(self, value):
        self._cycle_mode = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if isinstance(value, list):
            self._mode = list()
            for i in value:
                self._mode.append(i)
    @property
    def reservation_flag(self):
        return self._reservation_flag

    @reservation_flag.setter
    def reservation_flag(self, value):
        self._reservation_flag = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_mode:
            if hasattr(self.cycle_mode, 'to_alipay_dict'):
                params['cycle_mode'] = self.cycle_mode.to_alipay_dict()
            else:
                params['cycle_mode'] = self.cycle_mode
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.mode:
            if isinstance(self.mode, list):
                for i in range(0, len(self.mode)):
                    element = self.mode[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mode[i] = element.to_alipay_dict()
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.reservation_flag:
            if hasattr(self.reservation_flag, 'to_alipay_dict'):
                params['reservation_flag'] = self.reservation_flag.to_alipay_dict()
            else:
                params['reservation_flag'] = self.reservation_flag
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.strategy:
            if hasattr(self.strategy, 'to_alipay_dict'):
                params['strategy'] = self.strategy.to_alipay_dict()
            else:
                params['strategy'] = self.strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrivateChargingSetting()
        if 'cycle_mode' in d:
            o.cycle_mode = d['cycle_mode']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'mode' in d:
            o.mode = d['mode']
        if 'reservation_flag' in d:
            o.reservation_flag = d['reservation_flag']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'strategy' in d:
            o.strategy = d['strategy']
        return o


