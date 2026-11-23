#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HomedoctorServicePlanDTO(object):

    def __init__(self):
        self._fee = None
        self._notice = None
        self._period = None
        self._service_desc = None
        self._service_plan_id = None
        self._service_plan_name = None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def service_plan_id(self):
        return self._service_plan_id

    @service_plan_id.setter
    def service_plan_id(self, value):
        self._service_plan_id = value
    @property
    def service_plan_name(self):
        return self._service_plan_name

    @service_plan_name.setter
    def service_plan_name(self, value):
        self._service_plan_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.service_plan_id:
            if hasattr(self.service_plan_id, 'to_alipay_dict'):
                params['service_plan_id'] = self.service_plan_id.to_alipay_dict()
            else:
                params['service_plan_id'] = self.service_plan_id
        if self.service_plan_name:
            if hasattr(self.service_plan_name, 'to_alipay_dict'):
                params['service_plan_name'] = self.service_plan_name.to_alipay_dict()
            else:
                params['service_plan_name'] = self.service_plan_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HomedoctorServicePlanDTO()
        if 'fee' in d:
            o.fee = d['fee']
        if 'notice' in d:
            o.notice = d['notice']
        if 'period' in d:
            o.period = d['period']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_plan_id' in d:
            o.service_plan_id = d['service_plan_id']
        if 'service_plan_name' in d:
            o.service_plan_name = d['service_plan_name']
        return o


