#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniMiniappFavoriteAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappFavoriteAddResponse, self).__init__()
        self._add_result = None

    @property
    def add_result(self):
        return self._add_result

    @add_result.setter
    def add_result(self, value):
        self._add_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappFavoriteAddResponse, self).parse_response_content(response_content)
        if 'add_result' in response:
            self.add_result = response['add_result']
