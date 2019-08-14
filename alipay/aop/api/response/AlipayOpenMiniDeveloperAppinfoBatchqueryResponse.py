#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppBaseInfoQueryResponse import MiniAppBaseInfoQueryResponse


class AlipayOpenMiniDeveloperAppinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniDeveloperAppinfoBatchqueryResponse, self).__init__()
        self._app_base_info_list = None

    @property
    def app_base_info_list(self):
        return self._app_base_info_list

    @app_base_info_list.setter
    def app_base_info_list(self, value):
        if isinstance(value, list):
            self._app_base_info_list = list()
            for i in value:
                if isinstance(i, MiniAppBaseInfoQueryResponse):
                    self._app_base_info_list.append(i)
                else:
                    self._app_base_info_list.append(MiniAppBaseInfoQueryResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniDeveloperAppinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'app_base_info_list' in response:
            self.app_base_info_list = response['app_base_info_list']
