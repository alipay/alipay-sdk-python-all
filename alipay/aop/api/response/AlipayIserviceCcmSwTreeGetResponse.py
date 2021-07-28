#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmSwTreeGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwTreeGetResponse, self).__init__()
        self._tree = None

    @property
    def tree(self):
        return self._tree

    @tree.setter
    def tree(self, value):
        self._tree = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwTreeGetResponse, self).parse_response_content(response_content)
        if 'tree' in response:
            self.tree = response['tree']
