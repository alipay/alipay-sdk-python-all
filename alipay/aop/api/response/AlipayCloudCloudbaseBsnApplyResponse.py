#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseBsnApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseBsnApplyResponse, self).__init__()
        self._bsn = None

    @property
    def bsn(self):
        return self._bsn

    @bsn.setter
    def bsn(self, value):
        self._bsn = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseBsnApplyResponse, self).parse_response_content(response_content)
        if 'bsn' in response:
            self.bsn = response['bsn']
