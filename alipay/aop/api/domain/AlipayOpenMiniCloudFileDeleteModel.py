#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCloudFileDeleteModel(object):

    def __init__(self):
        self._cloud_id = None
        self._file_name_list = None
        self._path = None

    @property
    def cloud_id(self):
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, value):
        self._cloud_id = value
    @property
    def file_name_list(self):
        return self._file_name_list

    @file_name_list.setter
    def file_name_list(self, value):
        if isinstance(value, list):
            self._file_name_list = list()
            for i in value:
                self._file_name_list.append(i)
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_id:
            if hasattr(self.cloud_id, 'to_alipay_dict'):
                params['cloud_id'] = self.cloud_id.to_alipay_dict()
            else:
                params['cloud_id'] = self.cloud_id
        if self.file_name_list:
            if isinstance(self.file_name_list, list):
                for i in range(0, len(self.file_name_list)):
                    element = self.file_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_name_list[i] = element.to_alipay_dict()
            if hasattr(self.file_name_list, 'to_alipay_dict'):
                params['file_name_list'] = self.file_name_list.to_alipay_dict()
            else:
                params['file_name_list'] = self.file_name_list
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCloudFileDeleteModel()
        if 'cloud_id' in d:
            o.cloud_id = d['cloud_id']
        if 'file_name_list' in d:
            o.file_name_list = d['file_name_list']
        if 'path' in d:
            o.path = d['path']
        return o


