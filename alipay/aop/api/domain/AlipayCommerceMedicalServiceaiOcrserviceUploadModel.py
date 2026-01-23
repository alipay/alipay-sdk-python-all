#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServiceaiOcrserviceUploadModel(object):

    def __init__(self):
        self._afts_id = None
        self._file_type = None
        self._out_pic_id = None
        self._out_pic_url = None
        self._pic_url = None
        self._retry_parsing_task = None
        self._system_type = None
        self._user_id = None
        self._user_type = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def out_pic_id(self):
        return self._out_pic_id

    @out_pic_id.setter
    def out_pic_id(self, value):
        self._out_pic_id = value
    @property
    def out_pic_url(self):
        return self._out_pic_url

    @out_pic_url.setter
    def out_pic_url(self, value):
        self._out_pic_url = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def retry_parsing_task(self):
        return self._retry_parsing_task

    @retry_parsing_task.setter
    def retry_parsing_task(self, value):
        self._retry_parsing_task = value
    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        self._system_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_id:
            if hasattr(self.afts_id, 'to_alipay_dict'):
                params['afts_id'] = self.afts_id.to_alipay_dict()
            else:
                params['afts_id'] = self.afts_id
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.out_pic_id:
            if hasattr(self.out_pic_id, 'to_alipay_dict'):
                params['out_pic_id'] = self.out_pic_id.to_alipay_dict()
            else:
                params['out_pic_id'] = self.out_pic_id
        if self.out_pic_url:
            if hasattr(self.out_pic_url, 'to_alipay_dict'):
                params['out_pic_url'] = self.out_pic_url.to_alipay_dict()
            else:
                params['out_pic_url'] = self.out_pic_url
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.retry_parsing_task:
            if hasattr(self.retry_parsing_task, 'to_alipay_dict'):
                params['retry_parsing_task'] = self.retry_parsing_task.to_alipay_dict()
            else:
                params['retry_parsing_task'] = self.retry_parsing_task
        if self.system_type:
            if hasattr(self.system_type, 'to_alipay_dict'):
                params['system_type'] = self.system_type.to_alipay_dict()
            else:
                params['system_type'] = self.system_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServiceaiOcrserviceUploadModel()
        if 'afts_id' in d:
            o.afts_id = d['afts_id']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'out_pic_id' in d:
            o.out_pic_id = d['out_pic_id']
        if 'out_pic_url' in d:
            o.out_pic_url = d['out_pic_url']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'retry_parsing_task' in d:
            o.retry_parsing_task = d['retry_parsing_task']
        if 'system_type' in d:
            o.system_type = d['system_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


