#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CustomReportCondition import CustomReportCondition


class KoubeiMarketingDataCustomreportDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataCustomreportDetailQueryResponse, self).__init__()
        self._report_condition_info = None

    @property
    def report_condition_info(self):
        return self._report_condition_info

    @report_condition_info.setter
    def report_condition_info(self, value):
        if isinstance(value, CustomReportCondition):
            self._report_condition_info = value
        else:
            self._report_condition_info = CustomReportCondition.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataCustomreportDetailQueryResponse, self).parse_response_content(response_content)
        if 'report_condition_info' in response:
            self.report_condition_info = response['report_condition_info']
