#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmLcsLcsserversSaveModel(object):

    def __init__(self):
        self._add_type = None
        self._ccs_instance_id = None
        self._server_ids = None

    @property
    def add_type(self):
        return self._add_type

    @add_type.setter
    def add_type(self, value):
        self._add_type = value
    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def server_ids(self):
        return self._server_ids

    @server_ids.setter
    def server_ids(self, value):
        if isinstance(value, list):
            self._server_ids = list()
            for i in value:
                self._server_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.add_type:
            if hasattr(self.add_type, 'to_alipay_dict'):
                params['add_type'] = self.add_type.to_alipay_dict()
            else:
                params['add_type'] = self.add_type
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.server_ids:
            if isinstance(self.server_ids, list):
                for i in range(0, len(self.server_ids)):
                    element = self.server_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.server_ids[i] = element.to_alipay_dict()
            if hasattr(self.server_ids, 'to_alipay_dict'):
                params['server_ids'] = self.server_ids.to_alipay_dict()
            else:
                params['server_ids'] = self.server_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmLcsLcsserversSaveModel()
        if 'add_type' in d:
            o.add_type = d['add_type']
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'server_ids' in d:
            o.server_ids = d['server_ids']
        return o


