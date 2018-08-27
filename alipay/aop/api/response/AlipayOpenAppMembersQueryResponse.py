#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppMemberInfo import AppMemberInfo


class AlipayOpenAppMembersQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppMembersQueryResponse, self).__init__()
        self._app_member_info_list = None

    @property
    def app_member_info_list(self):
        return self._app_member_info_list

    @app_member_info_list.setter
    def app_member_info_list(self, value):
        if isinstance(value, list):
            self._app_member_info_list = list()
            for i in value:
                if isinstance(i, AppMemberInfo):
                    self._app_member_info_list.append(i)
                else:
                    self._app_member_info_list.append(AppMemberInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppMembersQueryResponse, self).parse_response_content(response_content)
        if 'app_member_info_list' in response:
            self.app_member_info_list = response['app_member_info_list']
