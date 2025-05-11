#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CardApplyTaskInfo import CardApplyTaskInfo


class AlipayCommercePropertyAcardTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyAcardTaskQueryResponse, self).__init__()
        self._card_apply_task_detail = None
        self._out_biz_id = None
        self._status = None
        self._task_id = None

    @property
    def card_apply_task_detail(self):
        return self._card_apply_task_detail

    @card_apply_task_detail.setter
    def card_apply_task_detail(self, value):
        if isinstance(value, CardApplyTaskInfo):
            self._card_apply_task_detail = value
        else:
            self._card_apply_task_detail = CardApplyTaskInfo.from_alipay_dict(value)
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyAcardTaskQueryResponse, self).parse_response_content(response_content)
        if 'card_apply_task_detail' in response:
            self.card_apply_task_detail = response['card_apply_task_detail']
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
        if 'status' in response:
            self.status = response['status']
        if 'task_id' in response:
            self.task_id = response['task_id']
