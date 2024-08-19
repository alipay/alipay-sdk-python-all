#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserInfoAuthResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInfoAuthResponse, self).__init__()
        self._pageRedirectionData = None

    @property
    def pageRedirectionData(self):
        return self._pageRedirectionData

    @pageRedirectionData.setter
    def pageRedirectionData(self, value):
        self._pageRedirectionData = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserInfoAuthResponse, self).parse_response_content(response_content)
        if 'pageRedirectionData' in response:
            self.pageRedirectionData = response['pageRedirectionData']
