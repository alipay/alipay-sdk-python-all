#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvTfjsModelversionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvTfjsModelversionBatchqueryResponse, self).__init__()
        self._model_version = None

    @property
    def model_version(self):
        return self._model_version

    @model_version.setter
    def model_version(self, value):
        self._model_version = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvTfjsModelversionBatchqueryResponse, self).parse_response_content(response_content)
        if 'model_version' in response:
            self.model_version = response['model_version']
