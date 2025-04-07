#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayContentLifeaccountStatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLifeaccountStatusSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayContentLifeaccountStatusSyncResponse, self).parse_response_content(response_content)
