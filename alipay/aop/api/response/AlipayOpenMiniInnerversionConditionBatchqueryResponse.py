#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniVersionBaseInfo import MiniVersionBaseInfo


class AlipayOpenMiniInnerversionConditionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionConditionBatchqueryResponse, self).__init__()
        self._mini_version_base_info_list = None

    @property
    def mini_version_base_info_list(self):
        return self._mini_version_base_info_list

    @mini_version_base_info_list.setter
    def mini_version_base_info_list(self, value):
        if isinstance(value, list):
            self._mini_version_base_info_list = list()
            for i in value:
                if isinstance(i, MiniVersionBaseInfo):
                    self._mini_version_base_info_list.append(i)
                else:
                    self._mini_version_base_info_list.append(MiniVersionBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionConditionBatchqueryResponse, self).parse_response_content(response_content)
        if 'mini_version_base_info_list' in response:
            self.mini_version_base_info_list = response['mini_version_base_info_list']
