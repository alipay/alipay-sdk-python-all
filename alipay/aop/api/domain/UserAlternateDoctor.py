#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserAlternateDoctor(object):

    def __init__(self):
        self._doctor_inner_id = None
        self._hdf_doctor_id = None

    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def hdf_doctor_id(self):
        return self._hdf_doctor_id

    @hdf_doctor_id.setter
    def hdf_doctor_id(self, value):
        self._hdf_doctor_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_inner_id:
            if hasattr(self.doctor_inner_id, 'to_alipay_dict'):
                params['doctor_inner_id'] = self.doctor_inner_id.to_alipay_dict()
            else:
                params['doctor_inner_id'] = self.doctor_inner_id
        if self.hdf_doctor_id:
            if hasattr(self.hdf_doctor_id, 'to_alipay_dict'):
                params['hdf_doctor_id'] = self.hdf_doctor_id.to_alipay_dict()
            else:
                params['hdf_doctor_id'] = self.hdf_doctor_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAlternateDoctor()
        if 'doctor_inner_id' in d:
            o.doctor_inner_id = d['doctor_inner_id']
        if 'hdf_doctor_id' in d:
            o.hdf_doctor_id = d['hdf_doctor_id']
        return o


