#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserTaskSimpleDto import UserTaskSimpleDto


class AlipayCommerceSportsTaskcenterFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsTaskcenterFinishResponse, self).__init__()
        self._user_task = None

    @property
    def user_task(self):
        return self._user_task

    @user_task.setter
    def user_task(self, value):
        if isinstance(value, UserTaskSimpleDto):
            self._user_task = value
        else:
            self._user_task = UserTaskSimpleDto.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsTaskcenterFinishResponse, self).parse_response_content(response_content)
        if 'user_task' in response:
            self.user_task = response['user_task']
