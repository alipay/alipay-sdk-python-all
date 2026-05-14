#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserRegisterDiscountInfo import UserRegisterDiscountInfo
from alipay.aop.api.domain.UserTaskProgress import UserTaskProgress


class AlipayUserDtbankcustDailydiscountuserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustDailydiscountuserQueryResponse, self).__init__()
        self._activity_status = None
        self._user_register = None
        self._user_register_discount_info = None
        self._user_task_progress = None

    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def user_register(self):
        return self._user_register

    @user_register.setter
    def user_register(self, value):
        self._user_register = value
    @property
    def user_register_discount_info(self):
        return self._user_register_discount_info

    @user_register_discount_info.setter
    def user_register_discount_info(self, value):
        if isinstance(value, UserRegisterDiscountInfo):
            self._user_register_discount_info = value
        else:
            self._user_register_discount_info = UserRegisterDiscountInfo.from_alipay_dict(value)
    @property
    def user_task_progress(self):
        return self._user_task_progress

    @user_task_progress.setter
    def user_task_progress(self, value):
        if isinstance(value, list):
            self._user_task_progress = list()
            for i in value:
                if isinstance(i, UserTaskProgress):
                    self._user_task_progress.append(i)
                else:
                    self._user_task_progress.append(UserTaskProgress.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustDailydiscountuserQueryResponse, self).parse_response_content(response_content)
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'user_register' in response:
            self.user_register = response['user_register']
        if 'user_register_discount_info' in response:
            self.user_register_discount_info = response['user_register_discount_info']
        if 'user_task_progress' in response:
            self.user_task_progress = response['user_task_progress']
