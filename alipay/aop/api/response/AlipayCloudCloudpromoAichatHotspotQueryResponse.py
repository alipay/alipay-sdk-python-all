#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChatHotspot import ChatHotspot


class AlipayCloudCloudpromoAichatHotspotQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAichatHotspotQueryResponse, self).__init__()
        self._hotspots = None

    @property
    def hotspots(self):
        return self._hotspots

    @hotspots.setter
    def hotspots(self, value):
        if isinstance(value, ChatHotspot):
            self._hotspots = value
        else:
            self._hotspots = ChatHotspot.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAichatHotspotQueryResponse, self).parse_response_content(response_content)
        if 'hotspots' in response:
            self.hotspots = response['hotspots']
