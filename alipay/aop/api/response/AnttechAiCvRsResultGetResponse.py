#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvRsResultGetResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvRsResultGetResponse, self).__init__()
        self._predict_res = None

    @property
    def predict_res(self):
        return self._predict_res

    @predict_res.setter
    def predict_res(self, value):
        self._predict_res = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvRsResultGetResponse, self).parse_response_content(response_content)
        if 'predict_res' in response:
            self.predict_res = response['predict_res']
