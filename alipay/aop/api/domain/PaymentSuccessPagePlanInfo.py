#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentSuccessPagePlanInfo(object):

    def __init__(self):
        self._activity_id = None
        self._activity_status = None
        self._begin_time = None
        self._end_time = None
        self._oper_app_id = None
        self._plan_id = None
        self._plan_name = None
        self._priority = None
        self._reject_reason = None
        self._service_list = None
        self._status = None
        self._type = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def oper_app_id(self):
        return self._oper_app_id

    @oper_app_id.setter
    def oper_app_id(self, value):
        self._oper_app_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                self._service_list.append(i)
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
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_status:
            if hasattr(self.activity_status, 'to_alipay_dict'):
                params['activity_status'] = self.activity_status.to_alipay_dict()
            else:
                params['activity_status'] = self.activity_status
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.oper_app_id:
            if hasattr(self.oper_app_id, 'to_alipay_dict'):
                params['oper_app_id'] = self.oper_app_id.to_alipay_dict()
            else:
                params['oper_app_id'] = self.oper_app_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.service_list:
            if isinstance(self.service_list, list):
                for i in range(0, len(self.service_list)):
                    element = self.service_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_list[i] = element.to_alipay_dict()
            if hasattr(self.service_list, 'to_alipay_dict'):
                params['service_list'] = self.service_list.to_alipay_dict()
            else:
                params['service_list'] = self.service_list
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
        o = PaymentSuccessPagePlanInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_status' in d:
            o.activity_status = d['activity_status']
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'oper_app_id' in d:
            o.oper_app_id = d['oper_app_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'priority' in d:
            o.priority = d['priority']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'service_list' in d:
            o.service_list = d['service_list']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


