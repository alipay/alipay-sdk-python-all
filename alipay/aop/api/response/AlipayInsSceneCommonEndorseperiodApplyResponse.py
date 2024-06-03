#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneCommonEndorseperiodApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCommonEndorseperiodApplyResponse, self).__init__()
        self._endorse_no = None

    @property
    def endorse_no(self):
        return self._endorse_no

    @endorse_no.setter
    def endorse_no(self, value):
        self._endorse_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCommonEndorseperiodApplyResponse, self).parse_response_content(response_content)
        if 'endorse_no' in response:
            self.endorse_no = response['endorse_no']
