#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DoctorDepartmentScheduleDetailDTO import DoctorDepartmentScheduleDetailDTO


class DoctorHospitalCampusScheduleDetailDTO(object):

    def __init__(self):
        self._department_schedule_list = None
        self._distance = None
        self._hospital_id = None
        self._platform_code = None
        self._sub_hospital_shore_name = None
        self._sub_hospital_uniq_code = None

    @property
    def department_schedule_list(self):
        return self._department_schedule_list

    @department_schedule_list.setter
    def department_schedule_list(self, value):
        if isinstance(value, list):
            self._department_schedule_list = list()
            for i in value:
                if isinstance(i, DoctorDepartmentScheduleDetailDTO):
                    self._department_schedule_list.append(i)
                else:
                    self._department_schedule_list.append(DoctorDepartmentScheduleDetailDTO.from_alipay_dict(i))
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def sub_hospital_shore_name(self):
        return self._sub_hospital_shore_name

    @sub_hospital_shore_name.setter
    def sub_hospital_shore_name(self, value):
        self._sub_hospital_shore_name = value
    @property
    def sub_hospital_uniq_code(self):
        return self._sub_hospital_uniq_code

    @sub_hospital_uniq_code.setter
    def sub_hospital_uniq_code(self, value):
        self._sub_hospital_uniq_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_schedule_list:
            if isinstance(self.department_schedule_list, list):
                for i in range(0, len(self.department_schedule_list)):
                    element = self.department_schedule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_schedule_list[i] = element.to_alipay_dict()
            if hasattr(self.department_schedule_list, 'to_alipay_dict'):
                params['department_schedule_list'] = self.department_schedule_list.to_alipay_dict()
            else:
                params['department_schedule_list'] = self.department_schedule_list
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.sub_hospital_shore_name:
            if hasattr(self.sub_hospital_shore_name, 'to_alipay_dict'):
                params['sub_hospital_shore_name'] = self.sub_hospital_shore_name.to_alipay_dict()
            else:
                params['sub_hospital_shore_name'] = self.sub_hospital_shore_name
        if self.sub_hospital_uniq_code:
            if hasattr(self.sub_hospital_uniq_code, 'to_alipay_dict'):
                params['sub_hospital_uniq_code'] = self.sub_hospital_uniq_code.to_alipay_dict()
            else:
                params['sub_hospital_uniq_code'] = self.sub_hospital_uniq_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorHospitalCampusScheduleDetailDTO()
        if 'department_schedule_list' in d:
            o.department_schedule_list = d['department_schedule_list']
        if 'distance' in d:
            o.distance = d['distance']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'sub_hospital_shore_name' in d:
            o.sub_hospital_shore_name = d['sub_hospital_shore_name']
        if 'sub_hospital_uniq_code' in d:
            o.sub_hospital_uniq_code = d['sub_hospital_uniq_code']
        return o


