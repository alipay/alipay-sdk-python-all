#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaoKeTaskTemplateInfoDTO import TaoKeTaskTemplateInfoDTO


class AlipayCommerceCommonTasktemplateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTasktemplateBatchqueryResponse, self).__init__()
        self._task_list = None
        self._total_num = None

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
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTasktemplateBatchqueryResponse, self).parse_response_content(response_content)
        if 'task_list' in response:
            self.task_list = response['task_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
