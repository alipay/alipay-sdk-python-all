#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenClaimDigestDTO import InsOpenClaimDigestDTO


class AlipayInsSceneEcommerceClaimApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceClaimApplyResponse, self).__init__()
        self._claim_digest = None

    @property
    def claim_digest(self):
        return self._claim_digest

    @claim_digest.setter
    def claim_digest(self, value):
        if isinstance(value, InsOpenClaimDigestDTO):
            self._claim_digest = value
        else:
            self._claim_digest = InsOpenClaimDigestDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceClaimApplyResponse, self).parse_response_content(response_content)
        if 'claim_digest' in response:
            self.claim_digest = response['claim_digest']
