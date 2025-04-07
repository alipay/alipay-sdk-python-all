#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpSceneAccountSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpSceneAccountSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpSceneAccountSyncResponse, self).parse_response_content(response_content)
