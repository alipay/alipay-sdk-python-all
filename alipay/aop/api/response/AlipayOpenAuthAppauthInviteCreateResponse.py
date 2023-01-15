#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthAppauthInviteCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthAppauthInviteCreateResponse, self).__init__()
        self._task_page_url = None

    @property
    def task_page_url(self):
        return self._task_page_url

    @task_page_url.setter
    def task_page_url(self, value):
        self._task_page_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthAppauthInviteCreateResponse, self).parse_response_content(response_content)
        if 'task_page_url' in response:
            self.task_page_url = response['task_page_url']
