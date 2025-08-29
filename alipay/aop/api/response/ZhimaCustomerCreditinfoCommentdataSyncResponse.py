#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerCreditinfoCommentdataSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerCreditinfoCommentdataSyncResponse, self).__init__()
        self._sync_info = None

    @property
    def sync_info(self):
        return self._sync_info

    @sync_info.setter
    def sync_info(self, value):
        self._sync_info = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerCreditinfoCommentdataSyncResponse, self).parse_response_content(response_content)
        if 'sync_info' in response:
            self.sync_info = response['sync_info']
