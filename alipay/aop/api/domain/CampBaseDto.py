#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityOrderDTO import ActivityOrderDTO


class CampBaseDto(object):

    def __init__(self):
        self._activity_orders = None
        self._audit_status = None
        self._auto_delay_flag = None
        self._end_time = None
        self._id = None
        self._name = None
        self._plan_status = None
        self._start_time = None
        self._status = None
        self._type = None

    @property
    def activity_orders(self):
        return self._activity_orders

    @activity_orders.setter
    def activity_orders(self, value):
        if isinstance(value, list):
            self._activity_orders = list()
            for i in value:
                if isinstance(i, ActivityOrderDTO):
                    self._activity_orders.append(i)
                else:
                    self._activity_orders.append(ActivityOrderDTO.from_alipay_dict(i))
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def auto_delay_flag(self):
        return self._auto_delay_flag

    @auto_delay_flag.setter
    def auto_delay_flag(self, value):
        self._auto_delay_flag = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def plan_status(self):
        return self._plan_status

    @plan_status.setter
    def plan_status(self, value):
        self._plan_status = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_orders:
            if isinstance(self.activity_orders, list):
                for i in range(0, len(self.activity_orders)):
                    element = self.activity_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_orders[i] = element.to_alipay_dict()
            if hasattr(self.activity_orders, 'to_alipay_dict'):
                params['activity_orders'] = self.activity_orders.to_alipay_dict()
            else:
                params['activity_orders'] = self.activity_orders
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.auto_delay_flag:
            if hasattr(self.auto_delay_flag, 'to_alipay_dict'):
                params['auto_delay_flag'] = self.auto_delay_flag.to_alipay_dict()
            else:
                params['auto_delay_flag'] = self.auto_delay_flag
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.plan_status:
            if hasattr(self.plan_status, 'to_alipay_dict'):
                params['plan_status'] = self.plan_status.to_alipay_dict()
            else:
                params['plan_status'] = self.plan_status
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CampBaseDto()
        if 'activity_orders' in d:
            o.activity_orders = d['activity_orders']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'auto_delay_flag' in d:
            o.auto_delay_flag = d['auto_delay_flag']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'plan_status' in d:
            o.plan_status = d['plan_status']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


