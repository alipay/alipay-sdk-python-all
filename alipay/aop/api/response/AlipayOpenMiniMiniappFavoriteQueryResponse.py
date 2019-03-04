#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniMiniappFavoriteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappFavoriteQueryResponse, self).__init__()
        self._favorite = None

    @property
    def favorite(self):
        return self._favorite

    @favorite.setter
    def favorite(self, value):
        self._favorite = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappFavoriteQueryResponse, self).parse_response_content(response_content)
        if 'favorite' in response:
            self.favorite = response['favorite']
