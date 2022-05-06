#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseTestplatformTaskSyncModel(object):

    def __init__(self):
        self._branch = None
        self._commit_id = None
        self._fail_msg = None
        self._result_type = None
        self._task_id = None
        self._task_status = None
        self._test_case_result = None
        self._test_info = None

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, value):
        self._branch = value
    @property
    def commit_id(self):
        return self._commit_id

    @commit_id.setter
    def commit_id(self, value):
        self._commit_id = value
    @property
    def fail_msg(self):
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, value):
        self._fail_msg = value
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def test_case_result(self):
        return self._test_case_result

    @test_case_result.setter
    def test_case_result(self, value):
        self._test_case_result = value
    @property
    def test_info(self):
        return self._test_info

    @test_info.setter
    def test_info(self, value):
        self._test_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.branch:
            if hasattr(self.branch, 'to_alipay_dict'):
                params['branch'] = self.branch.to_alipay_dict()
            else:
                params['branch'] = self.branch
        if self.commit_id:
            if hasattr(self.commit_id, 'to_alipay_dict'):
                params['commit_id'] = self.commit_id.to_alipay_dict()
            else:
                params['commit_id'] = self.commit_id
        if self.fail_msg:
            if hasattr(self.fail_msg, 'to_alipay_dict'):
                params['fail_msg'] = self.fail_msg.to_alipay_dict()
            else:
                params['fail_msg'] = self.fail_msg
        if self.result_type:
            if hasattr(self.result_type, 'to_alipay_dict'):
                params['result_type'] = self.result_type.to_alipay_dict()
            else:
                params['result_type'] = self.result_type
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_status:
            if hasattr(self.task_status, 'to_alipay_dict'):
                params['task_status'] = self.task_status.to_alipay_dict()
            else:
                params['task_status'] = self.task_status
        if self.test_case_result:
            if hasattr(self.test_case_result, 'to_alipay_dict'):
                params['test_case_result'] = self.test_case_result.to_alipay_dict()
            else:
                params['test_case_result'] = self.test_case_result
        if self.test_info:
            if hasattr(self.test_info, 'to_alipay_dict'):
                params['test_info'] = self.test_info.to_alipay_dict()
            else:
                params['test_info'] = self.test_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseTestplatformTaskSyncModel()
        if 'branch' in d:
            o.branch = d['branch']
        if 'commit_id' in d:
            o.commit_id = d['commit_id']
        if 'fail_msg' in d:
            o.fail_msg = d['fail_msg']
        if 'result_type' in d:
            o.result_type = d['result_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_status' in d:
            o.task_status = d['task_status']
        if 'test_case_result' in d:
            o.test_case_result = d['test_case_result']
        if 'test_info' in d:
            o.test_info = d['test_info']
        return o


