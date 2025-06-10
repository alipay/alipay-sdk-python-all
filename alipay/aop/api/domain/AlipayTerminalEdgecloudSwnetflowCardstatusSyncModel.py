#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudSwnetflowCardstatusSyncModel(object):

    def __init__(self):
        self._after_os_status = None
        self._after_status = None
        self._before_os_status = None
        self._before_status = None
        self._biling_cycle = None
        self._credential_name = None
        self._data_type = None
        self._icc_id = None

    @property
    def after_os_status(self):
        return self._after_os_status

    @after_os_status.setter
    def after_os_status(self, value):
        self._after_os_status = value
    @property
    def after_status(self):
        return self._after_status

    @after_status.setter
    def after_status(self, value):
        self._after_status = value
    @property
    def before_os_status(self):
        return self._before_os_status

    @before_os_status.setter
    def before_os_status(self, value):
        self._before_os_status = value
    @property
    def before_status(self):
        return self._before_status

    @before_status.setter
    def before_status(self, value):
        self._before_status = value
    @property
    def biling_cycle(self):
        return self._biling_cycle

    @biling_cycle.setter
    def biling_cycle(self, value):
        self._biling_cycle = value
    @property
    def credential_name(self):
        return self._credential_name

    @credential_name.setter
    def credential_name(self, value):
        self._credential_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def icc_id(self):
        return self._icc_id

    @icc_id.setter
    def icc_id(self, value):
        self._icc_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_os_status:
            if hasattr(self.after_os_status, 'to_alipay_dict'):
                params['after_os_status'] = self.after_os_status.to_alipay_dict()
            else:
                params['after_os_status'] = self.after_os_status
        if self.after_status:
            if hasattr(self.after_status, 'to_alipay_dict'):
                params['after_status'] = self.after_status.to_alipay_dict()
            else:
                params['after_status'] = self.after_status
        if self.before_os_status:
            if hasattr(self.before_os_status, 'to_alipay_dict'):
                params['before_os_status'] = self.before_os_status.to_alipay_dict()
            else:
                params['before_os_status'] = self.before_os_status
        if self.before_status:
            if hasattr(self.before_status, 'to_alipay_dict'):
                params['before_status'] = self.before_status.to_alipay_dict()
            else:
                params['before_status'] = self.before_status
        if self.biling_cycle:
            if hasattr(self.biling_cycle, 'to_alipay_dict'):
                params['biling_cycle'] = self.biling_cycle.to_alipay_dict()
            else:
                params['biling_cycle'] = self.biling_cycle
        if self.credential_name:
            if hasattr(self.credential_name, 'to_alipay_dict'):
                params['credential_name'] = self.credential_name.to_alipay_dict()
            else:
                params['credential_name'] = self.credential_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.icc_id:
            if hasattr(self.icc_id, 'to_alipay_dict'):
                params['icc_id'] = self.icc_id.to_alipay_dict()
            else:
                params['icc_id'] = self.icc_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudSwnetflowCardstatusSyncModel()
        if 'after_os_status' in d:
            o.after_os_status = d['after_os_status']
        if 'after_status' in d:
            o.after_status = d['after_status']
        if 'before_os_status' in d:
            o.before_os_status = d['before_os_status']
        if 'before_status' in d:
            o.before_status = d['before_status']
        if 'biling_cycle' in d:
            o.biling_cycle = d['biling_cycle']
        if 'credential_name' in d:
            o.credential_name = d['credential_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'icc_id' in d:
            o.icc_id = d['icc_id']
        return o


