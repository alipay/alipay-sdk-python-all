#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppRelationItemVo import MiniAppRelationItemVo


class AlipayOpenMiniInnerRelationconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerRelationconfigQueryResponse, self).__init__()
        self._unlimited = None
        self._white_list = None

    @property
    def unlimited(self):
        return self._unlimited

    @unlimited.setter
    def unlimited(self, value):
        self._unlimited = value
    @property
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        if isinstance(value, list):
            self._white_list = list()
            for i in value:
                if isinstance(i, MiniAppRelationItemVo):
                    self._white_list.append(i)
                else:
                    self._white_list.append(MiniAppRelationItemVo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerRelationconfigQueryResponse, self).parse_response_content(response_content)
        if 'unlimited' in response:
            self.unlimited = response['unlimited']
        if 'white_list' in response:
            self.white_list = response['white_list']
