#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAftsCertIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAftsCertIdentifyResponse, self).__init__()
        self._cert_probability = None
        self._cert_type = None
        self._ocr_engine_number = None
        self._ocr_name = None
        self._ocr_plate_number = None
        self._ocr_vehicle_id = None

    @property
    def cert_probability(self):
        return self._cert_probability

    @cert_probability.setter
    def cert_probability(self, value):
        self._cert_probability = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def ocr_engine_number(self):
        return self._ocr_engine_number

    @ocr_engine_number.setter
    def ocr_engine_number(self, value):
        self._ocr_engine_number = value
    @property
    def ocr_name(self):
        return self._ocr_name

    @ocr_name.setter
    def ocr_name(self, value):
        self._ocr_name = value
    @property
    def ocr_plate_number(self):
        return self._ocr_plate_number

    @ocr_plate_number.setter
    def ocr_plate_number(self, value):
        self._ocr_plate_number = value
    @property
    def ocr_vehicle_id(self):
        return self._ocr_vehicle_id

    @ocr_vehicle_id.setter
    def ocr_vehicle_id(self, value):
        self._ocr_vehicle_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAftsCertIdentifyResponse, self).parse_response_content(response_content)
        if 'cert_probability' in response:
            self.cert_probability = response['cert_probability']
        if 'cert_type' in response:
            self.cert_type = response['cert_type']
        if 'ocr_engine_number' in response:
            self.ocr_engine_number = response['ocr_engine_number']
        if 'ocr_name' in response:
            self.ocr_name = response['ocr_name']
        if 'ocr_plate_number' in response:
            self.ocr_plate_number = response['ocr_plate_number']
        if 'ocr_vehicle_id' in response:
            self.ocr_vehicle_id = response['ocr_vehicle_id']
