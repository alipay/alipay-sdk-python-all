#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCircularAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCircularAgreementSignResponse, self).__init__()
        self._status = None
        self._url = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCircularAgreementSignResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
        if 'url' in response:
            self.url = response['url']
