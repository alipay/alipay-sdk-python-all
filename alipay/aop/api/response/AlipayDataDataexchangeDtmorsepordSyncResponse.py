#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataexchangeDtmorsepordSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeDtmorsepordSyncResponse, self).__init__()
        self._biz_id = None
        self._result_extent = None
        self._success = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def result_extent(self):
        return self._result_extent

    @result_extent.setter
    def result_extent(self, value):
        self._result_extent = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeDtmorsepordSyncResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'result_extent' in response:
            self.result_extent = response['result_extent']
        if 'success' in response:
            self.success = response['success']
