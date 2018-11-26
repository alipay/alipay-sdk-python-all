#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosDeskCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDeskCreateResponse, self).__init__()
        self._ids = None

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if isinstance(value, list):
            self._ids = list()
            for i in value:
                self._ids.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDeskCreateResponse, self).parse_response_content(response_content)
        if 'ids' in response:
            self.ids = response['ids']
