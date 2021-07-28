#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotSnCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotSnCreateResponse, self).__init__()
        self._apply_id = None
        self._sn_list = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def sn_list(self):
        return self._sn_list

    @sn_list.setter
    def sn_list(self, value):
        if isinstance(value, list):
            self._sn_list = list()
            for i in value:
                self._sn_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotSnCreateResponse, self).parse_response_content(response_content)
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'sn_list' in response:
            self.sn_list = response['sn_list']
