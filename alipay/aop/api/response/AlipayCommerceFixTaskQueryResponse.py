#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FixCooperationDTO import FixCooperationDTO
from alipay.aop.api.domain.FixExtData import FixExtData
from alipay.aop.api.domain.FixFileInfo import FixFileInfo
from alipay.aop.api.domain.FixProblemDTO import FixProblemDTO
from alipay.aop.api.domain.FixProblemDTO import FixProblemDTO


class AlipayCommerceFixTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceFixTaskQueryResponse, self).__init__()
        self._biz_type = None
        self._close_time = None
        self._conclusion_ext_info = None
        self._conclusion_memo = None
        self._conclusion_type = None
        self._cooperations = None
        self._current_cooperation_id = None
        self._duty_owner_name = None
        self._duty_owner_phone = None
        self._extra_info = None
        self._files = None
        self._first_apply_time = None
        self._gmt_create = None
        self._is_resolved = None
        self._original_problem = None
        self._owner_name = None
        self._problem = None
        self._rule_scene = None
        self._start_confirm_time = None
        self._status = None
        self._status_name = None
        self._task_category = None
        self._task_type = None
        self._unresolved_reason = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def conclusion_ext_info(self):
        return self._conclusion_ext_info

    @conclusion_ext_info.setter
    def conclusion_ext_info(self, value):
        self._conclusion_ext_info = value
    @property
    def conclusion_memo(self):
        return self._conclusion_memo

    @conclusion_memo.setter
    def conclusion_memo(self, value):
        self._conclusion_memo = value
    @property
    def conclusion_type(self):
        return self._conclusion_type

    @conclusion_type.setter
    def conclusion_type(self, value):
        self._conclusion_type = value
    @property
    def cooperations(self):
        return self._cooperations

    @cooperations.setter
    def cooperations(self, value):
        if isinstance(value, list):
            self._cooperations = list()
            for i in value:
                if isinstance(i, FixCooperationDTO):
                    self._cooperations.append(i)
                else:
                    self._cooperations.append(FixCooperationDTO.from_alipay_dict(i))
    @property
    def current_cooperation_id(self):
        return self._current_cooperation_id

    @current_cooperation_id.setter
    def current_cooperation_id(self, value):
        self._current_cooperation_id = value
    @property
    def duty_owner_name(self):
        return self._duty_owner_name

    @duty_owner_name.setter
    def duty_owner_name(self, value):
        self._duty_owner_name = value
    @property
    def duty_owner_phone(self):
        return self._duty_owner_phone

    @duty_owner_phone.setter
    def duty_owner_phone(self, value):
        self._duty_owner_phone = value
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        if isinstance(value, list):
            self._extra_info = list()
            for i in value:
                if isinstance(i, FixExtData):
                    self._extra_info.append(i)
                else:
                    self._extra_info.append(FixExtData.from_alipay_dict(i))
    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        if isinstance(value, list):
            self._files = list()
            for i in value:
                if isinstance(i, FixFileInfo):
                    self._files.append(i)
                else:
                    self._files.append(FixFileInfo.from_alipay_dict(i))
    @property
    def first_apply_time(self):
        return self._first_apply_time

    @first_apply_time.setter
    def first_apply_time(self, value):
        self._first_apply_time = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def is_resolved(self):
        return self._is_resolved

    @is_resolved.setter
    def is_resolved(self, value):
        self._is_resolved = value
    @property
    def original_problem(self):
        return self._original_problem

    @original_problem.setter
    def original_problem(self, value):
        if isinstance(value, FixProblemDTO):
            self._original_problem = value
        else:
            self._original_problem = FixProblemDTO.from_alipay_dict(value)
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def problem(self):
        return self._problem

    @problem.setter
    def problem(self, value):
        if isinstance(value, FixProblemDTO):
            self._problem = value
        else:
            self._problem = FixProblemDTO.from_alipay_dict(value)
    @property
    def rule_scene(self):
        return self._rule_scene

    @rule_scene.setter
    def rule_scene(self, value):
        self._rule_scene = value
    @property
    def start_confirm_time(self):
        return self._start_confirm_time

    @start_confirm_time.setter
    def start_confirm_time(self, value):
        self._start_confirm_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, value):
        self._status_name = value
    @property
    def task_category(self):
        return self._task_category

    @task_category.setter
    def task_category(self, value):
        self._task_category = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def unresolved_reason(self):
        return self._unresolved_reason

    @unresolved_reason.setter
    def unresolved_reason(self, value):
        self._unresolved_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceFixTaskQueryResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'close_time' in response:
            self.close_time = response['close_time']
        if 'conclusion_ext_info' in response:
            self.conclusion_ext_info = response['conclusion_ext_info']
        if 'conclusion_memo' in response:
            self.conclusion_memo = response['conclusion_memo']
        if 'conclusion_type' in response:
            self.conclusion_type = response['conclusion_type']
        if 'cooperations' in response:
            self.cooperations = response['cooperations']
        if 'current_cooperation_id' in response:
            self.current_cooperation_id = response['current_cooperation_id']
        if 'duty_owner_name' in response:
            self.duty_owner_name = response['duty_owner_name']
        if 'duty_owner_phone' in response:
            self.duty_owner_phone = response['duty_owner_phone']
        if 'extra_info' in response:
            self.extra_info = response['extra_info']
        if 'files' in response:
            self.files = response['files']
        if 'first_apply_time' in response:
            self.first_apply_time = response['first_apply_time']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'is_resolved' in response:
            self.is_resolved = response['is_resolved']
        if 'original_problem' in response:
            self.original_problem = response['original_problem']
        if 'owner_name' in response:
            self.owner_name = response['owner_name']
        if 'problem' in response:
            self.problem = response['problem']
        if 'rule_scene' in response:
            self.rule_scene = response['rule_scene']
        if 'start_confirm_time' in response:
            self.start_confirm_time = response['start_confirm_time']
        if 'status' in response:
            self.status = response['status']
        if 'status_name' in response:
            self.status_name = response['status_name']
        if 'task_category' in response:
            self.task_category = response['task_category']
        if 'task_type' in response:
            self.task_type = response['task_type']
        if 'unresolved_reason' in response:
            self.unresolved_reason = response['unresolved_reason']
