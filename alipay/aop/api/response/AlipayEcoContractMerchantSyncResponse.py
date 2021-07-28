#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoContractMerchantSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoContractMerchantSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoContractMerchantSyncResponse, self).parse_response_content(response_content)
