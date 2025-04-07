#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataPrescriptionstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataPrescriptionstatusQueryResponse, self).__init__()
        self._prescription_status = None

    @property
    def prescription_status(self):
        return self._prescription_status

    @prescription_status.setter
    def prescription_status(self, value):
        self._prescription_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataPrescriptionstatusQueryResponse, self).parse_response_content(response_content)
        if 'prescription_status' in response:
            self.prescription_status = response['prescription_status']
