#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntProdpaasProductInspectionCompleteCallbackResponse(AlipayResponse):

    def __init__(self):
        super(AntProdpaasProductInspectionCompleteCallbackResponse, self).__init__()
        self._quality_inspection_no = None

    @property
    def quality_inspection_no(self):
        return self._quality_inspection_no

    @quality_inspection_no.setter
    def quality_inspection_no(self, value):
        self._quality_inspection_no = value

    def parse_response_content(self, response_content):
        response = super(AntProdpaasProductInspectionCompleteCallbackResponse, self).parse_response_content(response_content)
        if 'quality_inspection_no' in response:
            self.quality_inspection_no = response['quality_inspection_no']
