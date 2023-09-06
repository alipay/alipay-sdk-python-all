#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CashSummaryDTO import CashSummaryDTO


class ResponseModelForPaymentInstruction(object):

    def __init__(self):
        self._data = None
        self._error_code = None
        self._error_detail_info = None
        self._error_msg = None
        self._success = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, CashSummaryDTO):
                    self._data.append(i)
                else:
                    self._data.append(CashSummaryDTO.from_alipay_dict(i))
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_detail_info(self):
        return self._error_detail_info

    @error_detail_info.setter
    def error_detail_info(self, value):
        self._error_detail_info = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_detail_info:
            if hasattr(self.error_detail_info, 'to_alipay_dict'):
                params['error_detail_info'] = self.error_detail_info.to_alipay_dict()
            else:
                params['error_detail_info'] = self.error_detail_info
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResponseModelForPaymentInstruction()
        if 'data' in d:
            o.data = d['data']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_detail_info' in d:
            o.error_detail_info = d['error_detail_info']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'success' in d:
            o.success = d['success']
        return o


