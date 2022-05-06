#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTaskProcessQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTaskProcessQueryResponse, self).__init__()
        self._alipay_user_id = None
        self._biz_id = None
        self._current = None
        self._target = None
        self._target_type = None
        self._task_id = None
        self._type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTaskProcessQueryResponse, self).parse_response_content(response_content)
        if 'alipay_user_id' in response:
            self.alipay_user_id = response['alipay_user_id']
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'current' in response:
            self.current = response['current']
        if 'target' in response:
            self.target = response['target']
        if 'target_type' in response:
            self.target_type = response['target_type']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'type' in response:
            self.type = response['type']
