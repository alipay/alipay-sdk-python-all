#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FulfillmentStaffInfo(object):

    def __init__(self):
        self._department = None
        self._organization = None
        self._phone = None
        self._service_count = None
        self._staff_name = None
        self._title = None
        self._work_years = None

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        self._organization = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def service_count(self):
        return self._service_count

    @service_count.setter
    def service_count(self, value):
        self._service_count = value
    @property
    def staff_name(self):
        return self._staff_name

    @staff_name.setter
    def staff_name(self, value):
        self._staff_name = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def work_years(self):
        return self._work_years

    @work_years.setter
    def work_years(self, value):
        self._work_years = value


    def to_alipay_dict(self):
        params = dict()
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.organization:
            if hasattr(self.organization, 'to_alipay_dict'):
                params['organization'] = self.organization.to_alipay_dict()
            else:
                params['organization'] = self.organization
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.service_count:
            if hasattr(self.service_count, 'to_alipay_dict'):
                params['service_count'] = self.service_count.to_alipay_dict()
            else:
                params['service_count'] = self.service_count
        if self.staff_name:
            if hasattr(self.staff_name, 'to_alipay_dict'):
                params['staff_name'] = self.staff_name.to_alipay_dict()
            else:
                params['staff_name'] = self.staff_name
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.work_years:
            if hasattr(self.work_years, 'to_alipay_dict'):
                params['work_years'] = self.work_years.to_alipay_dict()
            else:
                params['work_years'] = self.work_years
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentStaffInfo()
        if 'department' in d:
            o.department = d['department']
        if 'organization' in d:
            o.organization = d['organization']
        if 'phone' in d:
            o.phone = d['phone']
        if 'service_count' in d:
            o.service_count = d['service_count']
        if 'staff_name' in d:
            o.staff_name = d['staff_name']
        if 'title' in d:
            o.title = d['title']
        if 'work_years' in d:
            o.work_years = d['work_years']
        return o


