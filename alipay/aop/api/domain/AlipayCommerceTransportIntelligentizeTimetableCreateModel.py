#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimeTableLineInfo import TimeTableLineInfo


class AlipayCommerceTransportIntelligentizeTimetableCreateModel(object):

    def __init__(self):
        self._city_code = None
        self._corp_id = None
        self._ext_param = None
        self._line_info_list = None
        self._request_id = None
        self._service_task_name = None
        self._timetable_task_type = None

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
    def line_info_list(self):
        return self._line_info_list

    @line_info_list.setter
    def line_info_list(self, value):
        if isinstance(value, list):
            self._line_info_list = list()
            for i in value:
                if isinstance(i, TimeTableLineInfo):
                    self._line_info_list.append(i)
                else:
                    self._line_info_list.append(TimeTableLineInfo.from_alipay_dict(i))
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
    def timetable_task_type(self):
        return self._timetable_task_type

    @timetable_task_type.setter
    def timetable_task_type(self, value):
        self._timetable_task_type = value


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
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_info_list:
            if isinstance(self.line_info_list, list):
                for i in range(0, len(self.line_info_list)):
                    element = self.line_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.line_info_list[i] = element.to_alipay_dict()
            if hasattr(self.line_info_list, 'to_alipay_dict'):
                params['line_info_list'] = self.line_info_list.to_alipay_dict()
            else:
                params['line_info_list'] = self.line_info_list
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
        if self.timetable_task_type:
            if hasattr(self.timetable_task_type, 'to_alipay_dict'):
                params['timetable_task_type'] = self.timetable_task_type.to_alipay_dict()
            else:
                params['timetable_task_type'] = self.timetable_task_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeTimetableCreateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_info_list' in d:
            o.line_info_list = d['line_info_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_task_name' in d:
            o.service_task_name = d['service_task_name']
        if 'timetable_task_type' in d:
            o.timetable_task_type = d['timetable_task_type']
        return o


