#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMallApplyruleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMallApplyruleCreateResponse, self).__init__()
        self._biz_rule_id = None

    @property
    def biz_rule_id(self):
        return self._biz_rule_id

    @biz_rule_id.setter
    def biz_rule_id(self, value):
        self._biz_rule_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMallApplyruleCreateResponse, self).parse_response_content(response_content)
        if 'biz_rule_id' in response:
            self.biz_rule_id = response['biz_rule_id']
