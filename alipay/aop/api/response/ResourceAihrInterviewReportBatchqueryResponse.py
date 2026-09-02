#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenapiInterviewReportItemDTO import OpenapiInterviewReportItemDTO


class ResourceAihrInterviewReportBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(ResourceAihrInterviewReportBatchqueryResponse, self).__init__()
        self._report_list = None

    @property
    def report_list(self):
        return self._report_list

    @report_list.setter
    def report_list(self, value):
        if isinstance(value, list):
            self._report_list = list()
            for i in value:
                if isinstance(i, OpenapiInterviewReportItemDTO):
                    self._report_list.append(i)
                else:
                    self._report_list.append(OpenapiInterviewReportItemDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ResourceAihrInterviewReportBatchqueryResponse, self).parse_response_content(response_content)
        if 'report_list' in response:
            self.report_list = response['report_list']
