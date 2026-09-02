#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAffinitycardPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAffinitycardPreconsultResponse, self).__init__()
        self._can_apply = None

    @property
    def can_apply(self):
        return self._can_apply

    @can_apply.setter
    def can_apply(self, value):
        self._can_apply = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAffinitycardPreconsultResponse, self).parse_response_content(response_content)
        if 'can_apply' in response:
            self.can_apply = response['can_apply']
