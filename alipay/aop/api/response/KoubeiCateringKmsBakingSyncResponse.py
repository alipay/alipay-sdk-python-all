#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringKmsBakingSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringKmsBakingSyncResponse, self).__init__()
        self._check_msg = None
        self._check_pass = None
        self._sync_count = None

    @property
    def check_msg(self):
        return self._check_msg

    @check_msg.setter
    def check_msg(self, value):
        self._check_msg = value
    @property
    def check_pass(self):
        return self._check_pass

    @check_pass.setter
    def check_pass(self, value):
        self._check_pass = value
    @property
    def sync_count(self):
        return self._sync_count

    @sync_count.setter
    def sync_count(self, value):
        self._sync_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringKmsBakingSyncResponse, self).parse_response_content(response_content)
        if 'check_msg' in response:
            self.check_msg = response['check_msg']
        if 'check_pass' in response:
            self.check_pass = response['check_pass']
        if 'sync_count' in response:
            self.sync_count = response['sync_count']
