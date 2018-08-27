#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiRetailWmsOutboundworkCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsOutboundworkCreateResponse, self).__init__()
        self._outbound_work_id = None

    @property
    def outbound_work_id(self):
        return self._outbound_work_id

    @outbound_work_id.setter
    def outbound_work_id(self, value):
        self._outbound_work_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsOutboundworkCreateResponse, self).parse_response_content(response_content)
        if 'outbound_work_id' in response:
            self.outbound_work_id = response['outbound_work_id']
