#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlegalchainMultipartyModifyModel(object):

    def __init__(self):
        self._bas_data_id = None
        self._biz_unique_id = None
        self._corp_code = None
        self._corp_name = None
        self._op_reason = None
        self._op_type = None
        self._request_app_name = None
        self._request_time_stamp = None
        self._request_token = None

    @property
    def bas_data_id(self):
        return self._bas_data_id

    @bas_data_id.setter
    def bas_data_id(self, value):
        self._bas_data_id = value
    @property
    def biz_unique_id(self):
        return self._biz_unique_id

    @biz_unique_id.setter
    def biz_unique_id(self, value):
        self._biz_unique_id = value
    @property
    def corp_code(self):
        return self._corp_code

    @corp_code.setter
    def corp_code(self, value):
        self._corp_code = value
    @property
    def corp_name(self):
        return self._corp_name

    @corp_name.setter
    def corp_name(self, value):
        self._corp_name = value
    @property
    def op_reason(self):
        return self._op_reason

    @op_reason.setter
    def op_reason(self, value):
        self._op_reason = value
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def request_app_name(self):
        return self._request_app_name

    @request_app_name.setter
    def request_app_name(self, value):
        self._request_app_name = value
    @property
    def request_time_stamp(self):
        return self._request_time_stamp

    @request_time_stamp.setter
    def request_time_stamp(self, value):
        self._request_time_stamp = value
    @property
    def request_token(self):
        return self._request_token

    @request_token.setter
    def request_token(self, value):
        self._request_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.bas_data_id:
            if hasattr(self.bas_data_id, 'to_alipay_dict'):
                params['bas_data_id'] = self.bas_data_id.to_alipay_dict()
            else:
                params['bas_data_id'] = self.bas_data_id
        if self.biz_unique_id:
            if hasattr(self.biz_unique_id, 'to_alipay_dict'):
                params['biz_unique_id'] = self.biz_unique_id.to_alipay_dict()
            else:
                params['biz_unique_id'] = self.biz_unique_id
        if self.corp_code:
            if hasattr(self.corp_code, 'to_alipay_dict'):
                params['corp_code'] = self.corp_code.to_alipay_dict()
            else:
                params['corp_code'] = self.corp_code
        if self.corp_name:
            if hasattr(self.corp_name, 'to_alipay_dict'):
                params['corp_name'] = self.corp_name.to_alipay_dict()
            else:
                params['corp_name'] = self.corp_name
        if self.op_reason:
            if hasattr(self.op_reason, 'to_alipay_dict'):
                params['op_reason'] = self.op_reason.to_alipay_dict()
            else:
                params['op_reason'] = self.op_reason
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.request_app_name:
            if hasattr(self.request_app_name, 'to_alipay_dict'):
                params['request_app_name'] = self.request_app_name.to_alipay_dict()
            else:
                params['request_app_name'] = self.request_app_name
        if self.request_time_stamp:
            if hasattr(self.request_time_stamp, 'to_alipay_dict'):
                params['request_time_stamp'] = self.request_time_stamp.to_alipay_dict()
            else:
                params['request_time_stamp'] = self.request_time_stamp
        if self.request_token:
            if hasattr(self.request_token, 'to_alipay_dict'):
                params['request_token'] = self.request_token.to_alipay_dict()
            else:
                params['request_token'] = self.request_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlegalchainMultipartyModifyModel()
        if 'bas_data_id' in d:
            o.bas_data_id = d['bas_data_id']
        if 'biz_unique_id' in d:
            o.biz_unique_id = d['biz_unique_id']
        if 'corp_code' in d:
            o.corp_code = d['corp_code']
        if 'corp_name' in d:
            o.corp_name = d['corp_name']
        if 'op_reason' in d:
            o.op_reason = d['op_reason']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'request_app_name' in d:
            o.request_app_name = d['request_app_name']
        if 'request_time_stamp' in d:
            o.request_time_stamp = d['request_time_stamp']
        if 'request_token' in d:
            o.request_token = d['request_token']
        return o


