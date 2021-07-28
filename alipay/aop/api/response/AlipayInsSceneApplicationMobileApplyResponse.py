#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneApplicationMobileApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationMobileApplyResponse, self).__init__()
        self._card_url = None
        self._out_biz_no = None
        self._policy_no = None

    @property
    def card_url(self):
        return self._card_url

    @card_url.setter
    def card_url(self, value):
        self._card_url = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationMobileApplyResponse, self).parse_response_content(response_content)
        if 'card_url' in response:
            self.card_url = response['card_url']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
