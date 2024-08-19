#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunObjectstorageCdsRefreshResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageCdsRefreshResponse, self).__init__()
        self._requestid = None

    @property
    def requestid(self):
        return self._requestid

    @requestid.setter
    def requestid(self, value):
        self._requestid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageCdsRefreshResponse, self).parse_response_content(response_content)
        if 'requestid' in response:
            self.requestid = response['requestid']
