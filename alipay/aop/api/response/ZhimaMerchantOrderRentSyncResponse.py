#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderRentSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderRentSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderRentSyncResponse, self).parse_response_content(response_content)
