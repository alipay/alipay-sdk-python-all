#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderIndflowActionMaintainResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderIndflowActionMaintainResponse, self).__init__()
        self._reported = None

    @property
    def reported(self):
        return self._reported

    @reported.setter
    def reported(self, value):
        self._reported = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderIndflowActionMaintainResponse, self).parse_response_content(response_content)
        if 'reported' in response:
            self.reported = response['reported']
