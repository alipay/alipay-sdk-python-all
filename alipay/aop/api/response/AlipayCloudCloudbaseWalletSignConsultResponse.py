#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseWalletSignConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletSignConsultResponse, self).__init__()
        self._original_url = None
        self._short_url = None
        self._status = None

    @property
    def original_url(self):
        return self._original_url

    @original_url.setter
    def original_url(self, value):
        self._original_url = value
    @property
    def short_url(self):
        return self._short_url

    @short_url.setter
    def short_url(self, value):
        self._short_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletSignConsultResponse, self).parse_response_content(response_content)
        if 'original_url' in response:
            self.original_url = response['original_url']
        if 'short_url' in response:
            self.short_url = response['short_url']
        if 'status' in response:
            self.status = response['status']
