#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppAppcontentPoiSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppAppcontentPoiSyncResponse, self).__init__()
        self._alipay_poi_id = None

    @property
    def alipay_poi_id(self):
        return self._alipay_poi_id

    @alipay_poi_id.setter
    def alipay_poi_id(self, value):
        self._alipay_poi_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppAppcontentPoiSyncResponse, self).parse_response_content(response_content)
        if 'alipay_poi_id' in response:
            self.alipay_poi_id = response['alipay_poi_id']
