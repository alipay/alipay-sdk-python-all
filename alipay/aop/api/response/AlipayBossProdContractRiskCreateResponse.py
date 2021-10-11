#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenAPIContractRiskResult import OpenAPIContractRiskResult


class AlipayBossProdContractRiskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdContractRiskCreateResponse, self).__init__()
        self._business_id = None
        self._open_api_contract_risk_result_list = None
        self._result_code = None
        self._result_message = None
        self._result_success = None
        self._result_trace_id = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def open_api_contract_risk_result_list(self):
        return self._open_api_contract_risk_result_list

    @open_api_contract_risk_result_list.setter
    def open_api_contract_risk_result_list(self, value):
        if isinstance(value, list):
            self._open_api_contract_risk_result_list = list()
            for i in value:
                if isinstance(i, OpenAPIContractRiskResult):
                    self._open_api_contract_risk_result_list.append(i)
                else:
                    self._open_api_contract_risk_result_list.append(OpenAPIContractRiskResult.from_alipay_dict(i))
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def result_success(self):
        return self._result_success

    @result_success.setter
    def result_success(self, value):
        self._result_success = value
    @property
    def result_trace_id(self):
        return self._result_trace_id

    @result_trace_id.setter
    def result_trace_id(self, value):
        self._result_trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdContractRiskCreateResponse, self).parse_response_content(response_content)
        if 'business_id' in response:
            self.business_id = response['business_id']
        if 'open_api_contract_risk_result_list' in response:
            self.open_api_contract_risk_result_list = response['open_api_contract_risk_result_list']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
        if 'result_success' in response:
            self.result_success = response['result_success']
        if 'result_trace_id' in response:
            self.result_trace_id = response['result_trace_id']
