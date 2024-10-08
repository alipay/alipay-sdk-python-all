#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DumpPageRes import DumpPageRes


class AlipayCloudCloudrunObDumpresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObDumpresultQueryResponse, self).__init__()
        self._dump_page_res = None

    @property
    def dump_page_res(self):
        return self._dump_page_res

    @dump_page_res.setter
    def dump_page_res(self, value):
        if isinstance(value, DumpPageRes):
            self._dump_page_res = value
        else:
            self._dump_page_res = DumpPageRes.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObDumpresultQueryResponse, self).parse_response_content(response_content)
        if 'dump_page_res' in response:
            self.dump_page_res = response['dump_page_res']
