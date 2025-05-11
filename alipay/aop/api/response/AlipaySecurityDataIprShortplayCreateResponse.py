#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityDataIprShortplayCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataIprShortplayCreateResponse, self).__init__()
        self._desc = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataIprShortplayCreateResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
