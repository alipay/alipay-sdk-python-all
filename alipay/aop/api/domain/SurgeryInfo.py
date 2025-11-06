#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SurgeryInfo(object):

    def __init__(self):
        self._surgery_anesthesia = None
        self._surgery_date = None
        self._surgery_desc = None
        self._surgery_doctor = None
        self._surgery_name = None

    @property
    def surgery_anesthesia(self):
        return self._surgery_anesthesia

    @surgery_anesthesia.setter
    def surgery_anesthesia(self, value):
        self._surgery_anesthesia = value
    @property
    def surgery_date(self):
        return self._surgery_date

    @surgery_date.setter
    def surgery_date(self, value):
        self._surgery_date = value
    @property
    def surgery_desc(self):
        return self._surgery_desc

    @surgery_desc.setter
    def surgery_desc(self, value):
        self._surgery_desc = value
    @property
    def surgery_doctor(self):
        return self._surgery_doctor

    @surgery_doctor.setter
    def surgery_doctor(self, value):
        self._surgery_doctor = value
    @property
    def surgery_name(self):
        return self._surgery_name

    @surgery_name.setter
    def surgery_name(self, value):
        self._surgery_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.surgery_anesthesia:
            if hasattr(self.surgery_anesthesia, 'to_alipay_dict'):
                params['surgery_anesthesia'] = self.surgery_anesthesia.to_alipay_dict()
            else:
                params['surgery_anesthesia'] = self.surgery_anesthesia
        if self.surgery_date:
            if hasattr(self.surgery_date, 'to_alipay_dict'):
                params['surgery_date'] = self.surgery_date.to_alipay_dict()
            else:
                params['surgery_date'] = self.surgery_date
        if self.surgery_desc:
            if hasattr(self.surgery_desc, 'to_alipay_dict'):
                params['surgery_desc'] = self.surgery_desc.to_alipay_dict()
            else:
                params['surgery_desc'] = self.surgery_desc
        if self.surgery_doctor:
            if hasattr(self.surgery_doctor, 'to_alipay_dict'):
                params['surgery_doctor'] = self.surgery_doctor.to_alipay_dict()
            else:
                params['surgery_doctor'] = self.surgery_doctor
        if self.surgery_name:
            if hasattr(self.surgery_name, 'to_alipay_dict'):
                params['surgery_name'] = self.surgery_name.to_alipay_dict()
            else:
                params['surgery_name'] = self.surgery_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SurgeryInfo()
        if 'surgery_anesthesia' in d:
            o.surgery_anesthesia = d['surgery_anesthesia']
        if 'surgery_date' in d:
            o.surgery_date = d['surgery_date']
        if 'surgery_desc' in d:
            o.surgery_desc = d['surgery_desc']
        if 'surgery_doctor' in d:
            o.surgery_doctor = d['surgery_doctor']
        if 'surgery_name' in d:
            o.surgery_name = d['surgery_name']
        return o


