#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CustomReportCondition import CustomReportCondition


class KoubeiMarketingDataCustomreportBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataCustomreportBatchqueryResponse, self).__init__()
        self._report_condition_list = None

    @property
    def report_condition_list(self):
        return self._report_condition_list

    @report_condition_list.setter
    def report_condition_list(self, value):
        if isinstance(value, list):
            self._report_condition_list = list()
            for i in value:
                if isinstance(i, CustomReportCondition):
                    self._report_condition_list.append(i)
                else:
                    self._report_condition_list.append(CustomReportCondition.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataCustomreportBatchqueryResponse, self).parse_response_content(response_content)
        if 'report_condition_list' in response:
            self.report_condition_list = response['report_condition_list']
