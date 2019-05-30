#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppBaseInfoQueryResponse import MiniAppBaseInfoQueryResponse


class AlipayOpenMiniInnerbaseinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoBatchqueryResponse, self).__init__()
        self._base_info_list = None

    @property
    def base_info_list(self):
        return self._base_info_list

    @base_info_list.setter
    def base_info_list(self, value):
        if isinstance(value, list):
            self._base_info_list = list()
            for i in value:
                if isinstance(i, MiniAppBaseInfoQueryResponse):
                    self._base_info_list.append(i)
                else:
                    self._base_info_list.append(MiniAppBaseInfoQueryResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerbaseinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'base_info_list' in response:
            self.base_info_list = response['base_info_list']
