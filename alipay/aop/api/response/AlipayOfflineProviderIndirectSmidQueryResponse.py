#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderIndirectSmidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderIndirectSmidQueryResponse, self).__init__()
        self._smid = None

    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderIndirectSmidQueryResponse, self).parse_response_content(response_content)
        if 'smid' in response:
            self.smid = response['smid']
