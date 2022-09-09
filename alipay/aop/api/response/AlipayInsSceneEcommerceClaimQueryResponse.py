#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenClaimDigestDTO import InsOpenClaimDigestDTO


class AlipayInsSceneEcommerceClaimQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneEcommerceClaimQueryResponse, self).__init__()
        self._claim_list = None

    @property
    def claim_list(self):
        return self._claim_list

    @claim_list.setter
    def claim_list(self, value):
        if isinstance(value, list):
            self._claim_list = list()
            for i in value:
                if isinstance(i, InsOpenClaimDigestDTO):
                    self._claim_list.append(i)
                else:
                    self._claim_list.append(InsOpenClaimDigestDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneEcommerceClaimQueryResponse, self).parse_response_content(response_content)
        if 'claim_list' in response:
            self.claim_list = response['claim_list']
