#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedagentDoctoragentstatusQueryModel(object):

    def __init__(self):
        self._hdf_doctor_id = None

    @property
    def hdf_doctor_id(self):
        return self._hdf_doctor_id

    @hdf_doctor_id.setter
    def hdf_doctor_id(self, value):
        self._hdf_doctor_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayCommerceMedicalMedagentDoctoragentstatusQueryModel()
        if 'hdf_doctor_id' in d:
            o.hdf_doctor_id = d['hdf_doctor_id']
        return o


