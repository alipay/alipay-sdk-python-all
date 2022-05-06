#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperationTaskDTO import OperationTaskDTO


class DatadigitalFincloudFinsaasOperationtaskBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasOperationtaskBatchqueryResponse, self).__init__()
        self._operation_tasks = None
        self._total = None

    @property
    def operation_tasks(self):
        return self._operation_tasks

    @operation_tasks.setter
    def operation_tasks(self, value):
        if isinstance(value, list):
            self._operation_tasks = list()
            for i in value:
                if isinstance(i, OperationTaskDTO):
                    self._operation_tasks.append(i)
                else:
                    self._operation_tasks.append(OperationTaskDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasOperationtaskBatchqueryResponse, self).parse_response_content(response_content)
        if 'operation_tasks' in response:
            self.operation_tasks = response['operation_tasks']
        if 'total' in response:
            self.total = response['total']
