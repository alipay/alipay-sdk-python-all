#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicPersonalizedExtensionDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicPersonalizedExtensionDeleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicPersonalizedExtensionDeleteResponse, self).parse_response_content(response_content)
