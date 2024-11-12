#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateRosterInfoSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterInfoSaveResponse, self).__init__()
        self._roster_id = None

    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterInfoSaveResponse, self).parse_response_content(response_content)
        if 'roster_id' in response:
            self.roster_id = response['roster_id']
