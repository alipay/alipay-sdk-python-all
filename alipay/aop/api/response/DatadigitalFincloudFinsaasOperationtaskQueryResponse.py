#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasOperationtaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasOperationtaskQueryResponse, self).__init__()
        self._comment = None
        self._config = None
        self._crowd_id = None
        self._operation_task_id = None
        self._operation_task_name = None
        self._operation_task_type = None
        self._plan_end_time = None
        self._plan_start_time = None
        self._reject_comment = None
        self._status = None
        self._status_name = None
        self._update_time = None
        self._user_id = None
        self._user_name = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def operation_task_id(self):
        return self._operation_task_id

    @operation_task_id.setter
    def operation_task_id(self, value):
        self._operation_task_id = value
    @property
    def operation_task_name(self):
        return self._operation_task_name

    @operation_task_name.setter
    def operation_task_name(self, value):
        self._operation_task_name = value
    @property
    def operation_task_type(self):
        return self._operation_task_type

    @operation_task_type.setter
    def operation_task_type(self, value):
        self._operation_task_type = value
    @property
    def plan_end_time(self):
        return self._plan_end_time

    @plan_end_time.setter
    def plan_end_time(self, value):
        self._plan_end_time = value
    @property
    def plan_start_time(self):
        return self._plan_start_time

    @plan_start_time.setter
    def plan_start_time(self, value):
        self._plan_start_time = value
    @property
    def reject_comment(self):
        return self._reject_comment

    @reject_comment.setter
    def reject_comment(self, value):
        self._reject_comment = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, value):
        self._status_name = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasOperationtaskQueryResponse, self).parse_response_content(response_content)
        if 'comment' in response:
            self.comment = response['comment']
        if 'config' in response:
            self.config = response['config']
        if 'crowd_id' in response:
            self.crowd_id = response['crowd_id']
        if 'operation_task_id' in response:
            self.operation_task_id = response['operation_task_id']
        if 'operation_task_name' in response:
            self.operation_task_name = response['operation_task_name']
        if 'operation_task_type' in response:
            self.operation_task_type = response['operation_task_type']
        if 'plan_end_time' in response:
            self.plan_end_time = response['plan_end_time']
        if 'plan_start_time' in response:
            self.plan_start_time = response['plan_start_time']
        if 'reject_comment' in response:
            self.reject_comment = response['reject_comment']
        if 'status' in response:
            self.status = response['status']
        if 'status_name' in response:
            self.status_name = response['status_name']
        if 'update_time' in response:
            self.update_time = response['update_time']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
