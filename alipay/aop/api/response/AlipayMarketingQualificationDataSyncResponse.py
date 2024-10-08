#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingQualificationDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQualificationDataSyncResponse, self).__init__()
        self._operate_id = None

    @property
    def operate_id(self):
        return self._operate_id

    @operate_id.setter
    def operate_id(self, value):
        self._operate_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQualificationDataSyncResponse, self).parse_response_content(response_content)
        if 'operate_id' in response:
            self.operate_id = response['operate_id']
