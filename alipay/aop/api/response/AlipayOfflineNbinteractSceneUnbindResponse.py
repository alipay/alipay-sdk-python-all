#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineNbinteractSceneUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineNbinteractSceneUnbindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineNbinteractSceneUnbindResponse, self).parse_response_content(response_content)
