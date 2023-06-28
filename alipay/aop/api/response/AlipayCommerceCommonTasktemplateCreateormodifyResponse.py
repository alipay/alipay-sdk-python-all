#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCommonTasktemplateCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTasktemplateCreateormodifyResponse, self).__init__()
        self._task_template_id = None

    @property
    def task_template_id(self):
        return self._task_template_id

    @task_template_id.setter
    def task_template_id(self, value):
        self._task_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTasktemplateCreateormodifyResponse, self).parse_response_content(response_content)
        if 'task_template_id' in response:
            self.task_template_id = response['task_template_id']
