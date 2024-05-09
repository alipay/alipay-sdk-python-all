#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialUnitCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialUnitCreateResponse, self).__init__()
        self._unit_code = None

    @property
    def unit_code(self):
        return self._unit_code

    @unit_code.setter
    def unit_code(self, value):
        self._unit_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialUnitCreateResponse, self).parse_response_content(response_content)
        if 'unit_code' in response:
            self.unit_code = response['unit_code']
