#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaoKeTaskTemplateInfoDTO import TaoKeTaskTemplateInfoDTO


class AlipayCommerceCommonTasktemplateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTasktemplateBatchqueryResponse, self).__init__()
        self._task_list = None

    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, TaoKeTaskTemplateInfoDTO):
                    self._task_list.append(i)
                else:
                    self._task_list.append(TaoKeTaskTemplateInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTasktemplateBatchqueryResponse, self).parse_response_content(response_content)
        if 'task_list' in response:
            self.task_list = response['task_list']
