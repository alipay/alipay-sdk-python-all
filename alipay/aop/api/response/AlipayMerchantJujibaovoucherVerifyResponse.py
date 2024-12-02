#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChinaMobileOutContractRoot import ChinaMobileOutContractRoot


class AlipayMerchantJujibaovoucherVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantJujibaovoucherVerifyResponse, self).__init__()
        self._contract_root = None

    @property
    def contract_root(self):
        return self._contract_root

    @contract_root.setter
    def contract_root(self, value):
        if isinstance(value, ChinaMobileOutContractRoot):
            self._contract_root = value
        else:
            self._contract_root = ChinaMobileOutContractRoot.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantJujibaovoucherVerifyResponse, self).parse_response_content(response_content)
        if 'contract_root' in response:
            self.contract_root = response['contract_root']
