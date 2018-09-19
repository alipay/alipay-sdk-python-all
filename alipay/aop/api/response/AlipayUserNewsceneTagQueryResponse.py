#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserNewsceneTagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserNewsceneTagQueryResponse, self).__init__()
        self._tags_result = None

    @property
    def tags_result(self):
        return self._tags_result

    @tags_result.setter
    def tags_result(self, value):
        self._tags_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserNewsceneTagQueryResponse, self).parse_response_content(response_content)
        if 'tags_result' in response:
            self.tags_result = response['tags_result']
