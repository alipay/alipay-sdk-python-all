#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCampusIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusIdentityQueryResponse, self).__init__()
        self._college_online_tag = None

    @property
    def college_online_tag(self):
        return self._college_online_tag

    @college_online_tag.setter
    def college_online_tag(self, value):
        self._college_online_tag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusIdentityQueryResponse, self).parse_response_content(response_content)
        if 'college_online_tag' in response:
            self.college_online_tag = response['college_online_tag']
