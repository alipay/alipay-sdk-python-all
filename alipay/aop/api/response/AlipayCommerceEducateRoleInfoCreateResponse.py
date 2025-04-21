#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateRoleInfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRoleInfoCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRoleInfoCreateResponse, self).parse_response_content(response_content)
