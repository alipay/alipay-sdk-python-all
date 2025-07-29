#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RcMedConsultResult import RcMedConsultResult


class AlipaySecurityDataMedicalSuwenConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataMedicalSuwenConsultResponse, self).__init__()
        self._consult_result_list = None

    @property
    def consult_result_list(self):
        return self._consult_result_list

    @consult_result_list.setter
    def consult_result_list(self, value):
        if isinstance(value, list):
            self._consult_result_list = list()
            for i in value:
                if isinstance(i, RcMedConsultResult):
                    self._consult_result_list.append(i)
                else:
                    self._consult_result_list.append(RcMedConsultResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataMedicalSuwenConsultResponse, self).parse_response_content(response_content)
        if 'consult_result_list' in response:
            self.consult_result_list = response['consult_result_list']
