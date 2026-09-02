#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAccountAcccoreCetifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountAcccoreCetifyQueryResponse, self).__init__()
        self._certified = None

    @property
    def certified(self):
        return self._certified

    @certified.setter
    def certified(self, value):
        self._certified = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountAcccoreCetifyQueryResponse, self).parse_response_content(response_content)
        if 'certified' in response:
            self.certified = response['certified']
