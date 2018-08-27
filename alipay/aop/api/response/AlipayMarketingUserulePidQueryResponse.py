#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingUserulePidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingUserulePidQueryResponse, self).__init__()
        self._pids = None

    @property
    def pids(self):
        return self._pids

    @pids.setter
    def pids(self, value):
        self._pids = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingUserulePidQueryResponse, self).parse_response_content(response_content)
        if 'pids' in response:
            self.pids = response['pids']
