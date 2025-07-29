#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RcDoctorLicenseRequest(object):

    def __init__(self):
        self._doctor_id = None
        self._doctor_name = None
        self._gender = None
        self._job_title = None
        self._license_no = None
        self._main_department = None
        self._main_hospital = None
        self._province = None
        self._second_hos_list = None

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def main_department(self):
        return self._main_department

    @main_department.setter
    def main_department(self, value):
        self._main_department = value
    @property
    def main_hospital(self):
        return self._main_hospital

    @main_hospital.setter
    def main_hospital(self, value):
        self._main_hospital = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def second_hos_list(self):
        return self._second_hos_list

    @second_hos_list.setter
    def second_hos_list(self, value):
        if isinstance(value, list):
            self._second_hos_list = list()
            for i in value:
                self._second_hos_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.job_title:
            if hasattr(self.job_title, 'to_alipay_dict'):
                params['job_title'] = self.job_title.to_alipay_dict()
            else:
                params['job_title'] = self.job_title
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.main_department:
            if hasattr(self.main_department, 'to_alipay_dict'):
                params['main_department'] = self.main_department.to_alipay_dict()
            else:
                params['main_department'] = self.main_department
        if self.main_hospital:
            if hasattr(self.main_hospital, 'to_alipay_dict'):
                params['main_hospital'] = self.main_hospital.to_alipay_dict()
            else:
                params['main_hospital'] = self.main_hospital
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.second_hos_list:
            if isinstance(self.second_hos_list, list):
                for i in range(0, len(self.second_hos_list)):
                    element = self.second_hos_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.second_hos_list[i] = element.to_alipay_dict()
            if hasattr(self.second_hos_list, 'to_alipay_dict'):
                params['second_hos_list'] = self.second_hos_list.to_alipay_dict()
            else:
                params['second_hos_list'] = self.second_hos_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcDoctorLicenseRequest()
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'gender' in d:
            o.gender = d['gender']
        if 'job_title' in d:
            o.job_title = d['job_title']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'main_department' in d:
            o.main_department = d['main_department']
        if 'main_hospital' in d:
            o.main_hospital = d['main_hospital']
        if 'province' in d:
            o.province = d['province']
        if 'second_hos_list' in d:
            o.second_hos_list = d['second_hos_list']
        return o


