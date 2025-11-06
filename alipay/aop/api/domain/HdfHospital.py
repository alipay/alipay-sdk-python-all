#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HdfHospital(object):

    def __init__(self):
        self._consultation_credentials = None
        self._credentials_number = None
        self._faculty_name = None
        self._hospital_name = None

    @property
    def consultation_credentials(self):
        return self._consultation_credentials

    @consultation_credentials.setter
    def consultation_credentials(self, value):
        self._consultation_credentials = value
    @property
    def credentials_number(self):
        return self._credentials_number

    @credentials_number.setter
    def credentials_number(self, value):
        self._credentials_number = value
    @property
    def faculty_name(self):
        return self._faculty_name

    @faculty_name.setter
    def faculty_name(self, value):
        self._faculty_name = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.consultation_credentials:
            if hasattr(self.consultation_credentials, 'to_alipay_dict'):
                params['consultation_credentials'] = self.consultation_credentials.to_alipay_dict()
            else:
                params['consultation_credentials'] = self.consultation_credentials
        if self.credentials_number:
            if hasattr(self.credentials_number, 'to_alipay_dict'):
                params['credentials_number'] = self.credentials_number.to_alipay_dict()
            else:
                params['credentials_number'] = self.credentials_number
        if self.faculty_name:
            if hasattr(self.faculty_name, 'to_alipay_dict'):
                params['faculty_name'] = self.faculty_name.to_alipay_dict()
            else:
                params['faculty_name'] = self.faculty_name
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HdfHospital()
        if 'consultation_credentials' in d:
            o.consultation_credentials = d['consultation_credentials']
        if 'credentials_number' in d:
            o.credentials_number = d['credentials_number']
        if 'faculty_name' in d:
            o.faculty_name = d['faculty_name']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        return o


