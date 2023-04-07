#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppOpenidApplyorderSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenidApplyorderSubmitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenidApplyorderSubmitResponse, self).parse_response_content(response_content)
