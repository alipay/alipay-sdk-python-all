#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCsfuCaseModifyModel(object):

    def __init__(self):
        self._data_id = None
        self._modified_info = None
        self._tenant_id = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def modified_info(self):
        return self._modified_info

    @modified_info.setter
    def modified_info(self, value):
        self._modified_info = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.modified_info:
            if hasattr(self.modified_info, 'to_alipay_dict'):
                params['modified_info'] = self.modified_info.to_alipay_dict()
            else:
                params['modified_info'] = self.modified_info
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCsfuCaseModifyModel()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'modified_info' in d:
            o.modified_info = d['modified_info']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


