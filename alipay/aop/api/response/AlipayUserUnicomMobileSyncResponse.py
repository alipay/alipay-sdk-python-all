#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserUnicomMobileSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUnicomMobileSyncResponse, self).__init__()
        self._mobile_sync_result = None
        self._out_biz_no = None

    @property
    def mobile_sync_result(self):
        return self._mobile_sync_result

    @mobile_sync_result.setter
    def mobile_sync_result(self, value):
        self._mobile_sync_result = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserUnicomMobileSyncResponse, self).parse_response_content(response_content)
        if 'mobile_sync_result' in response:
            self.mobile_sync_result = response['mobile_sync_result']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
