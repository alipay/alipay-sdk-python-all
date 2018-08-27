#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiItemExtitemExistedQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemExtitemExistedQueryResponse, self).__init__()
        self._existed_list = None

    @property
    def existed_list(self):
        return self._existed_list

    @existed_list.setter
    def existed_list(self, value):
        if isinstance(value, list):
            self._existed_list = list()
            for i in value:
                self._existed_list.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiItemExtitemExistedQueryResponse, self).parse_response_content(response_content)
        if 'existed_list' in response:
            self.existed_list = response['existed_list']
