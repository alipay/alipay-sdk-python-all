#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DoctorBasicInfo import DoctorBasicInfo


class AlipayCommerceMedicalDoctorinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctorinfoBatchqueryResponse, self).__init__()
        self._doctor_info_list = None

    @property
    def doctor_info_list(self):
        return self._doctor_info_list

    @doctor_info_list.setter
    def doctor_info_list(self, value):
        if isinstance(value, list):
            self._doctor_info_list = list()
            for i in value:
                if isinstance(i, DoctorBasicInfo):
                    self._doctor_info_list.append(i)
                else:
                    self._doctor_info_list.append(DoctorBasicInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctorinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'doctor_info_list' in response:
            self.doctor_info_list = response['doctor_info_list']
