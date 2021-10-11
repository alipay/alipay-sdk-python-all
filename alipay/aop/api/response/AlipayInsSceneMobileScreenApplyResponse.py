#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneMobileScreenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneMobileScreenApplyResponse, self).__init__()
        self._out_biz_no = None
        self._policy_no = None
        self._policy_url = None
        self._premium = None

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
    @property
    def policy_url(self):
        return self._policy_url

    @policy_url.setter
    def policy_url(self, value):
        self._policy_url = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneMobileScreenApplyResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'policy_url' in response:
            self.policy_url = response['policy_url']
        if 'premium' in response:
            self.premium = response['premium']
