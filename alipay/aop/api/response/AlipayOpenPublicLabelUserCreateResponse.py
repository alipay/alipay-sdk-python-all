#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicLabelUserCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLabelUserCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLabelUserCreateResponse, self).parse_response_content(response_content)
