#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EntityPriorRiskVO import EntityPriorRiskVO


class AlipayAccountFinriskGiriskrequestCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountFinriskGiriskrequestCreateResponse, self).__init__()
        self._result_code = None
        self._result_code_third = None
        self._result_desc = None
        self._risk_details = None
        self._risk_result_code = None
        self._success = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_code_third(self):
        return self._result_code_third

    @result_code_third.setter
    def result_code_third(self, value):
        self._result_code_third = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def risk_details(self):
        return self._risk_details

    @risk_details.setter
    def risk_details(self, value):
        if isinstance(value, list):
            self._risk_details = list()
            for i in value:
                if isinstance(i, EntityPriorRiskVO):
                    self._risk_details.append(i)
                else:
                    self._risk_details.append(EntityPriorRiskVO.from_alipay_dict(i))
    @property
    def risk_result_code(self):
        return self._risk_result_code

    @risk_result_code.setter
    def risk_result_code(self, value):
        self._risk_result_code = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountFinriskGiriskrequestCreateResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_code_third' in response:
            self.result_code_third = response['result_code_third']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'risk_details' in response:
            self.risk_details = response['risk_details']
        if 'risk_result_code' in response:
            self.risk_result_code = response['risk_result_code']
        if 'success' in response:
            self.success = response['success']
