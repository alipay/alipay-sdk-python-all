#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntLinkeAlcollectioncenterPreviewurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntLinkeAlcollectioncenterPreviewurlQueryResponse, self).__init__()
        self._urls = None

    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, value):
        if isinstance(value, list):
            self._urls = list()
            for i in value:
                self._urls.append(i)

    def parse_response_content(self, response_content):
        response = super(AntLinkeAlcollectioncenterPreviewurlQueryResponse, self).parse_response_content(response_content)
        if 'urls' in response:
            self.urls = response['urls']
