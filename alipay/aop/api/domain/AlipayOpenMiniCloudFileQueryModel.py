#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniCloudFileQueryModel(object):

    def __init__(self):
        self._cloud_id = None
        self._file_id = None

    @property
    def cloud_id(self):
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, value):
        self._cloud_id = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_id:
            if hasattr(self.cloud_id, 'to_alipay_dict'):
                params['cloud_id'] = self.cloud_id.to_alipay_dict()
            else:
                params['cloud_id'] = self.cloud_id
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniCloudFileQueryModel()
        if 'cloud_id' in d:
            o.cloud_id = d['cloud_id']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


