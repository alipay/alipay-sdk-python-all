#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityThirdpartybillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityThirdpartybillCreateResponse, self).__init__()
        self._alipay_biz_no = None

    @property
    def alipay_biz_no(self):
        return self._alipay_biz_no

    @alipay_biz_no.setter
    def alipay_biz_no(self, value):
        self._alipay_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityThirdpartybillCreateResponse, self).parse_response_content(response_content)
        if 'alipay_biz_no' in response:
            self.alipay_biz_no = response['alipay_biz_no']
