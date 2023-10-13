#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlescenterDocusignmultiCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterDocusignmultiCreateResponse, self).__init__()
        self._sign_task_id = None

    @property
    def sign_task_id(self):
        return self._sign_task_id

    @sign_task_id.setter
    def sign_task_id(self, value):
        self._sign_task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterDocusignmultiCreateResponse, self).parse_response_content(response_content)
        if 'sign_task_id' in response:
            self.sign_task_id = response['sign_task_id']
