#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHomedoctorFollowuptaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHomedoctorFollowuptaskQueryResponse, self).__init__()
        self._biz_id = None
        self._completed_time = None
        self._conversation_data_encrypted = None
        self._conversation_data_hash = None
        self._encryption_key_version = None
        self._form_data_encrypted = None
        self._form_data_hash = None
        self._task_id = None
        self._task_status = None
        self._template_id = None
        self._template_name = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def completed_time(self):
        return self._completed_time

    @completed_time.setter
    def completed_time(self, value):
        self._completed_time = value
    @property
    def conversation_data_encrypted(self):
        return self._conversation_data_encrypted

    @conversation_data_encrypted.setter
    def conversation_data_encrypted(self, value):
        self._conversation_data_encrypted = value
    @property
    def conversation_data_hash(self):
        return self._conversation_data_hash

    @conversation_data_hash.setter
    def conversation_data_hash(self, value):
        self._conversation_data_hash = value
    @property
    def encryption_key_version(self):
        return self._encryption_key_version

    @encryption_key_version.setter
    def encryption_key_version(self, value):
        self._encryption_key_version = value
    @property
    def form_data_encrypted(self):
        return self._form_data_encrypted

    @form_data_encrypted.setter
    def form_data_encrypted(self, value):
        self._form_data_encrypted = value
    @property
    def form_data_hash(self):
        return self._form_data_hash

    @form_data_hash.setter
    def form_data_hash(self, value):
        self._form_data_hash = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHomedoctorFollowuptaskQueryResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'completed_time' in response:
            self.completed_time = response['completed_time']
        if 'conversation_data_encrypted' in response:
            self.conversation_data_encrypted = response['conversation_data_encrypted']
        if 'conversation_data_hash' in response:
            self.conversation_data_hash = response['conversation_data_hash']
        if 'encryption_key_version' in response:
            self.encryption_key_version = response['encryption_key_version']
        if 'form_data_encrypted' in response:
            self.form_data_encrypted = response['form_data_encrypted']
        if 'form_data_hash' in response:
            self.form_data_hash = response['form_data_hash']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'task_status' in response:
            self.task_status = response['task_status']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'template_name' in response:
            self.template_name = response['template_name']
