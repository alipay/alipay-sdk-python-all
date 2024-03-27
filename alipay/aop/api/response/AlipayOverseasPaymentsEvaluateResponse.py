#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasPaymentsEvaluateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasPaymentsEvaluateResponse, self).__init__()
        self._guide_url = None

    @property
    def guide_url(self):
        return self._guide_url

    @guide_url.setter
    def guide_url(self, value):
        self._guide_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasPaymentsEvaluateResponse, self).parse_response_content(response_content)
        if 'guide_url' in response:
            self.guide_url = response['guide_url']
