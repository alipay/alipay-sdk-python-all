#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdUserbalanceOnlineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdUserbalanceOnlineResponse, self).__init__()
        self._success_user_id_list = None

    @property
    def success_user_id_list(self):
        return self._success_user_id_list

    @success_user_id_list.setter
    def success_user_id_list(self, value):
        if isinstance(value, list):
            self._success_user_id_list = list()
            for i in value:
                self._success_user_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdUserbalanceOnlineResponse, self).parse_response_content(response_content)
        if 'success_user_id_list' in response:
            self.success_user_id_list = response['success_user_id_list']
