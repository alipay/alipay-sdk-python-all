#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceOnlinetestsecondRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceOnlinetestsecondRainystestQueryResponse, self).__init__()
        self._tc_case = None

    @property
    def tc_case(self):
        return self._tc_case

    @tc_case.setter
    def tc_case(self, value):
        self._tc_case = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceOnlinetestsecondRainystestQueryResponse, self).parse_response_content(response_content)
        if 'tc_case' in response:
            self.tc_case = response['tc_case']
