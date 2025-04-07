#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceClaimSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceClaimSyncResponse, self).__init__()
        self._ant_claim_no = None

    @property
    def ant_claim_no(self):
        return self._ant_claim_no

    @ant_claim_no.setter
    def ant_claim_no(self, value):
        self._ant_claim_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceClaimSyncResponse, self).parse_response_content(response_content)
        if 'ant_claim_no' in response:
            self.ant_claim_no = response['ant_claim_no']
