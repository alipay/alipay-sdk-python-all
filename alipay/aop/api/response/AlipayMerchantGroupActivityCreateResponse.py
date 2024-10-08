#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupActivityCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupActivityCreateResponse, self).__init__()
        self._group_activity_id = None

    @property
    def group_activity_id(self):
        return self._group_activity_id

    @group_activity_id.setter
    def group_activity_id(self, value):
        self._group_activity_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupActivityCreateResponse, self).parse_response_content(response_content)
        if 'group_activity_id' in response:
            self.group_activity_id = response['group_activity_id']
