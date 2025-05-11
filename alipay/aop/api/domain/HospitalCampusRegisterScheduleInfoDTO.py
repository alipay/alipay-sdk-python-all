#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RegisterScheduleDateDTO import RegisterScheduleDateDTO


class HospitalCampusRegisterScheduleInfoDTO(object):

    def __init__(self):
        self._distance = None
        self._schedule_date_list = None
        self._sub_hospital_shore_name = None
        self._sub_hospital_uniq_code = None

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def schedule_date_list(self):
        return self._schedule_date_list

    @schedule_date_list.setter
    def schedule_date_list(self, value):
        if isinstance(value, list):
            self._schedule_date_list = list()
            for i in value:
                if isinstance(i, RegisterScheduleDateDTO):
                    self._schedule_date_list.append(i)
                else:
                    self._schedule_date_list.append(RegisterScheduleDateDTO.from_alipay_dict(i))
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
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
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
        o = HospitalCampusRegisterScheduleInfoDTO()
        if 'distance' in d:
            o.distance = d['distance']
        if 'schedule_date_list' in d:
            o.schedule_date_list = d['schedule_date_list']
        if 'sub_hospital_shore_name' in d:
            o.sub_hospital_shore_name = d['sub_hospital_shore_name']
        if 'sub_hospital_uniq_code' in d:
            o.sub_hospital_uniq_code = d['sub_hospital_uniq_code']
        return o


