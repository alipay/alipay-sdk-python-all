#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WorkSchedulePlan import WorkSchedulePlan


class AlipayCommerceTransportIntelligentizeChargescheduleCreateModel(object):

    def __init__(self):
        self._charge_schedule_mode = None
        self._city_code = None
        self._corp_id = None
        self._ext_param = None
        self._request_id = None
        self._service_task_name = None
        self._work_schedule_plan_list = None

    @property
    def charge_schedule_mode(self):
        return self._charge_schedule_mode

    @charge_schedule_mode.setter
    def charge_schedule_mode(self, value):
        self._charge_schedule_mode = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def service_task_name(self):
        return self._service_task_name

    @service_task_name.setter
    def service_task_name(self, value):
        self._service_task_name = value
    @property
    def work_schedule_plan_list(self):
        return self._work_schedule_plan_list

    @work_schedule_plan_list.setter
    def work_schedule_plan_list(self, value):
        if isinstance(value, list):
            self._work_schedule_plan_list = list()
            for i in value:
                if isinstance(i, WorkSchedulePlan):
                    self._work_schedule_plan_list.append(i)
                else:
                    self._work_schedule_plan_list.append(WorkSchedulePlan.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.charge_schedule_mode:
            if hasattr(self.charge_schedule_mode, 'to_alipay_dict'):
                params['charge_schedule_mode'] = self.charge_schedule_mode.to_alipay_dict()
            else:
                params['charge_schedule_mode'] = self.charge_schedule_mode
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.service_task_name:
            if hasattr(self.service_task_name, 'to_alipay_dict'):
                params['service_task_name'] = self.service_task_name.to_alipay_dict()
            else:
                params['service_task_name'] = self.service_task_name
        if self.work_schedule_plan_list:
            if isinstance(self.work_schedule_plan_list, list):
                for i in range(0, len(self.work_schedule_plan_list)):
                    element = self.work_schedule_plan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_schedule_plan_list[i] = element.to_alipay_dict()
            if hasattr(self.work_schedule_plan_list, 'to_alipay_dict'):
                params['work_schedule_plan_list'] = self.work_schedule_plan_list.to_alipay_dict()
            else:
                params['work_schedule_plan_list'] = self.work_schedule_plan_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeChargescheduleCreateModel()
        if 'charge_schedule_mode' in d:
            o.charge_schedule_mode = d['charge_schedule_mode']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_task_name' in d:
            o.service_task_name = d['service_task_name']
        if 'work_schedule_plan_list' in d:
            o.work_schedule_plan_list = d['work_schedule_plan_list']
        return o


