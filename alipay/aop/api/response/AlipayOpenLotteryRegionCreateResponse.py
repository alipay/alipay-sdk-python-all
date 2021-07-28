#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenLotteryRegionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenLotteryRegionCreateResponse, self).__init__()
        self._region_id = None

    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, value):
        self._region_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenLotteryRegionCreateResponse, self).parse_response_content(response_content)
        if 'region_id' in response:
            self.region_id = response['region_id']
