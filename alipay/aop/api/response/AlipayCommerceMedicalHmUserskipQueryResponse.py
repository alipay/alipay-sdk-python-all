#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHmUserskipQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmUserskipQueryResponse, self).__init__()
        self._skip_url = None

    @property
    def skip_url(self):
        return self._skip_url

    @skip_url.setter
    def skip_url(self, value):
        self._skip_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmUserskipQueryResponse, self).parse_response_content(response_content)
        if 'skip_url' in response:
            self.skip_url = response['skip_url']
