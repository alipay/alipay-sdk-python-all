#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcSupplierUrlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcSupplierUrlQueryResponse, self).__init__()
        self._url = None
        self._url_type = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def url_type(self):
        return self._url_type

    @url_type.setter
    def url_type(self, value):
        self._url_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcSupplierUrlQueryResponse, self).parse_response_content(response_content)
        if 'url' in response:
            self.url = response['url']
        if 'url_type' in response:
            self.url_type = response['url_type']
