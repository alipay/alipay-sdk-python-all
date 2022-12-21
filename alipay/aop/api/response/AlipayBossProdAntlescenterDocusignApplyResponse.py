#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlescenterDocusignApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterDocusignApplyResponse, self).__init__()
        self._sign_task_request_id = None

    @property
    def sign_task_request_id(self):
        return self._sign_task_request_id

    @sign_task_request_id.setter
    def sign_task_request_id(self, value):
        self._sign_task_request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterDocusignApplyResponse, self).parse_response_content(response_content)
        if 'sign_task_request_id' in response:
            self.sign_task_request_id = response['sign_task_request_id']
