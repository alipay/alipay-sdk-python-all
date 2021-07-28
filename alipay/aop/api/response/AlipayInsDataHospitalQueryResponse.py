#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HospitalDTO import HospitalDTO


class AlipayInsDataHospitalQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataHospitalQueryResponse, self).__init__()
        self._hospitals = None

    @property
    def hospitals(self):
        return self._hospitals

    @hospitals.setter
    def hospitals(self, value):
        if isinstance(value, list):
            self._hospitals = list()
            for i in value:
                if isinstance(i, HospitalDTO):
                    self._hospitals.append(i)
                else:
                    self._hospitals.append(HospitalDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataHospitalQueryResponse, self).parse_response_content(response_content)
        if 'hospitals' in response:
            self.hospitals = response['hospitals']
