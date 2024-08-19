#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardCycle(object):

    def __init__(self):
        self._charge_now = None
        self._cycle_charge_type = None
        self._cycle_type = None
        self._cycle_value = None
        self._period_item_type = None
        self._user_select_range_start = None

    @property
    def charge_now(self):
        return self._charge_now

    @charge_now.setter
    def charge_now(self, value):
        self._charge_now = value
    @property
    def cycle_charge_type(self):
        return self._cycle_charge_type

    @cycle_charge_type.setter
    def cycle_charge_type(self, value):
        self._cycle_charge_type = value
    @property
    def cycle_type(self):
        return self._cycle_type

    @cycle_type.setter
    def cycle_type(self, value):
        self._cycle_type = value
    @property
    def cycle_value(self):
        return self._cycle_value

    @cycle_value.setter
    def cycle_value(self, value):
        self._cycle_value = value
    @property
    def period_item_type(self):
        return self._period_item_type

    @period_item_type.setter
    def period_item_type(self, value):
        self._period_item_type = value
    @property
    def user_select_range_start(self):
        return self._user_select_range_start

    @user_select_range_start.setter
    def user_select_range_start(self, value):
        self._user_select_range_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_now:
            if hasattr(self.charge_now, 'to_alipay_dict'):
                params['charge_now'] = self.charge_now.to_alipay_dict()
            else:
                params['charge_now'] = self.charge_now
        if self.cycle_charge_type:
            if hasattr(self.cycle_charge_type, 'to_alipay_dict'):
                params['cycle_charge_type'] = self.cycle_charge_type.to_alipay_dict()
            else:
                params['cycle_charge_type'] = self.cycle_charge_type
        if self.cycle_type:
            if hasattr(self.cycle_type, 'to_alipay_dict'):
                params['cycle_type'] = self.cycle_type.to_alipay_dict()
            else:
                params['cycle_type'] = self.cycle_type
        if self.cycle_value:
            if hasattr(self.cycle_value, 'to_alipay_dict'):
                params['cycle_value'] = self.cycle_value.to_alipay_dict()
            else:
                params['cycle_value'] = self.cycle_value
        if self.period_item_type:
            if hasattr(self.period_item_type, 'to_alipay_dict'):
                params['period_item_type'] = self.period_item_type.to_alipay_dict()
            else:
                params['period_item_type'] = self.period_item_type
        if self.user_select_range_start:
            if hasattr(self.user_select_range_start, 'to_alipay_dict'):
                params['user_select_range_start'] = self.user_select_range_start.to_alipay_dict()
            else:
                params['user_select_range_start'] = self.user_select_range_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardCycle()
        if 'charge_now' in d:
            o.charge_now = d['charge_now']
        if 'cycle_charge_type' in d:
            o.cycle_charge_type = d['cycle_charge_type']
        if 'cycle_type' in d:
            o.cycle_type = d['cycle_type']
        if 'cycle_value' in d:
            o.cycle_value = d['cycle_value']
        if 'period_item_type' in d:
            o.period_item_type = d['period_item_type']
        if 'user_select_range_start' in d:
            o.user_select_range_start = d['user_select_range_start']
        return o


