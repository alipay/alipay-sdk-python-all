#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppHexidemoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppHexidemoModifyResponse, self).__init__()
        self._wegdsfgvdsgds = None

    @property
    def wegdsfgvdsgds(self):
        return self._wegdsfgvdsgds

    @wegdsfgvdsgds.setter
    def wegdsfgvdsgds(self, value):
        self._wegdsfgvdsgds = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppHexidemoModifyResponse, self).parse_response_content(response_content)
        if 'wegdsfgvdsgds' in response:
            self.wegdsfgvdsgds = response['wegdsfgvdsgds']
