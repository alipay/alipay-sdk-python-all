#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMaptorchrelayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMaptorchrelayQueryResponse, self).__init__()
        self._site_uv = None

    @property
    def site_uv(self):
        return self._site_uv

    @site_uv.setter
    def site_uv(self, value):
        self._site_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMaptorchrelayQueryResponse, self).parse_response_content(response_content)
        if 'site_uv' in response:
            self.site_uv = response['site_uv']
