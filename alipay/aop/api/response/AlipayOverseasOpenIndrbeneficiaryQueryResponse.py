#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndrISVBeneficiaryDTO import IndrISVBeneficiaryDTO
from alipay.aop.api.domain.IndrISVResult import IndrISVResult


class AlipayOverseasOpenIndrbeneficiaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenIndrbeneficiaryQueryResponse, self).__init__()
        self._beneficiary_list = None
        self._result = None

    @property
    def beneficiary_list(self):
        return self._beneficiary_list

    @beneficiary_list.setter
    def beneficiary_list(self, value):
        if isinstance(value, IndrISVBeneficiaryDTO):
            self._beneficiary_list = value
        else:
            self._beneficiary_list = IndrISVBeneficiaryDTO.from_alipay_dict(value)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, IndrISVResult):
            self._result = value
        else:
            self._result = IndrISVResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenIndrbeneficiaryQueryResponse, self).parse_response_content(response_content)
        if 'beneficiary_list' in response:
            self.beneficiary_list = response['beneficiary_list']
        if 'result' in response:
            self.result = response['result']
