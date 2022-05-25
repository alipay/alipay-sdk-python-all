#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpLeadsExpandCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpLeadsExpandCreateResponse, self).__init__()
        self._leads_id = None

    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpLeadsExpandCreateResponse, self).parse_response_content(response_content)
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
