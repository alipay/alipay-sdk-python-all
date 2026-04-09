#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class RobbyOpenTaskCancelResponse(AlipayResponse):

    def __init__(self):
        super(RobbyOpenTaskCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(RobbyOpenTaskCancelResponse, self).parse_response_content(response_content)
