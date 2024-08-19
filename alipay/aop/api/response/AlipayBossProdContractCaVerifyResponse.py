#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PdfCertificateResult import PdfCertificateResult


class AlipayBossProdContractCaVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdContractCaVerifyResponse, self).__init__()
        self._result_data = None
        self._result_trace_id = None

    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, list):
            self._result_data = list()
            for i in value:
                if isinstance(i, PdfCertificateResult):
                    self._result_data.append(i)
                else:
                    self._result_data.append(PdfCertificateResult.from_alipay_dict(i))
    @property
    def result_trace_id(self):
        return self._result_trace_id

    @result_trace_id.setter
    def result_trace_id(self, value):
        self._result_trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdContractCaVerifyResponse, self).parse_response_content(response_content)
        if 'result_data' in response:
            self.result_data = response['result_data']
        if 'result_trace_id' in response:
            self.result_trace_id = response['result_trace_id']
