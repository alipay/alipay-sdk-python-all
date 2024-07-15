#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenVoucherBizDataDTO(object):

    def __init__(self):
        self._encrypt_phone = None

    @property
    def encrypt_phone(self):
        return self._encrypt_phone

    @encrypt_phone.setter
    def encrypt_phone(self, value):
        self._encrypt_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_phone:
            if hasattr(self.encrypt_phone, 'to_alipay_dict'):
                params['encrypt_phone'] = self.encrypt_phone.to_alipay_dict()
            else:
                params['encrypt_phone'] = self.encrypt_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenVoucherBizDataDTO()
        if 'encrypt_phone' in d:
            o.encrypt_phone = d['encrypt_phone']
        return o


