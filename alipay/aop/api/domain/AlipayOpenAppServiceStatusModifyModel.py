#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServiceStatusModifyModel(object):

    def __init__(self):
        self._action = None
        self._biz_id = None
        self._data_timestamp = None
        self._service_spec_code = None

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
    def data_timestamp(self):
        return self._data_timestamp

    @data_timestamp.setter
    def data_timestamp(self, value):
        self._data_timestamp = value
    @property
    def service_spec_code(self):
        return self._service_spec_code

    @service_spec_code.setter
    def service_spec_code(self, value):
        self._service_spec_code = value


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
        if self.data_timestamp:
            if hasattr(self.data_timestamp, 'to_alipay_dict'):
                params['data_timestamp'] = self.data_timestamp.to_alipay_dict()
            else:
                params['data_timestamp'] = self.data_timestamp
        if self.service_spec_code:
            if hasattr(self.service_spec_code, 'to_alipay_dict'):
                params['service_spec_code'] = self.service_spec_code.to_alipay_dict()
            else:
                params['service_spec_code'] = self.service_spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServiceStatusModifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'data_timestamp' in d:
            o.data_timestamp = d['data_timestamp']
        if 'service_spec_code' in d:
            o.service_spec_code = d['service_spec_code']
        return o


