#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMemberRegioninsureApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMemberRegioninsureApplyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayUserMemberRegioninsureApplyResponse, self).parse_response_content(response_content)
