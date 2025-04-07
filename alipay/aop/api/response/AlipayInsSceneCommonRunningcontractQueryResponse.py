#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsOpenPurchaseContractInfoDigestDTO import InsOpenPurchaseContractInfoDigestDTO


class AlipayInsSceneCommonRunningcontractQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonRunningcontractQueryResponse, self).__init__()
        self._contract_digest = None

    @property
    def contract_digest(self):
        return self._contract_digest

    @contract_digest.setter
    def contract_digest(self, value):
        if isinstance(value, InsOpenPurchaseContractInfoDigestDTO):
            self._contract_digest = value
        else:
            self._contract_digest = InsOpenPurchaseContractInfoDigestDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonRunningcontractQueryResponse, self).parse_response_content(response_content)
        if 'contract_digest' in response:
            self.contract_digest = response['contract_digest']
