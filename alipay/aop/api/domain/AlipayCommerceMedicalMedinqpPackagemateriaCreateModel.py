#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedinqpPackagemateriaCreateModel(object):

    def __init__(self):
        self._department = None
        self._doctor_id = None
        self._doctor_image = None
        self._doctor_name = None
        self._doctor_title = None
        self._education_title = None
        self._hospital_name = None
        self._qr_type = None
        self._service_package_id = None
        self._service_package_type = None

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_image(self):
        return self._doctor_image

    @doctor_image.setter
    def doctor_image(self, value):
        self._doctor_image = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_title(self):
        return self._doctor_title

    @doctor_title.setter
    def doctor_title(self, value):
        self._doctor_title = value
    @property
    def education_title(self):
        return self._education_title

    @education_title.setter
    def education_title(self, value):
        self._education_title = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def qr_type(self):
        return self._qr_type

    @qr_type.setter
    def qr_type(self, value):
        self._qr_type = value
    @property
    def service_package_id(self):
        return self._service_package_id

    @service_package_id.setter
    def service_package_id(self, value):
        self._service_package_id = value
    @property
    def service_package_type(self):
        return self._service_package_type

    @service_package_type.setter
    def service_package_type(self, value):
        self._service_package_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_image:
            if hasattr(self.doctor_image, 'to_alipay_dict'):
                params['doctor_image'] = self.doctor_image.to_alipay_dict()
            else:
                params['doctor_image'] = self.doctor_image
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_title:
            if hasattr(self.doctor_title, 'to_alipay_dict'):
                params['doctor_title'] = self.doctor_title.to_alipay_dict()
            else:
                params['doctor_title'] = self.doctor_title
        if self.education_title:
            if hasattr(self.education_title, 'to_alipay_dict'):
                params['education_title'] = self.education_title.to_alipay_dict()
            else:
                params['education_title'] = self.education_title
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.qr_type:
            if hasattr(self.qr_type, 'to_alipay_dict'):
                params['qr_type'] = self.qr_type.to_alipay_dict()
            else:
                params['qr_type'] = self.qr_type
        if self.service_package_id:
            if hasattr(self.service_package_id, 'to_alipay_dict'):
                params['service_package_id'] = self.service_package_id.to_alipay_dict()
            else:
                params['service_package_id'] = self.service_package_id
        if self.service_package_type:
            if hasattr(self.service_package_type, 'to_alipay_dict'):
                params['service_package_type'] = self.service_package_type.to_alipay_dict()
            else:
                params['service_package_type'] = self.service_package_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedinqpPackagemateriaCreateModel()
        if 'department' in d:
            o.department = d['department']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_image' in d:
            o.doctor_image = d['doctor_image']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_title' in d:
            o.doctor_title = d['doctor_title']
        if 'education_title' in d:
            o.education_title = d['education_title']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'qr_type' in d:
            o.qr_type = d['qr_type']
        if 'service_package_id' in d:
            o.service_package_id = d['service_package_id']
        if 'service_package_type' in d:
            o.service_package_type = d['service_package_type']
        return o


