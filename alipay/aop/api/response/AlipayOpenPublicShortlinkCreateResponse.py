#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicShortlinkCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicShortlinkCreateResponse, self).__init__()
        self._shortlink = None

    @property
    def shortlink(self):
        return self._shortlink

    @shortlink.setter
    def shortlink(self, value):
        self._shortlink = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicShortlinkCreateResponse, self).parse_response_content(response_content)
        if 'shortlink' in response:
            self.shortlink = response['shortlink']
