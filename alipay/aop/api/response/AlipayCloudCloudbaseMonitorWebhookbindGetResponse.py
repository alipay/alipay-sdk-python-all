#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseMonitorWebhookbindGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseMonitorWebhookbindGetResponse, self).__init__()
        self._name = None
        self._open = None
        self._request_body = None
        self._request_headers = None
        self._request_type = None
        self._request_url = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def request_body(self):
        return self._request_body

    @request_body.setter
    def request_body(self, value):
        self._request_body = value
    @property
    def request_headers(self):
        return self._request_headers

    @request_headers.setter
    def request_headers(self, value):
        self._request_headers = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def request_url(self):
        return self._request_url

    @request_url.setter
    def request_url(self, value):
        self._request_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseMonitorWebhookbindGetResponse, self).parse_response_content(response_content)
        if 'name' in response:
            self.name = response['name']
        if 'open' in response:
            self.open = response['open']
        if 'request_body' in response:
            self.request_body = response['request_body']
        if 'request_headers' in response:
            self.request_headers = response['request_headers']
        if 'request_type' in response:
            self.request_type = response['request_type']
        if 'request_url' in response:
            self.request_url = response['request_url']
