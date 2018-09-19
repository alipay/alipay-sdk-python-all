#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignedFileInfo import SignedFileInfo


class SignTaskFileResult(object):

    def __init__(self):
        self._biz_id = None
        self._biz_info = None
        self._signed_file_list = None
        self._status = None
        self._task_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def signed_file_list(self):
        return self._signed_file_list

    @signed_file_list.setter
    def signed_file_list(self, value):
        if isinstance(value, list):
            self._signed_file_list = list()
            for i in value:
                if isinstance(i, SignedFileInfo):
                    self._signed_file_list.append(i)
                else:
                    self._signed_file_list.append(SignedFileInfo.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.signed_file_list:
            if isinstance(self.signed_file_list, list):
                for i in range(0, len(self.signed_file_list)):
                    element = self.signed_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.signed_file_list[i] = element.to_alipay_dict()
            if hasattr(self.signed_file_list, 'to_alipay_dict'):
                params['signed_file_list'] = self.signed_file_list.to_alipay_dict()
            else:
                params['signed_file_list'] = self.signed_file_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignTaskFileResult()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'signed_file_list' in d:
            o.signed_file_list = d['signed_file_list']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


