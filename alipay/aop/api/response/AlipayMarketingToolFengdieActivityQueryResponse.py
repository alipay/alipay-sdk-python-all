#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FengdieActivity import FengdieActivity


class AlipayMarketingToolFengdieActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolFengdieActivityQueryResponse, self).__init__()
        self._activity = None

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        if isinstance(value, FengdieActivity):
            self._activity = value
        else:
            self._activity = FengdieActivity.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolFengdieActivityQueryResponse, self).parse_response_content(response_content)
        if 'activity' in response:
            self.activity = response['activity']
