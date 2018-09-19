#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppYufanlingsanyaowuYufalingsanyaowuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppYufanlingsanyaowuYufalingsanyaowuQueryResponse, self).__init__()
        self._userid = None

    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppYufanlingsanyaowuYufalingsanyaowuQueryResponse, self).parse_response_content(response_content)
        if 'userid' in response:
            self.userid = response['userid']
