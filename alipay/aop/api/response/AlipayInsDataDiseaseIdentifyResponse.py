#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsDataDiseaseIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataDiseaseIdentifyResponse, self).__init__()
        self._disease_code = None
        self._disease_name = None
        self._disease_tag = None

    @property
    def disease_code(self):
        return self._disease_code

    @disease_code.setter
    def disease_code(self, value):
        self._disease_code = value
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value
    @property
    def disease_tag(self):
        return self._disease_tag

    @disease_tag.setter
    def disease_tag(self, value):
        self._disease_tag = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataDiseaseIdentifyResponse, self).parse_response_content(response_content)
        if 'disease_code' in response:
            self.disease_code = response['disease_code']
        if 'disease_name' in response:
            self.disease_name = response['disease_name']
        if 'disease_tag' in response:
            self.disease_tag = response['disease_tag']
