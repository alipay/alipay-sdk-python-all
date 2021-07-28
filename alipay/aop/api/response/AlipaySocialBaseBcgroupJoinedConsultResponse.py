#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseBcgroupJoinedConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseBcgroupJoinedConsultResponse, self).__init__()
        self._joined = None

    @property
    def joined(self):
        return self._joined

    @joined.setter
    def joined(self, value):
        self._joined = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseBcgroupJoinedConsultResponse, self).parse_response_content(response_content)
        if 'joined' in response:
            self.joined = response['joined']
