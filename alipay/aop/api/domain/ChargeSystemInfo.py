#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargeSystemInfo(object):

    def __init__(self):
        self._ac_pile_num = None
        self._dc_pile_num = None
        self._electric_meter_no = None
        self._orderable = None
        self._park_num = None
        self._system_category = None
        self._total_rated_power = None
        self._use_type = None
        self._voltag_level = None

    @property
    def ac_pile_num(self):
        return self._ac_pile_num

    @ac_pile_num.setter
    def ac_pile_num(self, value):
        self._ac_pile_num = value
    @property
    def dc_pile_num(self):
        return self._dc_pile_num

    @dc_pile_num.setter
    def dc_pile_num(self, value):
        self._dc_pile_num = value
    @property
    def electric_meter_no(self):
        return self._electric_meter_no

    @electric_meter_no.setter
    def electric_meter_no(self, value):
        if isinstance(value, list):
            self._electric_meter_no = list()
            for i in value:
                self._electric_meter_no.append(i)
    @property
    def orderable(self):
        return self._orderable

    @orderable.setter
    def orderable(self, value):
        self._orderable = value
    @property
    def park_num(self):
        return self._park_num

    @park_num.setter
    def park_num(self, value):
        self._park_num = value
    @property
    def system_category(self):
        return self._system_category

    @system_category.setter
    def system_category(self, value):
        self._system_category = value
    @property
    def total_rated_power(self):
        return self._total_rated_power

    @total_rated_power.setter
    def total_rated_power(self, value):
        self._total_rated_power = value
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value
    @property
    def voltag_level(self):
        return self._voltag_level

    @voltag_level.setter
    def voltag_level(self, value):
        self._voltag_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.ac_pile_num:
            if hasattr(self.ac_pile_num, 'to_alipay_dict'):
                params['ac_pile_num'] = self.ac_pile_num.to_alipay_dict()
            else:
                params['ac_pile_num'] = self.ac_pile_num
        if self.dc_pile_num:
            if hasattr(self.dc_pile_num, 'to_alipay_dict'):
                params['dc_pile_num'] = self.dc_pile_num.to_alipay_dict()
            else:
                params['dc_pile_num'] = self.dc_pile_num
        if self.electric_meter_no:
            if isinstance(self.electric_meter_no, list):
                for i in range(0, len(self.electric_meter_no)):
                    element = self.electric_meter_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.electric_meter_no[i] = element.to_alipay_dict()
            if hasattr(self.electric_meter_no, 'to_alipay_dict'):
                params['electric_meter_no'] = self.electric_meter_no.to_alipay_dict()
            else:
                params['electric_meter_no'] = self.electric_meter_no
        if self.orderable:
            if hasattr(self.orderable, 'to_alipay_dict'):
                params['orderable'] = self.orderable.to_alipay_dict()
            else:
                params['orderable'] = self.orderable
        if self.park_num:
            if hasattr(self.park_num, 'to_alipay_dict'):
                params['park_num'] = self.park_num.to_alipay_dict()
            else:
                params['park_num'] = self.park_num
        if self.system_category:
            if hasattr(self.system_category, 'to_alipay_dict'):
                params['system_category'] = self.system_category.to_alipay_dict()
            else:
                params['system_category'] = self.system_category
        if self.total_rated_power:
            if hasattr(self.total_rated_power, 'to_alipay_dict'):
                params['total_rated_power'] = self.total_rated_power.to_alipay_dict()
            else:
                params['total_rated_power'] = self.total_rated_power
        if self.use_type:
            if hasattr(self.use_type, 'to_alipay_dict'):
                params['use_type'] = self.use_type.to_alipay_dict()
            else:
                params['use_type'] = self.use_type
        if self.voltag_level:
            if hasattr(self.voltag_level, 'to_alipay_dict'):
                params['voltag_level'] = self.voltag_level.to_alipay_dict()
            else:
                params['voltag_level'] = self.voltag_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeSystemInfo()
        if 'ac_pile_num' in d:
            o.ac_pile_num = d['ac_pile_num']
        if 'dc_pile_num' in d:
            o.dc_pile_num = d['dc_pile_num']
        if 'electric_meter_no' in d:
            o.electric_meter_no = d['electric_meter_no']
        if 'orderable' in d:
            o.orderable = d['orderable']
        if 'park_num' in d:
            o.park_num = d['park_num']
        if 'system_category' in d:
            o.system_category = d['system_category']
        if 'total_rated_power' in d:
            o.total_rated_power = d['total_rated_power']
        if 'use_type' in d:
            o.use_type = d['use_type']
        if 'voltag_level' in d:
            o.voltag_level = d['voltag_level']
        return o


