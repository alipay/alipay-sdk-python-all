#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AcChargePileRunTimeData(object):

    def __init__(self):
        self._adjust_down = None
        self._adjust_up = None
        self._cumulative_power = None
        self._current_a = None
        self._current_b = None
        self._current_c = None
        self._out_entity_id = None
        self._power = None
        self._pwm_duty_cycle = None
        self._voltage_a = None
        self._voltage_b = None
        self._voltage_c = None

    @property
    def adjust_down(self):
        return self._adjust_down

    @adjust_down.setter
    def adjust_down(self, value):
        self._adjust_down = value
    @property
    def adjust_up(self):
        return self._adjust_up

    @adjust_up.setter
    def adjust_up(self, value):
        self._adjust_up = value
    @property
    def cumulative_power(self):
        return self._cumulative_power

    @cumulative_power.setter
    def cumulative_power(self, value):
        self._cumulative_power = value
    @property
    def current_a(self):
        return self._current_a

    @current_a.setter
    def current_a(self, value):
        self._current_a = value
    @property
    def current_b(self):
        return self._current_b

    @current_b.setter
    def current_b(self, value):
        self._current_b = value
    @property
    def current_c(self):
        return self._current_c

    @current_c.setter
    def current_c(self, value):
        self._current_c = value
    @property
    def out_entity_id(self):
        return self._out_entity_id

    @out_entity_id.setter
    def out_entity_id(self, value):
        self._out_entity_id = value
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value
    @property
    def pwm_duty_cycle(self):
        return self._pwm_duty_cycle

    @pwm_duty_cycle.setter
    def pwm_duty_cycle(self, value):
        self._pwm_duty_cycle = value
    @property
    def voltage_a(self):
        return self._voltage_a

    @voltage_a.setter
    def voltage_a(self, value):
        self._voltage_a = value
    @property
    def voltage_b(self):
        return self._voltage_b

    @voltage_b.setter
    def voltage_b(self, value):
        self._voltage_b = value
    @property
    def voltage_c(self):
        return self._voltage_c

    @voltage_c.setter
    def voltage_c(self, value):
        self._voltage_c = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_down:
            if hasattr(self.adjust_down, 'to_alipay_dict'):
                params['adjust_down'] = self.adjust_down.to_alipay_dict()
            else:
                params['adjust_down'] = self.adjust_down
        if self.adjust_up:
            if hasattr(self.adjust_up, 'to_alipay_dict'):
                params['adjust_up'] = self.adjust_up.to_alipay_dict()
            else:
                params['adjust_up'] = self.adjust_up
        if self.cumulative_power:
            if hasattr(self.cumulative_power, 'to_alipay_dict'):
                params['cumulative_power'] = self.cumulative_power.to_alipay_dict()
            else:
                params['cumulative_power'] = self.cumulative_power
        if self.current_a:
            if hasattr(self.current_a, 'to_alipay_dict'):
                params['current_a'] = self.current_a.to_alipay_dict()
            else:
                params['current_a'] = self.current_a
        if self.current_b:
            if hasattr(self.current_b, 'to_alipay_dict'):
                params['current_b'] = self.current_b.to_alipay_dict()
            else:
                params['current_b'] = self.current_b
        if self.current_c:
            if hasattr(self.current_c, 'to_alipay_dict'):
                params['current_c'] = self.current_c.to_alipay_dict()
            else:
                params['current_c'] = self.current_c
        if self.out_entity_id:
            if hasattr(self.out_entity_id, 'to_alipay_dict'):
                params['out_entity_id'] = self.out_entity_id.to_alipay_dict()
            else:
                params['out_entity_id'] = self.out_entity_id
        if self.power:
            if hasattr(self.power, 'to_alipay_dict'):
                params['power'] = self.power.to_alipay_dict()
            else:
                params['power'] = self.power
        if self.pwm_duty_cycle:
            if hasattr(self.pwm_duty_cycle, 'to_alipay_dict'):
                params['pwm_duty_cycle'] = self.pwm_duty_cycle.to_alipay_dict()
            else:
                params['pwm_duty_cycle'] = self.pwm_duty_cycle
        if self.voltage_a:
            if hasattr(self.voltage_a, 'to_alipay_dict'):
                params['voltage_a'] = self.voltage_a.to_alipay_dict()
            else:
                params['voltage_a'] = self.voltage_a
        if self.voltage_b:
            if hasattr(self.voltage_b, 'to_alipay_dict'):
                params['voltage_b'] = self.voltage_b.to_alipay_dict()
            else:
                params['voltage_b'] = self.voltage_b
        if self.voltage_c:
            if hasattr(self.voltage_c, 'to_alipay_dict'):
                params['voltage_c'] = self.voltage_c.to_alipay_dict()
            else:
                params['voltage_c'] = self.voltage_c
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AcChargePileRunTimeData()
        if 'adjust_down' in d:
            o.adjust_down = d['adjust_down']
        if 'adjust_up' in d:
            o.adjust_up = d['adjust_up']
        if 'cumulative_power' in d:
            o.cumulative_power = d['cumulative_power']
        if 'current_a' in d:
            o.current_a = d['current_a']
        if 'current_b' in d:
            o.current_b = d['current_b']
        if 'current_c' in d:
            o.current_c = d['current_c']
        if 'out_entity_id' in d:
            o.out_entity_id = d['out_entity_id']
        if 'power' in d:
            o.power = d['power']
        if 'pwm_duty_cycle' in d:
            o.pwm_duty_cycle = d['pwm_duty_cycle']
        if 'voltage_a' in d:
            o.voltage_a = d['voltage_a']
        if 'voltage_b' in d:
            o.voltage_b = d['voltage_b']
        if 'voltage_c' in d:
            o.voltage_c = d['voltage_c']
        return o


