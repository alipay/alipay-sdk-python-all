#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JFExportInputFieldModel import JFExportInputFieldModel


class AlipayEbppJfexportInputfieldQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfexportInputfieldQueryResponse, self).__init__()
        self._input_fields = None

    @property
    def input_fields(self):
        return self._input_fields

    @input_fields.setter
    def input_fields(self, value):
        if isinstance(value, list):
            self._input_fields = list()
            for i in value:
                if isinstance(i, JFExportInputFieldModel):
                    self._input_fields.append(i)
                else:
                    self._input_fields.append(JFExportInputFieldModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfexportInputfieldQueryResponse, self).parse_response_content(response_content)
        if 'input_fields' in response:
            self.input_fields = response['input_fields']
