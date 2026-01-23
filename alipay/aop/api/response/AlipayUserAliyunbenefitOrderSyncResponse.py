#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAliyunbenefitOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAliyunbenefitOrderSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserAliyunbenefitOrderSyncResponse, self).parse_response_content(response_content)
