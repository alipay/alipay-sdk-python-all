#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityNoticePublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityNoticePublishResponse, self).__init__()
        self._alipay_notice_id = None

    @property
    def alipay_notice_id(self):
        return self._alipay_notice_id

    @alipay_notice_id.setter
    def alipay_notice_id(self, value):
        self._alipay_notice_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityNoticePublishResponse, self).parse_response_content(response_content)
        if 'alipay_notice_id' in response:
            self.alipay_notice_id = response['alipay_notice_id']
