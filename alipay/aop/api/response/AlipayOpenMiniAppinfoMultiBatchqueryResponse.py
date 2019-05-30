#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiAppBaseInfoDto import MultiAppBaseInfoDto


class AlipayOpenMiniAppinfoMultiBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAppinfoMultiBatchqueryResponse, self).__init__()
        self._app_base_info_list = None

    @property
    def app_base_info_list(self):
        return self._app_base_info_list

    @app_base_info_list.setter
    def app_base_info_list(self, value):
        if isinstance(value, list):
            self._app_base_info_list = list()
            for i in value:
                if isinstance(i, MultiAppBaseInfoDto):
                    self._app_base_info_list.append(i)
                else:
                    self._app_base_info_list.append(MultiAppBaseInfoDto.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAppinfoMultiBatchqueryResponse, self).parse_response_content(response_content)
        if 'app_base_info_list' in response:
            self.app_base_info_list = response['app_base_info_list']
