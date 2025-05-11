#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayContentLiveAdvanceModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLiveAdvanceModifyResponse, self).__init__()
        self._alipay_advance_id = None
        self._biz_trace_id = None

    @property
    def alipay_advance_id(self):
        return self._alipay_advance_id

    @alipay_advance_id.setter
    def alipay_advance_id(self, value):
        self._alipay_advance_id = value
    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayContentLiveAdvanceModifyResponse, self).parse_response_content(response_content)
        if 'alipay_advance_id' in response:
            self.alipay_advance_id = response['alipay_advance_id']
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
