#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppBaseInfoQueryResponse import MiniAppBaseInfoQueryResponse


class AlipayOpenMiniInnerbaseinfoListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoListQueryResponse, self).__init__()
        self._mini_app_list = None
        self._total_count = None

    @property
    def mini_app_list(self):
        return self._mini_app_list

    @mini_app_list.setter
    def mini_app_list(self, value):
        if isinstance(value, MiniAppBaseInfoQueryResponse):
            self._mini_app_list = value
        else:
            self._mini_app_list = MiniAppBaseInfoQueryResponse.from_alipay_dict(value)
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerbaseinfoListQueryResponse, self).parse_response_content(response_content)
        if 'mini_app_list' in response:
            self.mini_app_list = response['mini_app_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
