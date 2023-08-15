#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseHttpaccessCnameGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpaccessCnameGetResponse, self).__init__()
        self._cname = None

    @property
    def cname(self):
        return self._cname

    @cname.setter
    def cname(self, value):
        self._cname = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpaccessCnameGetResponse, self).parse_response_content(response_content)
        if 'cname' in response:
            self.cname = response['cname']
