#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransBillCloseModel(object):

    def __init__(self):
        self._transfer_no = None
        self._user_id = None

    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.transfer_no:
            if hasattr(self.transfer_no, 'to_alipay_dict'):
                params['transfer_no'] = self.transfer_no.to_alipay_dict()
            else:
                params['transfer_no'] = self.transfer_no
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
        o = AlipayFundTransBillCloseModel()
        if 'transfer_no' in d:
            o.transfer_no = d['transfer_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


