#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceOpenapiallTransferModel(object):

    def __init__(self):
        self._action = None
        self._params = None
        self._tnt_inst_id = None
        self._ur_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def ur_id(self):
        return self._ur_id

    @ur_id.setter
    def ur_id(self, value):
        self._ur_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.ur_id:
            if hasattr(self.ur_id, 'to_alipay_dict'):
                params['ur_id'] = self.ur_id.to_alipay_dict()
            else:
                params['ur_id'] = self.ur_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceOpenapiallTransferModel()
        if 'action' in d:
            o.action = d['action']
        if 'params' in d:
            o.params = d['params']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'ur_id' in d:
            o.ur_id = d['ur_id']
        return o


