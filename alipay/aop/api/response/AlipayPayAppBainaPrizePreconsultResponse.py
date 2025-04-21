#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppBainaPrizePreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppBainaPrizePreconsultResponse, self).__init__()
        self._allow_award = None

    @property
    def allow_award(self):
        return self._allow_award

    @allow_award.setter
    def allow_award(self, value):
        self._allow_award = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppBainaPrizePreconsultResponse, self).parse_response_content(response_content)
        if 'allow_award' in response:
            self.allow_award = response['allow_award']
