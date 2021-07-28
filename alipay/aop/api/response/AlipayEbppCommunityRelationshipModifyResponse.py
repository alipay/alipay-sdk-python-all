#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityRelationshipModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityRelationshipModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityRelationshipModifyResponse, self).parse_response_content(response_content)
