#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneSettleWorkersaasSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneSettleWorkersaasSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneSettleWorkersaasSyncResponse, self).parse_response_content(response_content)
