#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProdParams(object):

    def __init__(self):
        self._auth_biz_params = None
        self._pay_operation_info = None
        self._pre_consult_id = None

    @property
    def auth_biz_params(self):
        return self._auth_biz_params

    @auth_biz_params.setter
    def auth_biz_params(self, value):
        self._auth_biz_params = value
    @property
    def pay_operation_info(self):
        return self._pay_operation_info

    @pay_operation_info.setter
    def pay_operation_info(self, value):
        self._pay_operation_info = value
    @property
    def pre_consult_id(self):
        return self._pre_consult_id

    @pre_consult_id.setter
    def pre_consult_id(self, value):
        self._pre_consult_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_biz_params:
            if hasattr(self.auth_biz_params, 'to_alipay_dict'):
                params['auth_biz_params'] = self.auth_biz_params.to_alipay_dict()
            else:
                params['auth_biz_params'] = self.auth_biz_params
        if self.pay_operation_info:
            if hasattr(self.pay_operation_info, 'to_alipay_dict'):
                params['pay_operation_info'] = self.pay_operation_info.to_alipay_dict()
            else:
                params['pay_operation_info'] = self.pay_operation_info
        if self.pre_consult_id:
            if hasattr(self.pre_consult_id, 'to_alipay_dict'):
                params['pre_consult_id'] = self.pre_consult_id.to_alipay_dict()
            else:
                params['pre_consult_id'] = self.pre_consult_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProdParams()
        if 'auth_biz_params' in d:
            o.auth_biz_params = d['auth_biz_params']
        if 'pay_operation_info' in d:
            o.pay_operation_info = d['pay_operation_info']
        if 'pre_consult_id' in d:
            o.pre_consult_id = d['pre_consult_id']
        return o


