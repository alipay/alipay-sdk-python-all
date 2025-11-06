#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Params import Params


class AlipayPayInstructOpencardTriggerModel(object):

    def __init__(self):
        self._bpaas_ipc_timeout = None
        self._operate_type = None
        self._page = None
        self._params = None
        self._pos_id = None

    @property
    def bpaas_ipc_timeout(self):
        return self._bpaas_ipc_timeout

    @bpaas_ipc_timeout.setter
    def bpaas_ipc_timeout(self, value):
        self._bpaas_ipc_timeout = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        if isinstance(value, Params):
            self._params = value
        else:
            self._params = Params.from_alipay_dict(value)
    @property
    def pos_id(self):
        return self._pos_id

    @pos_id.setter
    def pos_id(self, value):
        self._pos_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bpaas_ipc_timeout:
            if hasattr(self.bpaas_ipc_timeout, 'to_alipay_dict'):
                params['bpaas_ipc_timeout'] = self.bpaas_ipc_timeout.to_alipay_dict()
            else:
                params['bpaas_ipc_timeout'] = self.bpaas_ipc_timeout
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.pos_id:
            if hasattr(self.pos_id, 'to_alipay_dict'):
                params['pos_id'] = self.pos_id.to_alipay_dict()
            else:
                params['pos_id'] = self.pos_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayInstructOpencardTriggerModel()
        if 'bpaas_ipc_timeout' in d:
            o.bpaas_ipc_timeout = d['bpaas_ipc_timeout']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'page' in d:
            o.page = d['page']
        if 'params' in d:
            o.params = d['params']
        if 'pos_id' in d:
            o.pos_id = d['pos_id']
        return o


