#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantBorrowEntityUploadResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantBorrowEntityUploadResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantBorrowEntityUploadResponse, self).parse_response_content(response_content)
