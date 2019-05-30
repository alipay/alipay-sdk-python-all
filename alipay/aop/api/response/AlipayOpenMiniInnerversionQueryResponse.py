#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppVersionBaseInfo import MiniAppVersionBaseInfo


class AlipayOpenMiniInnerversionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionQueryResponse, self).__init__()
        self._total_count = None
        self._version_list = None

    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def version_list(self):
        return self._version_list

    @version_list.setter
    def version_list(self, value):
        if isinstance(value, list):
            self._version_list = list()
            for i in value:
                if isinstance(i, MiniAppVersionBaseInfo):
                    self._version_list.append(i)
                else:
                    self._version_list.append(MiniAppVersionBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionQueryResponse, self).parse_response_content(response_content)
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'version_list' in response:
            self.version_list = response['version_list']
