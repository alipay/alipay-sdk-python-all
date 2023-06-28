#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaoKeTaskTemplateInfoDTO import TaoKeTaskTemplateInfoDTO


class AlipayCommerceCommonTasktemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTasktemplateQueryResponse, self).__init__()
        self._task_template_info = None

    @property
    def task_template_info(self):
        return self._task_template_info

    @task_template_info.setter
    def task_template_info(self, value):
        if isinstance(value, TaoKeTaskTemplateInfoDTO):
            self._task_template_info = value
        else:
            self._task_template_info = TaoKeTaskTemplateInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTasktemplateQueryResponse, self).parse_response_content(response_content)
        if 'task_template_info' in response:
            self.task_template_info = response['task_template_info']
