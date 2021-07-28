#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoContractMessageSendModel(object):

    def __init__(self):
        self._batch_no = None
        self._cert_no = None
        self._cert_type = None
        self._flow_id = None
        self._isv_app_id = None
        self._msg_template_id = None
        self._sign_platform_code = None
        self._user_ids = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        if isinstance(value, list):
            self._cert_no = list()
            for i in value:
                self._cert_no.append(i)
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def msg_template_id(self):
        return self._msg_template_id

    @msg_template_id.setter
    def msg_template_id(self, value):
        self._msg_template_id = value
    @property
    def sign_platform_code(self):
        return self._sign_platform_code

    @sign_platform_code.setter
    def sign_platform_code(self, value):
        self._sign_platform_code = value
    @property
    def user_ids(self):
        return self._user_ids

    @user_ids.setter
    def user_ids(self, value):
        if isinstance(value, list):
            self._user_ids = list()
            for i in value:
                self._user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.cert_no:
            if isinstance(self.cert_no, list):
                for i in range(0, len(self.cert_no)):
                    element = self.cert_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cert_no[i] = element.to_alipay_dict()
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.msg_template_id:
            if hasattr(self.msg_template_id, 'to_alipay_dict'):
                params['msg_template_id'] = self.msg_template_id.to_alipay_dict()
            else:
                params['msg_template_id'] = self.msg_template_id
        if self.sign_platform_code:
            if hasattr(self.sign_platform_code, 'to_alipay_dict'):
                params['sign_platform_code'] = self.sign_platform_code.to_alipay_dict()
            else:
                params['sign_platform_code'] = self.sign_platform_code
        if self.user_ids:
            if isinstance(self.user_ids, list):
                for i in range(0, len(self.user_ids)):
                    element = self.user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_ids[i] = element.to_alipay_dict()
            if hasattr(self.user_ids, 'to_alipay_dict'):
                params['user_ids'] = self.user_ids.to_alipay_dict()
            else:
                params['user_ids'] = self.user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoContractMessageSendModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'msg_template_id' in d:
            o.msg_template_id = d['msg_template_id']
        if 'sign_platform_code' in d:
            o.sign_platform_code = d['sign_platform_code']
        if 'user_ids' in d:
            o.user_ids = d['user_ids']
        return o


