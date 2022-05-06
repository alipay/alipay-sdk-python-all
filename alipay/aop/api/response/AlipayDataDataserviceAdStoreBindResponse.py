#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdStoreBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdStoreBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdStoreBindResponse, self).parse_response_content(response_content)
