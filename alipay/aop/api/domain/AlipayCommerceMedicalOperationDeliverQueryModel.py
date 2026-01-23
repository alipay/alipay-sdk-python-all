#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalOperationDeliverQueryModel(object):

    def __init__(self):
        self._account = None
        self._account_type = None
        self._channel_code = None
        self._parameter_info = None
        self._query_str = None
        self._scene_code = None
        self._template_code = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def parameter_info(self):
        return self._parameter_info

    @parameter_info.setter
    def parameter_info(self, value):
        self._parameter_info = value
    @property
    def query_str(self):
        return self._query_str

    @query_str.setter
    def query_str(self, value):
        self._query_str = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.parameter_info:
            if hasattr(self.parameter_info, 'to_alipay_dict'):
                params['parameter_info'] = self.parameter_info.to_alipay_dict()
            else:
                params['parameter_info'] = self.parameter_info
        if self.query_str:
            if hasattr(self.query_str, 'to_alipay_dict'):
                params['query_str'] = self.query_str.to_alipay_dict()
            else:
                params['query_str'] = self.query_str
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOperationDeliverQueryModel()
        if 'account' in d:
            o.account = d['account']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'parameter_info' in d:
            o.parameter_info = d['parameter_info']
        if 'query_str' in d:
            o.query_str = d['query_str']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


