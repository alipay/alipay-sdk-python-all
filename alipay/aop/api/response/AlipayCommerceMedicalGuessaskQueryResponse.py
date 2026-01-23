#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalGuessaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalGuessaskQueryResponse, self).__init__()
        self._diseases = None

    @property
    def diseases(self):
        return self._diseases

    @diseases.setter
    def diseases(self, value):
        if isinstance(value, list):
            self._diseases = list()
            for i in value:
                self._diseases.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalGuessaskQueryResponse, self).parse_response_content(response_content)
        if 'diseases' in response:
            self.diseases = response['diseases']
