#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniPoiCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPoiCreateResponse, self).__init__()
        self._poi_id = None

    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPoiCreateResponse, self).parse_response_content(response_content)
        if 'poi_id' in response:
            self.poi_id = response['poi_id']
