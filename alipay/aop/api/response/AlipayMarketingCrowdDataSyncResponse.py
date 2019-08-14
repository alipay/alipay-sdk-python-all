#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCrowdDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCrowdDataSyncResponse, self).__init__()
        self._crowd_record_id = None

    @property
    def crowd_record_id(self):
        return self._crowd_record_id

    @crowd_record_id.setter
    def crowd_record_id(self, value):
        self._crowd_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCrowdDataSyncResponse, self).parse_response_content(response_content)
        if 'crowd_record_id' in response:
            self.crowd_record_id = response['crowd_record_id']
