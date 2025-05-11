#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayContentLiveLivedataCurrentliveQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLiveLivedataCurrentliveQueryResponse, self).__init__()
        self._alipay_live_id = None
        self._biz_trace_id = None
        self._comment_uv = None
        self._num_gift_recipients = None
        self._owner_cash_flow = None
        self._play_uv = None
        self._praise_uv = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def comment_uv(self):
        return self._comment_uv

    @comment_uv.setter
    def comment_uv(self, value):
        self._comment_uv = value
    @property
    def num_gift_recipients(self):
        return self._num_gift_recipients

    @num_gift_recipients.setter
    def num_gift_recipients(self, value):
        self._num_gift_recipients = value
    @property
    def owner_cash_flow(self):
        return self._owner_cash_flow

    @owner_cash_flow.setter
    def owner_cash_flow(self, value):
        self._owner_cash_flow = value
    @property
    def play_uv(self):
        return self._play_uv

    @play_uv.setter
    def play_uv(self, value):
        self._play_uv = value
    @property
    def praise_uv(self):
        return self._praise_uv

    @praise_uv.setter
    def praise_uv(self, value):
        self._praise_uv = value

    def parse_response_content(self, response_content):
        response = super(AlipayContentLiveLivedataCurrentliveQueryResponse, self).parse_response_content(response_content)
        if 'alipay_live_id' in response:
            self.alipay_live_id = response['alipay_live_id']
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'comment_uv' in response:
            self.comment_uv = response['comment_uv']
        if 'num_gift_recipients' in response:
            self.num_gift_recipients = response['num_gift_recipients']
        if 'owner_cash_flow' in response:
            self.owner_cash_flow = response['owner_cash_flow']
        if 'play_uv' in response:
            self.play_uv = response['play_uv']
        if 'praise_uv' in response:
            self.praise_uv = response['praise_uv']
