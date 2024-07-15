#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneChannelsaleVoucherCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneChannelsaleVoucherCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneChannelsaleVoucherCancelResponse, self).parse_response_content(response_content)
