#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneStockReleasePublishCheckResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockReleasePublishCheckResponse, self).__init__()
        self._publish_able = None

    @property
    def publish_able(self):
        return self._publish_able

    @publish_able.setter
    def publish_able(self, value):
        self._publish_able = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockReleasePublishCheckResponse, self).parse_response_content(response_content)
        if 'publish_able' in response:
            self.publish_able = response['publish_able']
