#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMemberCitycardSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberCitycardSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberCitycardSyncResponse, self).parse_response_content(response_content)
