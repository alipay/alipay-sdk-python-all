#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MonthlyUsage import MonthlyUsage


class AlipayCloudCloudbaseResourceusageMonthlyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourceusageMonthlyQueryResponse, self).__init__()
        self._monthly_usages = None

    @property
    def monthly_usages(self):
        return self._monthly_usages

    @monthly_usages.setter
    def monthly_usages(self, value):
        if isinstance(value, list):
            self._monthly_usages = list()
            for i in value:
                if isinstance(i, MonthlyUsage):
                    self._monthly_usages.append(i)
                else:
                    self._monthly_usages.append(MonthlyUsage.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourceusageMonthlyQueryResponse, self).parse_response_content(response_content)
        if 'monthly_usages' in response:
            self.monthly_usages = response['monthly_usages']
