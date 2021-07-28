#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandSavingPassQueryModel(object):

    def __init__(self):
        self._ch_info = None
        self._pid = None
        self._sol_code = None
        self._user_id = None

    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def sol_code(self):
        return self._sol_code

    @sol_code.setter
    def sol_code(self, value):
        self._sol_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.sol_code:
            if hasattr(self.sol_code, 'to_alipay_dict'):
                params['sol_code'] = self.sol_code.to_alipay_dict()
            else:
                params['sol_code'] = self.sol_code
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
        o = AntMerchantExpandSavingPassQueryModel()
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'pid' in d:
            o.pid = d['pid']
        if 'sol_code' in d:
            o.sol_code = d['sol_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


