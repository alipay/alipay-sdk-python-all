#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntSignFileResult import AntSignFileResult
from alipay.aop.api.domain.AntSignOperatorResult import AntSignOperatorResult


class AntSignTaskResult(object):

    def __init__(self):
        self._ant_sign_file_result_list = None
        self._ant_sign_operator_result_list = None
        self._sign_task_id = None
        self._sign_task_status = None
        self._sub_biz_no = None

    @property
    def ant_sign_file_result_list(self):
        return self._ant_sign_file_result_list

    @ant_sign_file_result_list.setter
    def ant_sign_file_result_list(self, value):
        if isinstance(value, list):
            self._ant_sign_file_result_list = list()
            for i in value:
                if isinstance(i, AntSignFileResult):
                    self._ant_sign_file_result_list.append(i)
                else:
                    self._ant_sign_file_result_list.append(AntSignFileResult.from_alipay_dict(i))
    @property
    def ant_sign_operator_result_list(self):
        return self._ant_sign_operator_result_list

    @ant_sign_operator_result_list.setter
    def ant_sign_operator_result_list(self, value):
        if isinstance(value, list):
            self._ant_sign_operator_result_list = list()
            for i in value:
                if isinstance(i, AntSignOperatorResult):
                    self._ant_sign_operator_result_list.append(i)
                else:
                    self._ant_sign_operator_result_list.append(AntSignOperatorResult.from_alipay_dict(i))
    @property
    def sign_task_id(self):
        return self._sign_task_id

    @sign_task_id.setter
    def sign_task_id(self, value):
        self._sign_task_id = value
    @property
    def sign_task_status(self):
        return self._sign_task_status

    @sign_task_status.setter
    def sign_task_status(self, value):
        self._sign_task_status = value
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_sign_file_result_list:
            if isinstance(self.ant_sign_file_result_list, list):
                for i in range(0, len(self.ant_sign_file_result_list)):
                    element = self.ant_sign_file_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_file_result_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_file_result_list, 'to_alipay_dict'):
                params['ant_sign_file_result_list'] = self.ant_sign_file_result_list.to_alipay_dict()
            else:
                params['ant_sign_file_result_list'] = self.ant_sign_file_result_list
        if self.ant_sign_operator_result_list:
            if isinstance(self.ant_sign_operator_result_list, list):
                for i in range(0, len(self.ant_sign_operator_result_list)):
                    element = self.ant_sign_operator_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ant_sign_operator_result_list[i] = element.to_alipay_dict()
            if hasattr(self.ant_sign_operator_result_list, 'to_alipay_dict'):
                params['ant_sign_operator_result_list'] = self.ant_sign_operator_result_list.to_alipay_dict()
            else:
                params['ant_sign_operator_result_list'] = self.ant_sign_operator_result_list
        if self.sign_task_id:
            if hasattr(self.sign_task_id, 'to_alipay_dict'):
                params['sign_task_id'] = self.sign_task_id.to_alipay_dict()
            else:
                params['sign_task_id'] = self.sign_task_id
        if self.sign_task_status:
            if hasattr(self.sign_task_status, 'to_alipay_dict'):
                params['sign_task_status'] = self.sign_task_status.to_alipay_dict()
            else:
                params['sign_task_status'] = self.sign_task_status
        if self.sub_biz_no:
            if hasattr(self.sub_biz_no, 'to_alipay_dict'):
                params['sub_biz_no'] = self.sub_biz_no.to_alipay_dict()
            else:
                params['sub_biz_no'] = self.sub_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignTaskResult()
        if 'ant_sign_file_result_list' in d:
            o.ant_sign_file_result_list = d['ant_sign_file_result_list']
        if 'ant_sign_operator_result_list' in d:
            o.ant_sign_operator_result_list = d['ant_sign_operator_result_list']
        if 'sign_task_id' in d:
            o.sign_task_id = d['sign_task_id']
        if 'sign_task_status' in d:
            o.sign_task_status = d['sign_task_status']
        if 'sub_biz_no' in d:
            o.sub_biz_no = d['sub_biz_no']
        return o


