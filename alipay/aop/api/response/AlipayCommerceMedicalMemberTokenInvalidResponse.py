#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMemberTokenInvalidResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberTokenInvalidResponse, self).__init__()
        self._source = None

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberTokenInvalidResponse, self).parse_response_content(response_content)
        if 'source' in response:
            self.source = response['source']
