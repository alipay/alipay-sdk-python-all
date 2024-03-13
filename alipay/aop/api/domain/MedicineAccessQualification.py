#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicineAccessQualification(object):

    def __init__(self):
        self._access_qualification_approval_name = None
        self._access_qualification_approval_type = None
        self._access_qualification_cert_no = None
        self._access_qualification_department = None
        self._access_qualification_effective_date = None
        self._access_qualification_expiration_date = None
        self._access_qualification_image = None
        self._access_qualification_person = None

    @property
    def access_qualification_approval_name(self):
        return self._access_qualification_approval_name

    @access_qualification_approval_name.setter
    def access_qualification_approval_name(self, value):
        self._access_qualification_approval_name = value
    @property
    def access_qualification_approval_type(self):
        return self._access_qualification_approval_type

    @access_qualification_approval_type.setter
    def access_qualification_approval_type(self, value):
        self._access_qualification_approval_type = value
    @property
    def access_qualification_cert_no(self):
        return self._access_qualification_cert_no

    @access_qualification_cert_no.setter
    def access_qualification_cert_no(self, value):
        self._access_qualification_cert_no = value
    @property
    def access_qualification_department(self):
        return self._access_qualification_department

    @access_qualification_department.setter
    def access_qualification_department(self, value):
        self._access_qualification_department = value
    @property
    def access_qualification_effective_date(self):
        return self._access_qualification_effective_date

    @access_qualification_effective_date.setter
    def access_qualification_effective_date(self, value):
        self._access_qualification_effective_date = value
    @property
    def access_qualification_expiration_date(self):
        return self._access_qualification_expiration_date

    @access_qualification_expiration_date.setter
    def access_qualification_expiration_date(self, value):
        self._access_qualification_expiration_date = value
    @property
    def access_qualification_image(self):
        return self._access_qualification_image

    @access_qualification_image.setter
    def access_qualification_image(self, value):
        self._access_qualification_image = value
    @property
    def access_qualification_person(self):
        return self._access_qualification_person

    @access_qualification_person.setter
    def access_qualification_person(self, value):
        self._access_qualification_person = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_qualification_approval_name:
            if hasattr(self.access_qualification_approval_name, 'to_alipay_dict'):
                params['access_qualification_approval_name'] = self.access_qualification_approval_name.to_alipay_dict()
            else:
                params['access_qualification_approval_name'] = self.access_qualification_approval_name
        if self.access_qualification_approval_type:
            if hasattr(self.access_qualification_approval_type, 'to_alipay_dict'):
                params['access_qualification_approval_type'] = self.access_qualification_approval_type.to_alipay_dict()
            else:
                params['access_qualification_approval_type'] = self.access_qualification_approval_type
        if self.access_qualification_cert_no:
            if hasattr(self.access_qualification_cert_no, 'to_alipay_dict'):
                params['access_qualification_cert_no'] = self.access_qualification_cert_no.to_alipay_dict()
            else:
                params['access_qualification_cert_no'] = self.access_qualification_cert_no
        if self.access_qualification_department:
            if hasattr(self.access_qualification_department, 'to_alipay_dict'):
                params['access_qualification_department'] = self.access_qualification_department.to_alipay_dict()
            else:
                params['access_qualification_department'] = self.access_qualification_department
        if self.access_qualification_effective_date:
            if hasattr(self.access_qualification_effective_date, 'to_alipay_dict'):
                params['access_qualification_effective_date'] = self.access_qualification_effective_date.to_alipay_dict()
            else:
                params['access_qualification_effective_date'] = self.access_qualification_effective_date
        if self.access_qualification_expiration_date:
            if hasattr(self.access_qualification_expiration_date, 'to_alipay_dict'):
                params['access_qualification_expiration_date'] = self.access_qualification_expiration_date.to_alipay_dict()
            else:
                params['access_qualification_expiration_date'] = self.access_qualification_expiration_date
        if self.access_qualification_image:
            if hasattr(self.access_qualification_image, 'to_alipay_dict'):
                params['access_qualification_image'] = self.access_qualification_image.to_alipay_dict()
            else:
                params['access_qualification_image'] = self.access_qualification_image
        if self.access_qualification_person:
            if hasattr(self.access_qualification_person, 'to_alipay_dict'):
                params['access_qualification_person'] = self.access_qualification_person.to_alipay_dict()
            else:
                params['access_qualification_person'] = self.access_qualification_person
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicineAccessQualification()
        if 'access_qualification_approval_name' in d:
            o.access_qualification_approval_name = d['access_qualification_approval_name']
        if 'access_qualification_approval_type' in d:
            o.access_qualification_approval_type = d['access_qualification_approval_type']
        if 'access_qualification_cert_no' in d:
            o.access_qualification_cert_no = d['access_qualification_cert_no']
        if 'access_qualification_department' in d:
            o.access_qualification_department = d['access_qualification_department']
        if 'access_qualification_effective_date' in d:
            o.access_qualification_effective_date = d['access_qualification_effective_date']
        if 'access_qualification_expiration_date' in d:
            o.access_qualification_expiration_date = d['access_qualification_expiration_date']
        if 'access_qualification_image' in d:
            o.access_qualification_image = d['access_qualification_image']
        if 'access_qualification_person' in d:
            o.access_qualification_person = d['access_qualification_person']
        return o


