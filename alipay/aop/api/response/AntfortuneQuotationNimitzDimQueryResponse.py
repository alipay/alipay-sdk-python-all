#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RsData import RsData
from alipay.aop.api.domain.Status import Status


class AntfortuneQuotationNimitzDimQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneQuotationNimitzDimQueryResponse, self).__init__()
        self._result = None
        self._result_data = None
        self._result_status = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, RsData):
            self._result_data = value
        else:
            self._result_data = RsData.from_alipay_dict(value)
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        if isinstance(value, Status):
            self._result_status = value
        else:
            self._result_status = Status.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntfortuneQuotationNimitzDimQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'result_data' in response:
            self.result_data = response['result_data']
        if 'result_status' in response:
            self.result_status = response['result_status']
