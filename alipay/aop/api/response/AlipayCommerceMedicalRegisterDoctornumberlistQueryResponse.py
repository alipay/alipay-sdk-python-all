#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RegisterClinic import RegisterClinic


class AlipayCommerceMedicalRegisterDoctornumberlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterDoctornumberlistQueryResponse, self).__init__()
        self._isv_code = None
        self._platform_code = None
        self._register_clinic_list = None
        self._res_prop = None

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
    @property
    def register_clinic_list(self):
        return self._register_clinic_list

    @register_clinic_list.setter
    def register_clinic_list(self, value):
        if isinstance(value, list):
            self._register_clinic_list = list()
            for i in value:
                if isinstance(i, RegisterClinic):
                    self._register_clinic_list.append(i)
                else:
                    self._register_clinic_list.append(RegisterClinic.from_alipay_dict(i))
    @property
    def res_prop(self):
        return self._res_prop

    @res_prop.setter
    def res_prop(self, value):
        self._res_prop = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterDoctornumberlistQueryResponse, self).parse_response_content(response_content)
        if 'isv_code' in response:
            self.isv_code = response['isv_code']
        if 'platform_code' in response:
            self.platform_code = response['platform_code']
        if 'register_clinic_list' in response:
            self.register_clinic_list = response['register_clinic_list']
        if 'res_prop' in response:
            self.res_prop = response['res_prop']
