#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DailyUsage import DailyUsage


class AlipayCloudCloudbaseResourceusageDailyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourceusageDailyQueryResponse, self).__init__()
        self._daily_usages = None

    @property
    def daily_usages(self):
        return self._daily_usages

    @daily_usages.setter
    def daily_usages(self, value):
        if isinstance(value, list):
            self._daily_usages = list()
            for i in value:
                if isinstance(i, DailyUsage):
                    self._daily_usages.append(i)
                else:
                    self._daily_usages.append(DailyUsage.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourceusageDailyQueryResponse, self).parse_response_content(response_content)
        if 'daily_usages' in response:
            self.daily_usages = response['daily_usages']
