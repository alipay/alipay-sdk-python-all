#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppVersionInfo import MiniAppVersionInfo


class AlipayOpenMiniInnerversionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionBatchqueryResponse, self).__init__()
        self._version_info_list = None

    @property
    def version_info_list(self):
        return self._version_info_list

    @version_info_list.setter
    def version_info_list(self, value):
        if isinstance(value, list):
            self._version_info_list = list()
            for i in value:
                if isinstance(i, MiniAppVersionInfo):
                    self._version_info_list.append(i)
                else:
                    self._version_info_list.append(MiniAppVersionInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionBatchqueryResponse, self).parse_response_content(response_content)
        if 'version_info_list' in response:
            self.version_info_list = response['version_info_list']
