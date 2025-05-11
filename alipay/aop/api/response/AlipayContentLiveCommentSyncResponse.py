#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayContentLiveCommentSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLiveCommentSyncResponse, self).__init__()
        self._alipay_comment_id = None

    @property
    def alipay_comment_id(self):
        return self._alipay_comment_id

    @alipay_comment_id.setter
    def alipay_comment_id(self, value):
        self._alipay_comment_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayContentLiveCommentSyncResponse, self).parse_response_content(response_content)
        if 'alipay_comment_id' in response:
            self.alipay_comment_id = response['alipay_comment_id']
