#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamecenterSwitchapptaskCompleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamecenterSwitchapptaskCompleteResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserGamecenterSwitchapptaskCompleteResponse, self).parse_response_content(response_content)
