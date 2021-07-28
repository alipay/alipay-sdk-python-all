#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PlateNoCertDto import PlateNoCertDto


class AlipayEcoMycarVehicleCertifiedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarVehicleCertifiedQueryResponse, self).__init__()
        self._cert_list = None

    @property
    def cert_list(self):
        return self._cert_list

    @cert_list.setter
    def cert_list(self, value):
        if isinstance(value, list):
            self._cert_list = list()
            for i in value:
                if isinstance(i, PlateNoCertDto):
                    self._cert_list.append(i)
                else:
                    self._cert_list.append(PlateNoCertDto.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarVehicleCertifiedQueryResponse, self).parse_response_content(response_content)
        if 'cert_list' in response:
            self.cert_list = response['cert_list']
