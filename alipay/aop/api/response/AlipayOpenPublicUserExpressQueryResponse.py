#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicUserExpressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicUserExpressQueryResponse, self).__init__()
        self._express_user = None
        self._user_id = None

    @property
    def express_user(self):
        return self._express_user

    @express_user.setter
    def express_user(self, value):
        self._express_user = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicUserExpressQueryResponse, self).parse_response_content(response_content)
        if 'express_user' in response:
            self.express_user = response['express_user']
        if 'user_id' in response:
            self.user_id = response['user_id']
