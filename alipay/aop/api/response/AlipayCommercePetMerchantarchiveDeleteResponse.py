#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePetMerchantarchiveDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePetMerchantarchiveDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommercePetMerchantarchiveDeleteResponse, self).parse_response_content(response_content)
