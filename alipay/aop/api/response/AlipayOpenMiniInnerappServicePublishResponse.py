#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerappServicePublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerappServicePublishResponse, self).__init__()
        self._merchandise_id = None

    @property
    def merchandise_id(self):
        return self._merchandise_id

    @merchandise_id.setter
    def merchandise_id(self, value):
        self._merchandise_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerappServicePublishResponse, self).parse_response_content(response_content)
        if 'merchandise_id' in response:
            self.merchandise_id = response['merchandise_id']
