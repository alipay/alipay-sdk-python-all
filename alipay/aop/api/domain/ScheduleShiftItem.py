#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleShiftItem(object):

    def __init__(self):
        self._chain_num = None
        self._day_num = None
        self._line_id = None
        self._vehicle_id = None
        self._vir_employ_id = None

    @property
    def chain_num(self):
        return self._chain_num

    @chain_num.setter
    def chain_num(self, value):
        self._chain_num = value
    @property
    def day_num(self):
        return self._day_num

    @day_num.setter
    def day_num(self, value):
        self._day_num = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value
    @property
    def vir_employ_id(self):
        return self._vir_employ_id

    @vir_employ_id.setter
    def vir_employ_id(self, value):
        self._vir_employ_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chain_num:
            if hasattr(self.chain_num, 'to_alipay_dict'):
                params['chain_num'] = self.chain_num.to_alipay_dict()
            else:
                params['chain_num'] = self.chain_num
        if self.day_num:
            if hasattr(self.day_num, 'to_alipay_dict'):
                params['day_num'] = self.day_num.to_alipay_dict()
            else:
                params['day_num'] = self.day_num
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.vehicle_id:
            if hasattr(self.vehicle_id, 'to_alipay_dict'):
                params['vehicle_id'] = self.vehicle_id.to_alipay_dict()
            else:
                params['vehicle_id'] = self.vehicle_id
        if self.vir_employ_id:
            if hasattr(self.vir_employ_id, 'to_alipay_dict'):
                params['vir_employ_id'] = self.vir_employ_id.to_alipay_dict()
            else:
                params['vir_employ_id'] = self.vir_employ_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleShiftItem()
        if 'chain_num' in d:
            o.chain_num = d['chain_num']
        if 'day_num' in d:
            o.day_num = d['day_num']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'vehicle_id' in d:
            o.vehicle_id = d['vehicle_id']
        if 'vir_employ_id' in d:
            o.vir_employ_id = d['vir_employ_id']
        return o


