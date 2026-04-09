#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalDoctoravatarinfoCopyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctoravatarinfoCopyResponse, self).__init__()
        self._pic_sync_task_id = None

    @property
    def pic_sync_task_id(self):
        return self._pic_sync_task_id

    @pic_sync_task_id.setter
    def pic_sync_task_id(self, value):
        self._pic_sync_task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctoravatarinfoCopyResponse, self).parse_response_content(response_content)
        if 'pic_sync_task_id' in response:
            self.pic_sync_task_id = response['pic_sync_task_id']
