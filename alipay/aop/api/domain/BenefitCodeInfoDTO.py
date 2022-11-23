#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitCodeInfoDTO(object):

    def __init__(self):
        self._secret_voucher_file_key = None
        self._secret_voucher_general_code = None
        self._secret_voucher_style = None
        self._secret_voucher_type = None

    @property
    def secret_voucher_file_key(self):
        return self._secret_voucher_file_key

    @secret_voucher_file_key.setter
    def secret_voucher_file_key(self, value):
        self._secret_voucher_file_key = value
    @property
    def secret_voucher_general_code(self):
        return self._secret_voucher_general_code

    @secret_voucher_general_code.setter
    def secret_voucher_general_code(self, value):
        self._secret_voucher_general_code = value
    @property
    def secret_voucher_style(self):
        return self._secret_voucher_style

    @secret_voucher_style.setter
    def secret_voucher_style(self, value):
        self._secret_voucher_style = value
    @property
    def secret_voucher_type(self):
        return self._secret_voucher_type

    @secret_voucher_type.setter
    def secret_voucher_type(self, value):
        self._secret_voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.secret_voucher_file_key:
            if hasattr(self.secret_voucher_file_key, 'to_alipay_dict'):
                params['secret_voucher_file_key'] = self.secret_voucher_file_key.to_alipay_dict()
            else:
                params['secret_voucher_file_key'] = self.secret_voucher_file_key
        if self.secret_voucher_general_code:
            if hasattr(self.secret_voucher_general_code, 'to_alipay_dict'):
                params['secret_voucher_general_code'] = self.secret_voucher_general_code.to_alipay_dict()
            else:
                params['secret_voucher_general_code'] = self.secret_voucher_general_code
        if self.secret_voucher_style:
            if hasattr(self.secret_voucher_style, 'to_alipay_dict'):
                params['secret_voucher_style'] = self.secret_voucher_style.to_alipay_dict()
            else:
                params['secret_voucher_style'] = self.secret_voucher_style
        if self.secret_voucher_type:
            if hasattr(self.secret_voucher_type, 'to_alipay_dict'):
                params['secret_voucher_type'] = self.secret_voucher_type.to_alipay_dict()
            else:
                params['secret_voucher_type'] = self.secret_voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitCodeInfoDTO()
        if 'secret_voucher_file_key' in d:
            o.secret_voucher_file_key = d['secret_voucher_file_key']
        if 'secret_voucher_general_code' in d:
            o.secret_voucher_general_code = d['secret_voucher_general_code']
        if 'secret_voucher_style' in d:
            o.secret_voucher_style = d['secret_voucher_style']
        if 'secret_voucher_type' in d:
            o.secret_voucher_type = d['secret_voucher_type']
        return o


