#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderUserinfoNverifyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderUserinfoNverifyCreateResponse, self).__init__()
        self._vid = None

    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderUserinfoNverifyCreateResponse, self).parse_response_content(response_content)
        if 'vid' in response:
            self.vid = response['vid']
