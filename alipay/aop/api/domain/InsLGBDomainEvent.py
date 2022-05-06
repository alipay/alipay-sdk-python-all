#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsEmployee import InsEmployee
from alipay.aop.api.domain.InsCompany import InsCompany


class InsLGBDomainEvent(object):

    def __init__(self):
        self._employee = None
        self._event_place = None
        self._event_time = None
        self._event_type = None
        self._merchant = None
        self._product_plan_id = None

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, value):
        if isinstance(value, InsEmployee):
            self._employee = value
        else:
            self._employee = InsEmployee.from_alipay_dict(value)
    @property
    def event_place(self):
        return self._event_place

    @event_place.setter
    def event_place(self, value):
        self._event_place = value
    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsCompany):
            self._merchant = value
        else:
            self._merchant = InsCompany.from_alipay_dict(value)
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee:
            if hasattr(self.employee, 'to_alipay_dict'):
                params['employee'] = self.employee.to_alipay_dict()
            else:
                params['employee'] = self.employee
        if self.event_place:
            if hasattr(self.event_place, 'to_alipay_dict'):
                params['event_place'] = self.event_place.to_alipay_dict()
            else:
                params['event_place'] = self.event_place
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsLGBDomainEvent()
        if 'employee' in d:
            o.employee = d['employee']
        if 'event_place' in d:
            o.event_place = d['event_place']
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        return o


