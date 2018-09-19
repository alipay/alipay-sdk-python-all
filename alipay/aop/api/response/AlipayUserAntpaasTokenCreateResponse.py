#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAntpaasTokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntpaasTokenCreateResponse, self).__init__()
        self._ant_id = None

    @property
    def ant_id(self):
        return self._ant_id

    @ant_id.setter
    def ant_id(self, value):
        self._ant_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntpaasTokenCreateResponse, self).parse_response_content(response_content)
        if 'ant_id' in response:
            self.ant_id = response['ant_id']
