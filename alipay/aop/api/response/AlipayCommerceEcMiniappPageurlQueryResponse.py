#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcMiniappPageurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcMiniappPageurlQueryResponse, self).__init__()
        self._page_type = None
        self._page_url = None

    @property
    def page_type(self):
        return self._page_type

    @page_type.setter
    def page_type(self, value):
        self._page_type = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcMiniappPageurlQueryResponse, self).parse_response_content(response_content)
        if 'page_type' in response:
            self.page_type = response['page_type']
        if 'page_url' in response:
            self.page_url = response['page_url']
