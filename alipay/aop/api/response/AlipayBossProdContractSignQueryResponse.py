#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContractQueryDTO import ContractQueryDTO


class AlipayBossProdContractSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdContractSignQueryResponse, self).__init__()
        self._contract_title = None
        self._result_code = None
        self._result_data = None
        self._result_message = None
        self._result_success = None
        self._result_trace_id = None
        self._source_system_id = None

    @property
    def contract_title(self):
        return self._contract_title

    @contract_title.setter
    def contract_title(self, value):
        self._contract_title = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, ContractQueryDTO):
            self._result_data = value
        else:
            self._result_data = ContractQueryDTO.from_alipay_dict(value)
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
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdContractSignQueryResponse, self).parse_response_content(response_content)
        if 'contract_title' in response:
            self.contract_title = response['contract_title']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_data' in response:
            self.result_data = response['result_data']
        if 'result_message' in response:
            self.result_message = response['result_message']
        if 'result_success' in response:
            self.result_success = response['result_success']
        if 'result_trace_id' in response:
            self.result_trace_id = response['result_trace_id']
        if 'source_system_id' in response:
            self.source_system_id = response['source_system_id']
