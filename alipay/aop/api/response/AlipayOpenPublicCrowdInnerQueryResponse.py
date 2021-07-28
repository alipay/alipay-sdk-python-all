#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CrowdSummary import CrowdSummary


class AlipayOpenPublicCrowdInnerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicCrowdInnerQueryResponse, self).__init__()
        self._crowd_summary = None

    @property
    def crowd_summary(self):
        return self._crowd_summary

    @crowd_summary.setter
    def crowd_summary(self, value):
        if isinstance(value, CrowdSummary):
            self._crowd_summary = value
        else:
            self._crowd_summary = CrowdSummary.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicCrowdInnerQueryResponse, self).parse_response_content(response_content)
        if 'crowd_summary' in response:
            self.crowd_summary = response['crowd_summary']
