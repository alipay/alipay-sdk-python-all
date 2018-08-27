#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FeeValue import FeeValue
from alipay.aop.api.domain.ValidStrategy import ValidStrategy


class AlipayFinancialnetAuthContractMerchantSignModel(object):

    def __init__(self):
        self._account_no = None
        self._ext_info = None
        self._fee_value = None
        self._inst_id = None
        self._scene_code = None
        self._user_id = None
        self._valid_strategy = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fee_value(self):
        return self._fee_value

    @fee_value.setter
    def fee_value(self, value):
        if isinstance(value, FeeValue):
            self._fee_value = value
        else:
            self._fee_value = FeeValue.from_alipay_dict(value)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_strategy(self):
        return self._valid_strategy

    @valid_strategy.setter
    def valid_strategy(self, value):
        if isinstance(value, ValidStrategy):
            self._valid_strategy = value
        else:
            self._valid_strategy = ValidStrategy.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fee_value:
            if hasattr(self.fee_value, 'to_alipay_dict'):
                params['fee_value'] = self.fee_value.to_alipay_dict()
            else:
                params['fee_value'] = self.fee_value
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_strategy:
            if hasattr(self.valid_strategy, 'to_alipay_dict'):
                params['valid_strategy'] = self.valid_strategy.to_alipay_dict()
            else:
                params['valid_strategy'] = self.valid_strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthContractMerchantSignModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fee_value' in d:
            o.fee_value = d['fee_value']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_strategy' in d:
            o.valid_strategy = d['valid_strategy']
        return o


