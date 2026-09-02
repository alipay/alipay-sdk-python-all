#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InqueryDoctorStatusData import InqueryDoctorStatusData


class AlipayCommerceMedicalIndustrydataInquirydoctorstatusUploadModel(object):

    def __init__(self):
        self._doctor_status_list = None
        self._isv_code = None
        self._platform_code = None

    @property
    def doctor_status_list(self):
        return self._doctor_status_list

    @doctor_status_list.setter
    def doctor_status_list(self, value):
        if isinstance(value, list):
            self._doctor_status_list = list()
            for i in value:
                if isinstance(i, InqueryDoctorStatusData):
                    self._doctor_status_list.append(i)
                else:
                    self._doctor_status_list.append(InqueryDoctorStatusData.from_alipay_dict(i))
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_status_list:
            if isinstance(self.doctor_status_list, list):
                for i in range(0, len(self.doctor_status_list)):
                    element = self.doctor_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.doctor_status_list[i] = element.to_alipay_dict()
            if hasattr(self.doctor_status_list, 'to_alipay_dict'):
                params['doctor_status_list'] = self.doctor_status_list.to_alipay_dict()
            else:
                params['doctor_status_list'] = self.doctor_status_list
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataInquirydoctorstatusUploadModel()
        if 'doctor_status_list' in d:
            o.doctor_status_list = d['doctor_status_list']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        return o


