#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateTuitioncodePagedataSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTuitioncodePagedataSendResponse, self).__init__()
        self._pagedata_id = None

    @property
    def pagedata_id(self):
        return self._pagedata_id

    @pagedata_id.setter
    def pagedata_id(self, value):
        self._pagedata_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTuitioncodePagedataSendResponse, self).parse_response_content(response_content)
        if 'pagedata_id' in response:
            self.pagedata_id = response['pagedata_id']
