#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundInstcardOpenCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundInstcardOpenCancelResponse, self).__init__()
        self._canceled = None

    @property
    def canceled(self):
        return self._canceled

    @canceled.setter
    def canceled(self, value):
        self._canceled = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundInstcardOpenCancelResponse, self).parse_response_content(response_content)
        if 'canceled' in response:
            self.canceled = response['canceled']
