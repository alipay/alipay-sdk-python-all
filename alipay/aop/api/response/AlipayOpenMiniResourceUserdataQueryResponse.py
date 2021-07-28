#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResourceUserDataVO import ResourceUserDataVO


class AlipayOpenMiniResourceUserdataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniResourceUserdataQueryResponse, self).__init__()
        self._user_data_list = None

    @property
    def user_data_list(self):
        return self._user_data_list

    @user_data_list.setter
    def user_data_list(self, value):
        if isinstance(value, list):
            self._user_data_list = list()
            for i in value:
                if isinstance(i, ResourceUserDataVO):
                    self._user_data_list.append(i)
                else:
                    self._user_data_list.append(ResourceUserDataVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniResourceUserdataQueryResponse, self).parse_response_content(response_content)
        if 'user_data_list' in response:
            self.user_data_list = response['user_data_list']
