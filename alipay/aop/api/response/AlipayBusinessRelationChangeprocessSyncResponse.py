#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessRelationChangeprocessSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessRelationChangeprocessSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayBusinessRelationChangeprocessSyncResponse, self).parse_response_content(response_content)
