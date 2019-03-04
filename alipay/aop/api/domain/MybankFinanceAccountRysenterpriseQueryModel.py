#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankFinanceAccountRysenterpriseQueryModel(object):

    def __init__(self):
        self._account_no = None
        self._ip_id = None
        self._ip_role_id = None
        self._out_channel_id = None
        self._out_channel_type = None
        self._scene_code = None
        self._tnt_inst_id = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_channel_id(self):
        return self._out_channel_id

    @out_channel_id.setter
    def out_channel_id(self, value):
        self._out_channel_id = value
    @property
    def out_channel_type(self):
        return self._out_channel_type

    @out_channel_type.setter
    def out_channel_type(self, value):
        self._out_channel_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.out_channel_id:
            if hasattr(self.out_channel_id, 'to_alipay_dict'):
                params['out_channel_id'] = self.out_channel_id.to_alipay_dict()
            else:
                params['out_channel_id'] = self.out_channel_id
        if self.out_channel_type:
            if hasattr(self.out_channel_type, 'to_alipay_dict'):
                params['out_channel_type'] = self.out_channel_type.to_alipay_dict()
            else:
                params['out_channel_type'] = self.out_channel_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankFinanceAccountRysenterpriseQueryModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'out_channel_id' in d:
            o.out_channel_id = d['out_channel_id']
        if 'out_channel_type' in d:
            o.out_channel_type = d['out_channel_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


