#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoAgentBehaviorModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAgentBehaviorModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAgentBehaviorModifyResponse, self).parse_response_content(response_content)
