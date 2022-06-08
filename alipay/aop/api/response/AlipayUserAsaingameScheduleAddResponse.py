#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiUserScheduleVO import OpenApiUserScheduleVO


class AlipayUserAsaingameScheduleAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAsaingameScheduleAddResponse, self).__init__()
        self._result_code = None
        self._result_msg = None
        self._success = None
        self._user_schedule = None

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def user_schedule(self):
        return self._user_schedule

    @user_schedule.setter
    def user_schedule(self, value):
        if isinstance(value, OpenApiUserScheduleVO):
            self._user_schedule = value
        else:
            self._user_schedule = OpenApiUserScheduleVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserAsaingameScheduleAddResponse, self).parse_response_content(response_content)
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'success' in response:
            self.success = response['success']
        if 'user_schedule' in response:
            self.user_schedule = response['user_schedule']
