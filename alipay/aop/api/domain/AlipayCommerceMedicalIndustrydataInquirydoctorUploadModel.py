#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InqueryDoctorData import InqueryDoctorData


class AlipayCommerceMedicalIndustrydataInquirydoctorUploadModel(object):

    def __init__(self):
        self._doctor_list = None
        self._out_request_no = None
        self._platform_code = None

    @property
    def doctor_list(self):
        return self._doctor_list

    @doctor_list.setter
    def doctor_list(self, value):
        if isinstance(value, list):
            self._doctor_list = list()
            for i in value:
                if isinstance(i, InqueryDoctorData):
                    self._doctor_list.append(i)
                else:
                    self._doctor_list.append(InqueryDoctorData.from_alipay_dict(i))
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value


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
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
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
        o = AlipayCommerceMedicalIndustrydataInquirydoctorUploadModel()
        if 'doctor_list' in d:
            o.doctor_list = d['doctor_list']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        return o


