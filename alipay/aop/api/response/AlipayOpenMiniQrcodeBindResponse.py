#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniQrcodeBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniQrcodeBindResponse, self).__init__()
        self._route_group = None

    @property
    def route_group(self):
        return self._route_group

    @route_group.setter
    def route_group(self, value):
        self._route_group = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniQrcodeBindResponse, self).parse_response_content(response_content)
        if 'route_group' in response:
            self.route_group = response['route_group']
