#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalReportCategorytextQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalReportCategorytextQueryResponse, self).__init__()
        self._texts = None

    @property
    def texts(self):
        return self._texts

    @texts.setter
    def texts(self, value):
        if isinstance(value, list):
            self._texts = list()
            for i in value:
                self._texts.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalReportCategorytextQueryResponse, self).parse_response_content(response_content)
        if 'texts' in response:
            self.texts = response['texts']
