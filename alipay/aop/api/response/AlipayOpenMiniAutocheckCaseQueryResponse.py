#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UseCaseStepInfo import UseCaseStepInfo


class AlipayOpenMiniAutocheckCaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAutocheckCaseQueryResponse, self).__init__()
        self._biz_line_name = None
        self._case_type = None
        self._creator = None
        self._desc = None
        self._id = None
        self._labels = None
        self._mini_app_id = None
        self._mini_app_version = None
        self._step_info_list = None
        self._timeout = None
        self._use_case_name = None
        self._use_case_type = None

    @property
    def biz_line_name(self):
        return self._biz_line_name

    @biz_line_name.setter
    def biz_line_name(self, value):
        self._biz_line_name = value
    @property
    def case_type(self):
        return self._case_type

    @case_type.setter
    def case_type(self, value):
        self._case_type = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        if isinstance(value, list):
            self._labels = list()
            for i in value:
                self._labels.append(i)
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_version(self):
        return self._mini_app_version

    @mini_app_version.setter
    def mini_app_version(self, value):
        self._mini_app_version = value
    @property
    def step_info_list(self):
        return self._step_info_list

    @step_info_list.setter
    def step_info_list(self, value):
        if isinstance(value, UseCaseStepInfo):
            self._step_info_list = value
        else:
            self._step_info_list = UseCaseStepInfo.from_alipay_dict(value)
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
    @property
    def use_case_name(self):
        return self._use_case_name

    @use_case_name.setter
    def use_case_name(self, value):
        self._use_case_name = value
    @property
    def use_case_type(self):
        return self._use_case_type

    @use_case_type.setter
    def use_case_type(self, value):
        self._use_case_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAutocheckCaseQueryResponse, self).parse_response_content(response_content)
        if 'biz_line_name' in response:
            self.biz_line_name = response['biz_line_name']
        if 'case_type' in response:
            self.case_type = response['case_type']
        if 'creator' in response:
            self.creator = response['creator']
        if 'desc' in response:
            self.desc = response['desc']
        if 'id' in response:
            self.id = response['id']
        if 'labels' in response:
            self.labels = response['labels']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'mini_app_version' in response:
            self.mini_app_version = response['mini_app_version']
        if 'step_info_list' in response:
            self.step_info_list = response['step_info_list']
        if 'timeout' in response:
            self.timeout = response['timeout']
        if 'use_case_name' in response:
            self.use_case_name = response['use_case_name']
        if 'use_case_type' in response:
            self.use_case_type = response['use_case_type']
