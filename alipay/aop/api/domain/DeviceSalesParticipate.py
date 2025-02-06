#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceSalesParticipate(object):

    def __init__(self):
        self._activity_id = None
        self._sales_entry_order_id = None
        self._solution_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def sales_entry_order_id(self):
        return self._sales_entry_order_id

    @sales_entry_order_id.setter
    def sales_entry_order_id(self, value):
        self._sales_entry_order_id = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.sales_entry_order_id:
            if hasattr(self.sales_entry_order_id, 'to_alipay_dict'):
                params['sales_entry_order_id'] = self.sales_entry_order_id.to_alipay_dict()
            else:
                params['sales_entry_order_id'] = self.sales_entry_order_id
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceSalesParticipate()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'sales_entry_order_id' in d:
            o.sales_entry_order_id = d['sales_entry_order_id']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        return o


