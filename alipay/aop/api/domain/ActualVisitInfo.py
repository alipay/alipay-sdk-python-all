#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActualVisitInfo(object):

    def __init__(self):
        self._actual_city = None
        self._actual_department = None
        self._actual_hospital = None
        self._doctor_title = None
        self._expert = None
        self._hospital_address = None
        self._user_desc = None
        self._visit_end_time = None
        self._visit_start_time = None

    @property
    def actual_city(self):
        return self._actual_city

    @actual_city.setter
    def actual_city(self, value):
        self._actual_city = value
    @property
    def actual_department(self):
        return self._actual_department

    @actual_department.setter
    def actual_department(self, value):
        self._actual_department = value
    @property
    def actual_hospital(self):
        return self._actual_hospital

    @actual_hospital.setter
    def actual_hospital(self, value):
        self._actual_hospital = value
    @property
    def doctor_title(self):
        return self._doctor_title

    @doctor_title.setter
    def doctor_title(self, value):
        self._doctor_title = value
    @property
    def expert(self):
        return self._expert

    @expert.setter
    def expert(self, value):
        self._expert = value
    @property
    def hospital_address(self):
        return self._hospital_address

    @hospital_address.setter
    def hospital_address(self, value):
        self._hospital_address = value
    @property
    def user_desc(self):
        return self._user_desc

    @user_desc.setter
    def user_desc(self, value):
        self._user_desc = value
    @property
    def visit_end_time(self):
        return self._visit_end_time

    @visit_end_time.setter
    def visit_end_time(self, value):
        self._visit_end_time = value
    @property
    def visit_start_time(self):
        return self._visit_start_time

    @visit_start_time.setter
    def visit_start_time(self, value):
        self._visit_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_city:
            if hasattr(self.actual_city, 'to_alipay_dict'):
                params['actual_city'] = self.actual_city.to_alipay_dict()
            else:
                params['actual_city'] = self.actual_city
        if self.actual_department:
            if hasattr(self.actual_department, 'to_alipay_dict'):
                params['actual_department'] = self.actual_department.to_alipay_dict()
            else:
                params['actual_department'] = self.actual_department
        if self.actual_hospital:
            if hasattr(self.actual_hospital, 'to_alipay_dict'):
                params['actual_hospital'] = self.actual_hospital.to_alipay_dict()
            else:
                params['actual_hospital'] = self.actual_hospital
        if self.doctor_title:
            if hasattr(self.doctor_title, 'to_alipay_dict'):
                params['doctor_title'] = self.doctor_title.to_alipay_dict()
            else:
                params['doctor_title'] = self.doctor_title
        if self.expert:
            if hasattr(self.expert, 'to_alipay_dict'):
                params['expert'] = self.expert.to_alipay_dict()
            else:
                params['expert'] = self.expert
        if self.hospital_address:
            if hasattr(self.hospital_address, 'to_alipay_dict'):
                params['hospital_address'] = self.hospital_address.to_alipay_dict()
            else:
                params['hospital_address'] = self.hospital_address
        if self.user_desc:
            if hasattr(self.user_desc, 'to_alipay_dict'):
                params['user_desc'] = self.user_desc.to_alipay_dict()
            else:
                params['user_desc'] = self.user_desc
        if self.visit_end_time:
            if hasattr(self.visit_end_time, 'to_alipay_dict'):
                params['visit_end_time'] = self.visit_end_time.to_alipay_dict()
            else:
                params['visit_end_time'] = self.visit_end_time
        if self.visit_start_time:
            if hasattr(self.visit_start_time, 'to_alipay_dict'):
                params['visit_start_time'] = self.visit_start_time.to_alipay_dict()
            else:
                params['visit_start_time'] = self.visit_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActualVisitInfo()
        if 'actual_city' in d:
            o.actual_city = d['actual_city']
        if 'actual_department' in d:
            o.actual_department = d['actual_department']
        if 'actual_hospital' in d:
            o.actual_hospital = d['actual_hospital']
        if 'doctor_title' in d:
            o.doctor_title = d['doctor_title']
        if 'expert' in d:
            o.expert = d['expert']
        if 'hospital_address' in d:
            o.hospital_address = d['hospital_address']
        if 'user_desc' in d:
            o.user_desc = d['user_desc']
        if 'visit_end_time' in d:
            o.visit_end_time = d['visit_end_time']
        if 'visit_start_time' in d:
            o.visit_start_time = d['visit_start_time']
        return o


