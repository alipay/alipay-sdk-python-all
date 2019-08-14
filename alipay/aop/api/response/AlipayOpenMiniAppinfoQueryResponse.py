#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppBasicInfoResponse import AppBasicInfoResponse


class AlipayOpenMiniAppinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAppinfoQueryResponse, self).__init__()
        self._app_basic_info_response_list = None

    @property
    def app_basic_info_response_list(self):
        return self._app_basic_info_response_list

    @app_basic_info_response_list.setter
    def app_basic_info_response_list(self, value):
        if isinstance(value, list):
            self._app_basic_info_response_list = list()
            for i in value:
                if isinstance(i, AppBasicInfoResponse):
                    self._app_basic_info_response_list.append(i)
                else:
                    self._app_basic_info_response_list.append(AppBasicInfoResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAppinfoQueryResponse, self).parse_response_content(response_content)
        if 'app_basic_info_response_list' in response:
            self.app_basic_info_response_list = response['app_basic_info_response_list']
