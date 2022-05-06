#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DoctorData import DoctorData


class AlipayCommerceMedicalIndustrydataDoctorUploadModel(object):

    def __init__(self):
        self._doctor_list = None
        self._isv_pid = None
        self._request_id = None

    @property
    def doctor_list(self):
        return self._doctor_list

    @doctor_list.setter
    def doctor_list(self, value):
        if isinstance(value, list):
            self._doctor_list = list()
            for i in value:
                if isinstance(i, DoctorData):
                    self._doctor_list.append(i)
                else:
                    self._doctor_list.append(DoctorData.from_alipay_dict(i))
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_list:
            if isinstance(self.doctor_list, list):
                for i in range(0, len(self.doctor_list)):
                    element = self.doctor_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doctor_list[i] = element.to_alipay_dict()
            if hasattr(self.doctor_list, 'to_alipay_dict'):
                params['doctor_list'] = self.doctor_list.to_alipay_dict()
            else:
                params['doctor_list'] = self.doctor_list
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataDoctorUploadModel()
        if 'doctor_list' in d:
            o.doctor_list = d['doctor_list']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


