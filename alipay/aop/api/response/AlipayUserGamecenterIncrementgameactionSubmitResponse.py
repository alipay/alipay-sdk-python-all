#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamecenterIncrementgameactionSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamecenterIncrementgameactionSubmitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserGamecenterIncrementgameactionSubmitResponse, self).parse_response_content(response_content)
