#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestBurypointreportSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestBurypointreportSyncResponse, self).__init__()
        self._acknowledged = None

    @property
    def acknowledged(self):
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, value):
        self._acknowledged = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestBurypointreportSyncResponse, self).parse_response_content(response_content)
        if 'acknowledged' in response:
            self.acknowledged = response['acknowledged']
