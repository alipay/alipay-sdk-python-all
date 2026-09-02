#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipaySubscribePortalSessionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipaySubscribePortalSessionCreateResponse, self).__init__()
        self._expire_time = None
        self._portal_url = None

    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def portal_url(self):
        return self._portal_url

    @portal_url.setter
    def portal_url(self, value):
        self._portal_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipaySubscribePortalSessionCreateResponse, self).parse_response_content(response_content)
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'portal_url' in response:
            self.portal_url = response['portal_url']
