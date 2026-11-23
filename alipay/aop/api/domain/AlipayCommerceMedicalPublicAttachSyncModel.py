#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPublicAttachSyncModel(object):

    def __init__(self):
        self._file_path_list = None

    @property
    def file_path_list(self):
        return self._file_path_list

    @file_path_list.setter
    def file_path_list(self, value):
        if isinstance(value, list):
            self._file_path_list = list()
            for i in value:
                self._file_path_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.file_path_list:
            if isinstance(self.file_path_list, list):
                for i in range(0, len(self.file_path_list)):
                    element = self.file_path_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_path_list[i] = element.to_alipay_dict()
            if hasattr(self.file_path_list, 'to_alipay_dict'):
                params['file_path_list'] = self.file_path_list.to_alipay_dict()
            else:
                params['file_path_list'] = self.file_path_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPublicAttachSyncModel()
        if 'file_path_list' in d:
            o.file_path_list = d['file_path_list']
        return o


