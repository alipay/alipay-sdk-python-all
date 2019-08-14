#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdGroupCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdGroupCreateormodifyResponse, self).__init__()
        self._group_id = None
        self._group_outer_id = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_outer_id(self):
        return self._group_outer_id

    @group_outer_id.setter
    def group_outer_id(self, value):
        self._group_outer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdGroupCreateormodifyResponse, self).parse_response_content(response_content)
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'group_outer_id' in response:
            self.group_outer_id = response['group_outer_id']
