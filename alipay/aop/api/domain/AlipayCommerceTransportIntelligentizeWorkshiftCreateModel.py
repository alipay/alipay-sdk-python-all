#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WorkShiftParam import WorkShiftParam


class AlipayCommerceTransportIntelligentizeWorkshiftCreateModel(object):

    def __init__(self):
        self._city_code = None
        self._corp_id = None
        self._down_driver_count = None
        self._ext_param = None
        self._line_driver_count = None
        self._line_key = None
        self._request_id = None
        self._service_task_name = None
        self._up_driver_count = None
        self._work_shift_param_list = None

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
    def down_driver_count(self):
        return self._down_driver_count

    @down_driver_count.setter
    def down_driver_count(self, value):
        self._down_driver_count = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_driver_count(self):
        return self._line_driver_count

    @line_driver_count.setter
    def line_driver_count(self, value):
        self._line_driver_count = value
    @property
    def line_key(self):
        return self._line_key

    @line_key.setter
    def line_key(self, value):
        self._line_key = value
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
    def up_driver_count(self):
        return self._up_driver_count

    @up_driver_count.setter
    def up_driver_count(self, value):
        self._up_driver_count = value
    @property
    def work_shift_param_list(self):
        return self._work_shift_param_list

    @work_shift_param_list.setter
    def work_shift_param_list(self, value):
        if isinstance(value, list):
            self._work_shift_param_list = list()
            for i in value:
                if isinstance(i, WorkShiftParam):
                    self._work_shift_param_list.append(i)
                else:
                    self._work_shift_param_list.append(WorkShiftParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        if self.down_driver_count:
            if hasattr(self.down_driver_count, 'to_alipay_dict'):
                params['down_driver_count'] = self.down_driver_count.to_alipay_dict()
            else:
                params['down_driver_count'] = self.down_driver_count
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_driver_count:
            if hasattr(self.line_driver_count, 'to_alipay_dict'):
                params['line_driver_count'] = self.line_driver_count.to_alipay_dict()
            else:
                params['line_driver_count'] = self.line_driver_count
        if self.line_key:
            if hasattr(self.line_key, 'to_alipay_dict'):
                params['line_key'] = self.line_key.to_alipay_dict()
            else:
                params['line_key'] = self.line_key
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
        if self.up_driver_count:
            if hasattr(self.up_driver_count, 'to_alipay_dict'):
                params['up_driver_count'] = self.up_driver_count.to_alipay_dict()
            else:
                params['up_driver_count'] = self.up_driver_count
        if self.work_shift_param_list:
            if isinstance(self.work_shift_param_list, list):
                for i in range(0, len(self.work_shift_param_list)):
                    element = self.work_shift_param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_shift_param_list[i] = element.to_alipay_dict()
            if hasattr(self.work_shift_param_list, 'to_alipay_dict'):
                params['work_shift_param_list'] = self.work_shift_param_list.to_alipay_dict()
            else:
                params['work_shift_param_list'] = self.work_shift_param_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeWorkshiftCreateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'down_driver_count' in d:
            o.down_driver_count = d['down_driver_count']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_driver_count' in d:
            o.line_driver_count = d['line_driver_count']
        if 'line_key' in d:
            o.line_key = d['line_key']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_task_name' in d:
            o.service_task_name = d['service_task_name']
        if 'up_driver_count' in d:
            o.up_driver_count = d['up_driver_count']
        if 'work_shift_param_list' in d:
            o.work_shift_param_list = d['work_shift_param_list']
        return o


