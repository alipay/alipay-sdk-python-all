#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DoctorHospitalCampusScheduleDetailDTO import DoctorHospitalCampusScheduleDetailDTO


class DoctorHospitalScheduleInfoDTO(object):

    def __init__(self):
        self._hospital_name = None
        self._main_hos_uniq_code = None
        self._sub_hospital_register_info_list = None

    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def main_hos_uniq_code(self):
        return self._main_hos_uniq_code

    @main_hos_uniq_code.setter
    def main_hos_uniq_code(self, value):
        self._main_hos_uniq_code = value
    @property
    def sub_hospital_register_info_list(self):
        return self._sub_hospital_register_info_list

    @sub_hospital_register_info_list.setter
    def sub_hospital_register_info_list(self, value):
        if isinstance(value, list):
            self._sub_hospital_register_info_list = list()
            for i in value:
                if isinstance(i, DoctorHospitalCampusScheduleDetailDTO):
                    self._sub_hospital_register_info_list.append(i)
                else:
                    self._sub_hospital_register_info_list.append(DoctorHospitalCampusScheduleDetailDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.main_hos_uniq_code:
            if hasattr(self.main_hos_uniq_code, 'to_alipay_dict'):
                params['main_hos_uniq_code'] = self.main_hos_uniq_code.to_alipay_dict()
            else:
                params['main_hos_uniq_code'] = self.main_hos_uniq_code
        if self.sub_hospital_register_info_list:
            if isinstance(self.sub_hospital_register_info_list, list):
                for i in range(0, len(self.sub_hospital_register_info_list)):
                    element = self.sub_hospital_register_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_hospital_register_info_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_hospital_register_info_list, 'to_alipay_dict'):
                params['sub_hospital_register_info_list'] = self.sub_hospital_register_info_list.to_alipay_dict()
            else:
                params['sub_hospital_register_info_list'] = self.sub_hospital_register_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorHospitalScheduleInfoDTO()
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'main_hos_uniq_code' in d:
            o.main_hos_uniq_code = d['main_hos_uniq_code']
        if 'sub_hospital_register_info_list' in d:
            o.sub_hospital_register_info_list = d['sub_hospital_register_info_list']
        return o


