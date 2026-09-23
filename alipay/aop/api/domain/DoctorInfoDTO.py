#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DoctorInfoDTO(object):

    def __init__(self):
        self._doctor_id = None
        self._doctor_name = None
        self._doctor_signature = None
        self._doctor_signature_url = None
        self._role_desc = None

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
    def doctor_signature(self):
        return self._doctor_signature

    @doctor_signature.setter
    def doctor_signature(self, value):
        self._doctor_signature = value
    @property
    def doctor_signature_url(self):
        return self._doctor_signature_url

    @doctor_signature_url.setter
    def doctor_signature_url(self, value):
        self._doctor_signature_url = value
    @property
    def role_desc(self):
        return self._role_desc

    @role_desc.setter
    def role_desc(self, value):
        self._role_desc = value


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
        if self.doctor_signature:
            if hasattr(self.doctor_signature, 'to_alipay_dict'):
                params['doctor_signature'] = self.doctor_signature.to_alipay_dict()
            else:
                params['doctor_signature'] = self.doctor_signature
        if self.doctor_signature_url:
            if hasattr(self.doctor_signature_url, 'to_alipay_dict'):
                params['doctor_signature_url'] = self.doctor_signature_url.to_alipay_dict()
            else:
                params['doctor_signature_url'] = self.doctor_signature_url
        if self.role_desc:
            if hasattr(self.role_desc, 'to_alipay_dict'):
                params['role_desc'] = self.role_desc.to_alipay_dict()
            else:
                params['role_desc'] = self.role_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorInfoDTO()
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_signature' in d:
            o.doctor_signature = d['doctor_signature']
        if 'doctor_signature_url' in d:
            o.doctor_signature_url = d['doctor_signature_url']
        if 'role_desc' in d:
            o.role_desc = d['role_desc']
        return o


