#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMarketingPlanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMarketingPlanQueryResponse, self).__init__()
        self._biz_ids = None
        self._create_time = None
        self._end_time = None
        self._file_id = None
        self._modify_time = None
        self._plan_id = None
        self._plan_name = None
        self._priority = None
        self._space_code = None
        self._start_time = None
        self._status = None

    @property
    def biz_ids(self):
        return self._biz_ids

    @biz_ids.setter
    def biz_ids(self, value):
        if isinstance(value, list):
            self._biz_ids = list()
            for i in value:
                self._biz_ids.append(i)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def space_code(self):
        return self._space_code

    @space_code.setter
    def space_code(self, value):
        self._space_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMarketingPlanQueryResponse, self).parse_response_content(response_content)
        if 'biz_ids' in response:
            self.biz_ids = response['biz_ids']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'modify_time' in response:
            self.modify_time = response['modify_time']
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'priority' in response:
            self.priority = response['priority']
        if 'space_code' in response:
            self.space_code = response['space_code']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
