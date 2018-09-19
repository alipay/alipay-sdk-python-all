#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseGroupCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseGroupCreateResponse, self).__init__()
        self._group_id = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseGroupCreateResponse, self).parse_response_content(response_content)
        if 'group_id' in response:
            self.group_id = response['group_id']
