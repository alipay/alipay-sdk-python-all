#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvTfjsModelBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvTfjsModelBatchqueryResponse, self).__init__()
        self._model_info = None

    @property
    def model_info(self):
        return self._model_info

    @model_info.setter
    def model_info(self, value):
        self._model_info = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvTfjsModelBatchqueryResponse, self).parse_response_content(response_content)
        if 'model_info' in response:
            self.model_info = response['model_info']
