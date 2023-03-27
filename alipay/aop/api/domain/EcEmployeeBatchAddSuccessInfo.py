#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcEmployeeBatchAddSuccessInfo(object):

    def __init__(self):
        self._employee_email = None
        self._employee_id = None
        self._employee_mobile = None
        self._employee_name = None
        self._employee_no = None

    @property
    def employee_email(self):
        return self._employee_email

    @employee_email.setter
    def employee_email(self, value):
        self._employee_email = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def employee_mobile(self):
        return self._employee_mobile

    @employee_mobile.setter
    def employee_mobile(self, value):
        self._employee_mobile = value
    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, value):
        self._employee_name = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_email:
            if hasattr(self.employee_email, 'to_alipay_dict'):
                params['employee_email'] = self.employee_email.to_alipay_dict()
            else:
                params['employee_email'] = self.employee_email
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.employee_mobile:
            if hasattr(self.employee_mobile, 'to_alipay_dict'):
                params['employee_mobile'] = self.employee_mobile.to_alipay_dict()
            else:
                params['employee_mobile'] = self.employee_mobile
        if self.employee_name:
            if hasattr(self.employee_name, 'to_alipay_dict'):
                params['employee_name'] = self.employee_name.to_alipay_dict()
            else:
                params['employee_name'] = self.employee_name
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcEmployeeBatchAddSuccessInfo()
        if 'employee_email' in d:
            o.employee_email = d['employee_email']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'employee_mobile' in d:
            o.employee_mobile = d['employee_mobile']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        return o


