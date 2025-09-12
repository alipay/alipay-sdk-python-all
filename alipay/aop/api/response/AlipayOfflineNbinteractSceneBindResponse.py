#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineNbinteractSceneBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineNbinteractSceneBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOfflineNbinteractSceneBindResponse, self).parse_response_content(response_content)
