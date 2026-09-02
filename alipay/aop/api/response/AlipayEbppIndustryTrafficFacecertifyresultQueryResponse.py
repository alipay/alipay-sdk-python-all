#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryTrafficFacecertifyresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryTrafficFacecertifyresultQueryResponse, self).__init__()
        self._verified = None
        self._zim_id = None

    @property
    def verified(self):
        return self._verified

    @verified.setter
    def verified(self, value):
        self._verified = value
    @property
    def zim_id(self):
        return self._zim_id

    @zim_id.setter
    def zim_id(self, value):
        self._zim_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryTrafficFacecertifyresultQueryResponse, self).parse_response_content(response_content)
        if 'verified' in response:
            self.verified = response['verified']
        if 'zim_id' in response:
            self.zim_id = response['zim_id']
