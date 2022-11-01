#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OneStopCheckTaskDetailDTO import OneStopCheckTaskDetailDTO


class AlipayOpenMiniAutocheckTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAutocheckTaskQueryResponse, self).__init__()
        self._biz_status = None
        self._express_task_detail = None
        self._task_detail_vos = None
        self._task_id = None
        self._task_name = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def express_task_detail(self):
        return self._express_task_detail

    @express_task_detail.setter
    def express_task_detail(self, value):
        self._express_task_detail = value
    @property
    def task_detail_vos(self):
        return self._task_detail_vos

    @task_detail_vos.setter
    def task_detail_vos(self, value):
        if isinstance(value, list):
            self._task_detail_vos = list()
            for i in value:
                if isinstance(i, OneStopCheckTaskDetailDTO):
                    self._task_detail_vos.append(i)
                else:
                    self._task_detail_vos.append(OneStopCheckTaskDetailDTO.from_alipay_dict(i))
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAutocheckTaskQueryResponse, self).parse_response_content(response_content)
        if 'biz_status' in response:
            self.biz_status = response['biz_status']
        if 'express_task_detail' in response:
            self.express_task_detail = response['express_task_detail']
        if 'task_detail_vos' in response:
            self.task_detail_vos = response['task_detail_vos']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'task_name' in response:
            self.task_name = response['task_name']
