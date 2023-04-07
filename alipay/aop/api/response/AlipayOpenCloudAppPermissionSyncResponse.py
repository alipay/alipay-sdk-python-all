#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenCloudAppPermissionSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenCloudAppPermissionSyncResponse, self).__init__()
        self._permission_api_list = None

    @property
    def permission_api_list(self):
        return self._permission_api_list

    @permission_api_list.setter
    def permission_api_list(self, value):
        if isinstance(value, list):
            self._permission_api_list = list()
            for i in value:
                self._permission_api_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenCloudAppPermissionSyncResponse, self).parse_response_content(response_content)
        if 'permission_api_list' in response:
            self.permission_api_list = response['permission_api_list']
