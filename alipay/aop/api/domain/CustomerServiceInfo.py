#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerServiceInfo(object):

    def __init__(self):
        self._employee_no = None
        self._gender = None
        self._mobile = None
        self._name = None

    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerServiceInfo()
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'gender' in d:
            o.gender = d['gender']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        return o


