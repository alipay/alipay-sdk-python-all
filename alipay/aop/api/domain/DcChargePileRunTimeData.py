#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DcChargePileRunTimeData(object):

    def __init__(self):
        self._adjust_down = None
        self._adjust_up = None
        self._cumulative_power = None
        self._output_current = None
        self._output_voltage = None
        self._power = None
        self._remain_time = None
        self._request_current = None
        self._request_voltage = None
        self._vehicle_soc_values = None
        self._vin_code = None

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
    def output_current(self):
        return self._output_current

    @output_current.setter
    def output_current(self, value):
        self._output_current = value
    @property
    def output_voltage(self):
        return self._output_voltage

    @output_voltage.setter
    def output_voltage(self, value):
        self._output_voltage = value
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value
    @property
    def remain_time(self):
        return self._remain_time

    @remain_time.setter
    def remain_time(self, value):
        self._remain_time = value
    @property
    def request_current(self):
        return self._request_current

    @request_current.setter
    def request_current(self, value):
        self._request_current = value
    @property
    def request_voltage(self):
        return self._request_voltage

    @request_voltage.setter
    def request_voltage(self, value):
        self._request_voltage = value
    @property
    def vehicle_soc_values(self):
        return self._vehicle_soc_values

    @vehicle_soc_values.setter
    def vehicle_soc_values(self, value):
        self._vehicle_soc_values = value
    @property
    def vin_code(self):
        return self._vin_code

    @vin_code.setter
    def vin_code(self, value):
        self._vin_code = value


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
        if self.output_current:
            if hasattr(self.output_current, 'to_alipay_dict'):
                params['output_current'] = self.output_current.to_alipay_dict()
            else:
                params['output_current'] = self.output_current
        if self.output_voltage:
            if hasattr(self.output_voltage, 'to_alipay_dict'):
                params['output_voltage'] = self.output_voltage.to_alipay_dict()
            else:
                params['output_voltage'] = self.output_voltage
        if self.power:
            if hasattr(self.power, 'to_alipay_dict'):
                params['power'] = self.power.to_alipay_dict()
            else:
                params['power'] = self.power
        if self.remain_time:
            if hasattr(self.remain_time, 'to_alipay_dict'):
                params['remain_time'] = self.remain_time.to_alipay_dict()
            else:
                params['remain_time'] = self.remain_time
        if self.request_current:
            if hasattr(self.request_current, 'to_alipay_dict'):
                params['request_current'] = self.request_current.to_alipay_dict()
            else:
                params['request_current'] = self.request_current
        if self.request_voltage:
            if hasattr(self.request_voltage, 'to_alipay_dict'):
                params['request_voltage'] = self.request_voltage.to_alipay_dict()
            else:
                params['request_voltage'] = self.request_voltage
        if self.vehicle_soc_values:
            if hasattr(self.vehicle_soc_values, 'to_alipay_dict'):
                params['vehicle_soc_values'] = self.vehicle_soc_values.to_alipay_dict()
            else:
                params['vehicle_soc_values'] = self.vehicle_soc_values
        if self.vin_code:
            if hasattr(self.vin_code, 'to_alipay_dict'):
                params['vin_code'] = self.vin_code.to_alipay_dict()
            else:
                params['vin_code'] = self.vin_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DcChargePileRunTimeData()
        if 'adjust_down' in d:
            o.adjust_down = d['adjust_down']
        if 'adjust_up' in d:
            o.adjust_up = d['adjust_up']
        if 'cumulative_power' in d:
            o.cumulative_power = d['cumulative_power']
        if 'output_current' in d:
            o.output_current = d['output_current']
        if 'output_voltage' in d:
            o.output_voltage = d['output_voltage']
        if 'power' in d:
            o.power = d['power']
        if 'remain_time' in d:
            o.remain_time = d['remain_time']
        if 'request_current' in d:
            o.request_current = d['request_current']
        if 'request_voltage' in d:
            o.request_voltage = d['request_voltage']
        if 'vehicle_soc_values' in d:
            o.vehicle_soc_values = d['vehicle_soc_values']
        if 'vin_code' in d:
            o.vin_code = d['vin_code']
        return o


