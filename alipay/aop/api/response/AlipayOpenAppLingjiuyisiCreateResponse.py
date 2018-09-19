#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppLingjiuyisiCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppLingjiuyisiCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppLingjiuyisiCreateResponse, self).parse_response_content(response_content)
