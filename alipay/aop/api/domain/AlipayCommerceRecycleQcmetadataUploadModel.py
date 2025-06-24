#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleQcMetadata import RecycleQcMetadata


class AlipayCommerceRecycleQcmetadataUploadModel(object):

    def __init__(self):
        self._file_id = None
        self._metadata_list = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def metadata_list(self):
        return self._metadata_list

    @metadata_list.setter
    def metadata_list(self, value):
        if isinstance(value, list):
            self._metadata_list = list()
            for i in value:
                if isinstance(i, RecycleQcMetadata):
                    self._metadata_list.append(i)
                else:
                    self._metadata_list.append(RecycleQcMetadata.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.metadata_list:
            if isinstance(self.metadata_list, list):
                for i in range(0, len(self.metadata_list)):
                    element = self.metadata_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.metadata_list[i] = element.to_alipay_dict()
            if hasattr(self.metadata_list, 'to_alipay_dict'):
                params['metadata_list'] = self.metadata_list.to_alipay_dict()
            else:
                params['metadata_list'] = self.metadata_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleQcmetadataUploadModel()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'metadata_list' in d:
            o.metadata_list = d['metadata_list']
        return o


