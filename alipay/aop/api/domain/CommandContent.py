#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommandContent(object):

    def __init__(self):
        self._energy_save_mode = None
        self._power_switch = None
        self._target_temperature = None
        self._wind_speed = None
        self._work_mode = None

    @property
    def energy_save_mode(self):
        return self._energy_save_mode

    @energy_save_mode.setter
    def energy_save_mode(self, value):
        self._energy_save_mode = value
    @property
    def power_switch(self):
        return self._power_switch

    @power_switch.setter
    def power_switch(self, value):
        self._power_switch = value
    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        self._target_temperature = value
    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value
    @property
    def work_mode(self):
        return self._work_mode

    @work_mode.setter
    def work_mode(self, value):
        self._work_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.energy_save_mode:
            if hasattr(self.energy_save_mode, 'to_alipay_dict'):
                params['energy_save_mode'] = self.energy_save_mode.to_alipay_dict()
            else:
                params['energy_save_mode'] = self.energy_save_mode
        if self.power_switch:
            if hasattr(self.power_switch, 'to_alipay_dict'):
                params['power_switch'] = self.power_switch.to_alipay_dict()
            else:
                params['power_switch'] = self.power_switch
        if self.target_temperature:
            if hasattr(self.target_temperature, 'to_alipay_dict'):
                params['target_temperature'] = self.target_temperature.to_alipay_dict()
            else:
                params['target_temperature'] = self.target_temperature
        if self.wind_speed:
            if hasattr(self.wind_speed, 'to_alipay_dict'):
                params['wind_speed'] = self.wind_speed.to_alipay_dict()
            else:
                params['wind_speed'] = self.wind_speed
        if self.work_mode:
            if hasattr(self.work_mode, 'to_alipay_dict'):
                params['work_mode'] = self.work_mode.to_alipay_dict()
            else:
                params['work_mode'] = self.work_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommandContent()
        if 'energy_save_mode' in d:
            o.energy_save_mode = d['energy_save_mode']
        if 'power_switch' in d:
            o.power_switch = d['power_switch']
        if 'target_temperature' in d:
            o.target_temperature = d['target_temperature']
        if 'wind_speed' in d:
            o.wind_speed = d['wind_speed']
        if 'work_mode' in d:
            o.work_mode = d['work_mode']
        return o


