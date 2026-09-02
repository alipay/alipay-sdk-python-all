#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInstPolicyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInstPolicyQueryResponse, self).__init__()
        self._electronic_policy_url = None
        self._inst_policy_no = None

    @property
    def electronic_policy_url(self):
        return self._electronic_policy_url

    @electronic_policy_url.setter
    def electronic_policy_url(self, value):
        self._electronic_policy_url = value
    @property
    def inst_policy_no(self):
        return self._inst_policy_no

    @inst_policy_no.setter
    def inst_policy_no(self, value):
        self._inst_policy_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInstPolicyQueryResponse, self).parse_response_content(response_content)
        if 'electronic_policy_url' in response:
            self.electronic_policy_url = response['electronic_policy_url']
        if 'inst_policy_no' in response:
            self.inst_policy_no = response['inst_policy_no']
