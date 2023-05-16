#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityEntranceguarddataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityEntranceguarddataSyncResponse, self).__init__()
        self._out_user_id = None

    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityEntranceguarddataSyncResponse, self).parse_response_content(response_content)
        if 'out_user_id' in response:
            self.out_user_id = response['out_user_id']
