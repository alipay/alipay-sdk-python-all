#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayUserDetail import AlipayUserDetail


class AlipayUserGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGetResponse, self).__init__()
        self._alipay_user_detail = None

    @property
    def alipay_user_detail(self):
        return self._alipay_user_detail

    @alipay_user_detail.setter
    def alipay_user_detail(self, value):
        if isinstance(value, AlipayUserDetail):
            self._alipay_user_detail = value
        else:
            self._alipay_user_detail = AlipayUserDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserGetResponse, self).parse_response_content(response_content)
        if 'alipay_user_detail' in response:
            self.alipay_user_detail = response['alipay_user_detail']
