#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyPayorderNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyPayorderNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyPayorderNotifyResponse, self).parse_response_content(response_content)
