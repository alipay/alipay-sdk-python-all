#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskSummaryStatistic import YunTaskSummaryStatistic


class AlipayCommerceYuntaskSummarystatisticsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskSummarystatisticsQueryResponse, self).__init__()
        self._summary_statistic = None

    @property
    def summary_statistic(self):
        return self._summary_statistic

    @summary_statistic.setter
    def summary_statistic(self, value):
        if isinstance(value, YunTaskSummaryStatistic):
            self._summary_statistic = value
        else:
            self._summary_statistic = YunTaskSummaryStatistic.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskSummarystatisticsQueryResponse, self).parse_response_content(response_content)
        if 'summary_statistic' in response:
            self.summary_statistic = response['summary_statistic']
