#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReportInterpretationDetailResponse import ReportInterpretationDetailResponse
from alipay.aop.api.domain.ReportDetailResponse import ReportDetailResponse


class AlipayCommerceMedicalHealthfulfillmentReportinterpretationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthfulfillmentReportinterpretationQueryResponse, self).__init__()
        self._interpretation_result = None
        self._report_list = None

    @property
    def interpretation_result(self):
        return self._interpretation_result

    @interpretation_result.setter
    def interpretation_result(self, value):
        if isinstance(value, ReportInterpretationDetailResponse):
            self._interpretation_result = value
        else:
            self._interpretation_result = ReportInterpretationDetailResponse.from_alipay_dict(value)
    @property
    def report_list(self):
        return self._report_list

    @report_list.setter
    def report_list(self, value):
        if isinstance(value, list):
            self._report_list = list()
            for i in value:
                if isinstance(i, ReportDetailResponse):
                    self._report_list.append(i)
                else:
                    self._report_list.append(ReportDetailResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthfulfillmentReportinterpretationQueryResponse, self).parse_response_content(response_content)
        if 'interpretation_result' in response:
            self.interpretation_result = response['interpretation_result']
        if 'report_list' in response:
            self.report_list = response['report_list']
