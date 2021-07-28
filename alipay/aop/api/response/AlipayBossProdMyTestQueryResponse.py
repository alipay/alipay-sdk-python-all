#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdMyTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdMyTestQueryResponse, self).__init__()
        self._longitude = None

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdMyTestQueryResponse, self).parse_response_content(response_content)
        if 'longitude' in response:
            self.longitude = response['longitude']
