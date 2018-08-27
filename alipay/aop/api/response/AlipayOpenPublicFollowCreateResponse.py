#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicFollowCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicFollowCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicFollowCreateResponse, self).parse_response_content(response_content)
