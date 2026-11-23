#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetFileVO import AssetFileVO
from alipay.aop.api.domain.IngestIdentity import IngestIdentity


class AssetPushItem(object):

    def __init__(self):
        self._attachment_list = None
        self._identity = None
        self._source_data = None

    @property
    def attachment_list(self):
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, value):
        if isinstance(value, list):
            self._attachment_list = list()
            for i in value:
                if isinstance(i, AssetFileVO):
                    self._attachment_list.append(i)
                else:
                    self._attachment_list.append(AssetFileVO.from_alipay_dict(i))
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        if isinstance(value, IngestIdentity):
            self._identity = value
        else:
            self._identity = IngestIdentity.from_alipay_dict(value)
    @property
    def source_data(self):
        return self._source_data

    @source_data.setter
    def source_data(self, value):
        self._source_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_list:
            if isinstance(self.attachment_list, list):
                for i in range(0, len(self.attachment_list)):
                    element = self.attachment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_list[i] = element.to_alipay_dict()
            if hasattr(self.attachment_list, 'to_alipay_dict'):
                params['attachment_list'] = self.attachment_list.to_alipay_dict()
            else:
                params['attachment_list'] = self.attachment_list
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.source_data:
            if hasattr(self.source_data, 'to_alipay_dict'):
                params['source_data'] = self.source_data.to_alipay_dict()
            else:
                params['source_data'] = self.source_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetPushItem()
        if 'attachment_list' in d:
            o.attachment_list = d['attachment_list']
        if 'identity' in d:
            o.identity = d['identity']
        if 'source_data' in d:
            o.source_data = d['source_data']
        return o


