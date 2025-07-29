#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundExpandindirectCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundExpandindirectCreateResponse, self).__init__()
        self._create_time = None
        self._order_id = None
        self._out_biz_no = None
        self._status = None
        self._task_finish_time = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_finish_time(self):
        return self._task_finish_time

    @task_finish_time.setter
    def task_finish_time(self, value):
        self._task_finish_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundExpandindirectCreateResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
        if 'task_finish_time' in response:
            self.task_finish_time = response['task_finish_time']
