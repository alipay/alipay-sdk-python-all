#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftTenantidFansidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftTenantidFansidQueryResponse, self).__init__()
        self._fans_id = None

    @property
    def fans_id(self):
        return self._fans_id

    @fans_id.setter
    def fans_id(self, value):
        self._fans_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftTenantidFansidQueryResponse, self).parse_response_content(response_content)
        if 'fans_id' in response:
            self.fans_id = response['fans_id']
