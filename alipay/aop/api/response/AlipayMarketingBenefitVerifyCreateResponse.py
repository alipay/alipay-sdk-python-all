#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBenefitVerifyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitVerifyCreateResponse, self).__init__()
        self._need_verify = None
        self._verify_id = None
        self._verify_scene = None
        self._verify_url = None

    @property
    def need_verify(self):
        return self._need_verify

    @need_verify.setter
    def need_verify(self, value):
        self._need_verify = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value
    @property
    def verify_scene(self):
        return self._verify_scene

    @verify_scene.setter
    def verify_scene(self, value):
        self._verify_scene = value
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitVerifyCreateResponse, self).parse_response_content(response_content)
        if 'need_verify' in response:
            self.need_verify = response['need_verify']
        if 'verify_id' in response:
            self.verify_id = response['verify_id']
        if 'verify_scene' in response:
            self.verify_scene = response['verify_scene']
        if 'verify_url' in response:
            self.verify_url = response['verify_url']
