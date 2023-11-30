#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbasePassinfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassinfoCreateResponse, self).__init__()
        self._authorization = None

    @property
    def authorization(self):
        return self._authorization

    @authorization.setter
    def authorization(self, value):
        self._authorization = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassinfoCreateResponse, self).parse_response_content(response_content)
        if 'authorization' in response:
            self.authorization = response['authorization']
