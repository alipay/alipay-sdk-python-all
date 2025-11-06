#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFDoctorInfo(object):

    def __init__(self):
        self._doctor_name = None
        self._head_image = None
        self._sex = None

    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def head_image(self):
        return self._head_image

    @head_image.setter
    def head_image(self, value):
        self._head_image = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.head_image:
            if hasattr(self.head_image, 'to_alipay_dict'):
                params['head_image'] = self.head_image.to_alipay_dict()
            else:
                params['head_image'] = self.head_image
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFDoctorInfo()
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'head_image' in d:
            o.head_image = d['head_image']
        if 'sex' in d:
            o.sex = d['sex']
        return o


