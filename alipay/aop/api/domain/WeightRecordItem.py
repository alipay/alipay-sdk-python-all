#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WeightRecordItem(object):

    def __init__(self):
        self._record_date = None
        self._record_id = None
        self._record_time = None
        self._unit = None
        self._weight_value = None

    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def record_time(self):
        return self._record_time

    @record_time.setter
    def record_time(self, value):
        self._record_time = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def weight_value(self):
        return self._weight_value

    @weight_value.setter
    def weight_value(self, value):
        self._weight_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.record_date:
            if hasattr(self.record_date, 'to_alipay_dict'):
                params['record_date'] = self.record_date.to_alipay_dict()
            else:
                params['record_date'] = self.record_date
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.record_time:
            if hasattr(self.record_time, 'to_alipay_dict'):
                params['record_time'] = self.record_time.to_alipay_dict()
            else:
                params['record_time'] = self.record_time
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.weight_value:
            if hasattr(self.weight_value, 'to_alipay_dict'):
                params['weight_value'] = self.weight_value.to_alipay_dict()
            else:
                params['weight_value'] = self.weight_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WeightRecordItem()
        if 'record_date' in d:
            o.record_date = d['record_date']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'record_time' in d:
            o.record_time = d['record_time']
        if 'unit' in d:
            o.unit = d['unit']
        if 'weight_value' in d:
            o.weight_value = d['weight_value']
        return o


