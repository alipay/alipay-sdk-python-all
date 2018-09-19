#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiRetailWmsInboundworkCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsInboundworkCreateResponse, self).__init__()
        self._inbound_work_id = None

    @property
    def inbound_work_id(self):
        return self._inbound_work_id

    @inbound_work_id.setter
    def inbound_work_id(self, value):
        self._inbound_work_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsInboundworkCreateResponse, self).parse_response_content(response_content)
        if 'inbound_work_id' in response:
            self.inbound_work_id = response['inbound_work_id']
