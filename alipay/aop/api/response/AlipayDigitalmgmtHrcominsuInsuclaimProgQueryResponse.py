#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsuClaimVo import InsuClaimVo


class AlipayDigitalmgmtHrcominsuInsuclaimProgQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrcominsuInsuclaimProgQueryResponse, self).__init__()
        self._insu_claim_vos = None

    @property
    def insu_claim_vos(self):
        return self._insu_claim_vos

    @insu_claim_vos.setter
    def insu_claim_vos(self, value):
        if isinstance(value, list):
            self._insu_claim_vos = list()
            for i in value:
                if isinstance(i, InsuClaimVo):
                    self._insu_claim_vos.append(i)
                else:
                    self._insu_claim_vos.append(InsuClaimVo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrcominsuInsuclaimProgQueryResponse, self).parse_response_content(response_content)
        if 'insu_claim_vos' in response:
            self.insu_claim_vos = response['insu_claim_vos']
