#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServiceaiOcrserviceUseModel(object):

    def __init__(self):
        self._afts_id = None
        self._file_ext = None
        self._out_pic_id = None
        self._out_pic_url = None
        self._owner_id = None
        self._pic_url = None
        self._retry_parsing_task = None
        self._source_system = None
        self._user_identity = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
    @property
    def file_ext(self):
        return self._file_ext

    @file_ext.setter
    def file_ext(self, value):
        self._file_ext = value
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
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
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
    def source_system(self):
        return self._source_system

    @source_system.setter
    def source_system(self, value):
        self._source_system = value
    @property
    def user_identity(self):
        return self._user_identity

    @user_identity.setter
    def user_identity(self, value):
        self._user_identity = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_id:
            if hasattr(self.afts_id, 'to_alipay_dict'):
                params['afts_id'] = self.afts_id.to_alipay_dict()
            else:
                params['afts_id'] = self.afts_id
        if self.file_ext:
            if hasattr(self.file_ext, 'to_alipay_dict'):
                params['file_ext'] = self.file_ext.to_alipay_dict()
            else:
                params['file_ext'] = self.file_ext
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
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
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
        if self.source_system:
            if hasattr(self.source_system, 'to_alipay_dict'):
                params['source_system'] = self.source_system.to_alipay_dict()
            else:
                params['source_system'] = self.source_system
        if self.user_identity:
            if hasattr(self.user_identity, 'to_alipay_dict'):
                params['user_identity'] = self.user_identity.to_alipay_dict()
            else:
                params['user_identity'] = self.user_identity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServiceaiOcrserviceUseModel()
        if 'afts_id' in d:
            o.afts_id = d['afts_id']
        if 'file_ext' in d:
            o.file_ext = d['file_ext']
        if 'out_pic_id' in d:
            o.out_pic_id = d['out_pic_id']
        if 'out_pic_url' in d:
            o.out_pic_url = d['out_pic_url']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'retry_parsing_task' in d:
            o.retry_parsing_task = d['retry_parsing_task']
        if 'source_system' in d:
            o.source_system = d['source_system']
        if 'user_identity' in d:
            o.user_identity = d['user_identity']
        return o


