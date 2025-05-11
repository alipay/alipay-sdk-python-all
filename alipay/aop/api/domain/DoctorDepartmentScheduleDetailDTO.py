#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DoctorRegisterScheduleDateDTO import DoctorRegisterScheduleDateDTO


class DoctorDepartmentScheduleDetailDTO(object):

    def __init__(self):
        self._department_id = None
        self._department_name = None
        self._schedule_date_list = None

    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def schedule_date_list(self):
        return self._schedule_date_list

    @schedule_date_list.setter
    def schedule_date_list(self, value):
        if isinstance(value, list):
            self._schedule_date_list = list()
            for i in value:
                if isinstance(i, DoctorRegisterScheduleDateDTO):
                    self._schedule_date_list.append(i)
                else:
                    self._schedule_date_list.append(DoctorRegisterScheduleDateDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.schedule_date_list:
            if isinstance(self.schedule_date_list, list):
                for i in range(0, len(self.schedule_date_list)):
                    element = self.schedule_date_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schedule_date_list[i] = element.to_alipay_dict()
            if hasattr(self.schedule_date_list, 'to_alipay_dict'):
                params['schedule_date_list'] = self.schedule_date_list.to_alipay_dict()
            else:
                params['schedule_date_list'] = self.schedule_date_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorDepartmentScheduleDetailDTO()
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'schedule_date_list' in d:
            o.schedule_date_list = d['schedule_date_list']
        return o


