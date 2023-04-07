#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppOpenidApplyorderUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenidApplyorderUploadResponse, self).__init__()
        self._illegal_user_id_list = None

    @property
    def illegal_user_id_list(self):
        return self._illegal_user_id_list

    @illegal_user_id_list.setter
    def illegal_user_id_list(self, value):
        if isinstance(value, list):
            self._illegal_user_id_list = list()
            for i in value:
                self._illegal_user_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenidApplyorderUploadResponse, self).parse_response_content(response_content)
        if 'illegal_user_id_list' in response:
            self.illegal_user_id_list = response['illegal_user_id_list']
