#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozIdentificationZolozidGetModel(object):

    def __init__(self):
        self._action = None
        self._biz_id = None
        self._extern_params = None
        self._zcif_params = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def extern_params(self):
        return self._extern_params

    @extern_params.setter
    def extern_params(self, value):
        self._extern_params = value
    @property
    def zcif_params(self):
        return self._zcif_params

    @zcif_params.setter
    def zcif_params(self, value):
        self._zcif_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.extern_params:
            if hasattr(self.extern_params, 'to_alipay_dict'):
                params['extern_params'] = self.extern_params.to_alipay_dict()
            else:
                params['extern_params'] = self.extern_params
        if self.zcif_params:
            if hasattr(self.zcif_params, 'to_alipay_dict'):
                params['zcif_params'] = self.zcif_params.to_alipay_dict()
            else:
                params['zcif_params'] = self.zcif_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozIdentificationZolozidGetModel()
        if 'action' in d:
            o.action = d['action']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'extern_params' in d:
            o.extern_params = d['extern_params']
        if 'zcif_params' in d:
            o.zcif_params = d['zcif_params']
        return o


