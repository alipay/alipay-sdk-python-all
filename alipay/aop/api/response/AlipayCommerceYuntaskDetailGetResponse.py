#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskTemplateInfoDTO import YunTaskTemplateInfoDTO


class AlipayCommerceYuntaskDetailGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskDetailGetResponse, self).__init__()
        self._task = None

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, value):
        if isinstance(value, YunTaskTemplateInfoDTO):
            self._task = value
        else:
            self._task = YunTaskTemplateInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskDetailGetResponse, self).parse_response_content(response_content)
        if 'task' in response:
            self.task = response['task']
