#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMemberbuyItemdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberbuyItemdetailQueryResponse, self).__init__()
        self._detail_url = None
        self._service_id = None

    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberbuyItemdetailQueryResponse, self).parse_response_content(response_content)
        if 'detail_url' in response:
            self.detail_url = response['detail_url']
        if 'service_id' in response:
            self.service_id = response['service_id']
