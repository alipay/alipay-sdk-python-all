#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SendCodeResult import SendCodeResult


class AlipayMarketingCertificateCertificatetionSendcallbackModel(object):

    def __init__(self):
        self._open_id = None
        self._order_id = None
        self._result_code = None
        self._send_code_result_list = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def send_code_result_list(self):
        return self._send_code_result_list

    @send_code_result_list.setter
    def send_code_result_list(self, value):
        if isinstance(value, list):
            self._send_code_result_list = list()
            for i in value:
                if isinstance(i, SendCodeResult):
                    self._send_code_result_list.append(i)
                else:
                    self._send_code_result_list.append(SendCodeResult.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.send_code_result_list:
            if isinstance(self.send_code_result_list, list):
                for i in range(0, len(self.send_code_result_list)):
                    element = self.send_code_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.send_code_result_list[i] = element.to_alipay_dict()
            if hasattr(self.send_code_result_list, 'to_alipay_dict'):
                params['send_code_result_list'] = self.send_code_result_list.to_alipay_dict()
            else:
                params['send_code_result_list'] = self.send_code_result_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCertificateCertificatetionSendcallbackModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'send_code_result_list' in d:
            o.send_code_result_list = d['send_code_result_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


