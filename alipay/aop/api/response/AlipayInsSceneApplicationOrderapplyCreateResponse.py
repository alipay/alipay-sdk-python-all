#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneApplicationOrderapplyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationOrderapplyCreateResponse, self).__init__()
        self._biz_flow_no = None
        self._policy_no = None

    @property
    def biz_flow_no(self):
        return self._biz_flow_no

    @biz_flow_no.setter
    def biz_flow_no(self, value):
        self._biz_flow_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationOrderapplyCreateResponse, self).parse_response_content(response_content)
        if 'biz_flow_no' in response:
            self.biz_flow_no = response['biz_flow_no']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
