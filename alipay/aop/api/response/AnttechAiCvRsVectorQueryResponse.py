#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvRsVectorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvRsVectorQueryResponse, self).__init__()
        self._vector_result = None

    @property
    def vector_result(self):
        return self._vector_result

    @vector_result.setter
    def vector_result(self, value):
        self._vector_result = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvRsVectorQueryResponse, self).parse_response_content(response_content)
        if 'vector_result' in response:
            self.vector_result = response['vector_result']
