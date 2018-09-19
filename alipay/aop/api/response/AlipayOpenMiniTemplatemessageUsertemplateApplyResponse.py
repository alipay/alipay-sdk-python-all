#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniTemplatemessageUsertemplateApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTemplatemessageUsertemplateApplyResponse, self).__init__()
        self._user_template_id = None

    @property
    def user_template_id(self):
        return self._user_template_id

    @user_template_id.setter
    def user_template_id(self, value):
        self._user_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTemplatemessageUsertemplateApplyResponse, self).parse_response_content(response_content)
        if 'user_template_id' in response:
            self.user_template_id = response['user_template_id']
