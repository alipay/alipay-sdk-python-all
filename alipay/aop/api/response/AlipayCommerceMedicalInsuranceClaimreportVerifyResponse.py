#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ClaimResult import ClaimResult


class AlipayCommerceMedicalInsuranceClaimreportVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceClaimreportVerifyResponse, self).__init__()
        self._claim_result_list = None
        self._secret_key = None

    @property
    def claim_result_list(self):
        return self._claim_result_list

    @claim_result_list.setter
    def claim_result_list(self, value):
        if isinstance(value, list):
            self._claim_result_list = list()
            for i in value:
                if isinstance(i, ClaimResult):
                    self._claim_result_list.append(i)
                else:
                    self._claim_result_list.append(ClaimResult.from_alipay_dict(i))
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceClaimreportVerifyResponse, self).parse_response_content(response_content)
        if 'claim_result_list' in response:
            self.claim_result_list = response['claim_result_list']
        if 'secret_key' in response:
            self.secret_key = response['secret_key']
