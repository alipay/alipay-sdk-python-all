#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsDataDistrictQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataDistrictQueryResponse, self).__init__()
        self._districts = None

    @property
    def districts(self):
        return self._districts

    @districts.setter
    def districts(self, value):
        self._districts = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataDistrictQueryResponse, self).parse_response_content(response_content)
        if 'districts' in response:
            self.districts = response['districts']
