#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalOperationDeliverQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalOperationDeliverQueryResponse, self).__init__()
        self._content_info = None

    @property
    def content_info(self):
        return self._content_info

    @content_info.setter
    def content_info(self, value):
        self._content_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalOperationDeliverQueryResponse, self).parse_response_content(response_content)
        if 'content_info' in response:
            self.content_info = response['content_info']
