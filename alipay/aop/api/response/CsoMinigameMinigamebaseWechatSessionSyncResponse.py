#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class CsoMinigameMinigamebaseWechatSessionSyncResponse(AlipayResponse):

    def __init__(self):
        super(CsoMinigameMinigamebaseWechatSessionSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(CsoMinigameMinigamebaseWechatSessionSyncResponse, self).parse_response_content(response_content)
