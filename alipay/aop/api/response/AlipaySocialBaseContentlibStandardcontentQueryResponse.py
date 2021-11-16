#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseContentlibStandardcontentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseContentlibStandardcontentQueryResponse, self).__init__()
        self._source_status = None

    @property
    def source_status(self):
        return self._source_status

    @source_status.setter
    def source_status(self, value):
        self._source_status = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseContentlibStandardcontentQueryResponse, self).parse_response_content(response_content)
        if 'source_status' in response:
            self.source_status = response['source_status']
