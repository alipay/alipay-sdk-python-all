#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiEventReportDataResult import OpenApiEventReportDataResult


class AlipayCloudCloudpromoEventreportEventoverviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoEventreportEventoverviewQueryResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, OpenApiEventReportDataResult):
            self._result = value
        else:
            self._result = OpenApiEventReportDataResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoEventreportEventoverviewQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
