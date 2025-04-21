#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftPoapDistributeSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftPoapDistributeSubmitResponse, self).__init__()
        self._medal_id = None
        self._medal_meta_id = None

    @property
    def medal_id(self):
        return self._medal_id

    @medal_id.setter
    def medal_id(self, value):
        self._medal_id = value
    @property
    def medal_meta_id(self):
        return self._medal_meta_id

    @medal_meta_id.setter
    def medal_meta_id(self, value):
        self._medal_meta_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftPoapDistributeSubmitResponse, self).parse_response_content(response_content)
        if 'medal_id' in response:
            self.medal_id = response['medal_id']
        if 'medal_meta_id' in response:
            self.medal_meta_id = response['medal_meta_id']
