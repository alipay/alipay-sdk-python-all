#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CashVoucherValueInfo import CashVoucherValueInfo
from alipay.aop.api.domain.ExchangeVoucherValueInfo import ExchangeVoucherValueInfo
from alipay.aop.api.domain.VoucherPrincipalInfo import VoucherPrincipalInfo
from alipay.aop.api.domain.VoucherRuleInfo import VoucherRuleInfo
from alipay.aop.api.domain.VoucherUsageInfo import VoucherUsageInfo


class AlipayUserKabaoVoucherCreateModel(object):

    def __init__(self):
        self._batch_id = None
        self._biz_use_scene = None
        self._cash_voucher_value_info = None
        self._end_date = None
        self._exchange_voucher_value_info = None
        self._open_id = None
        self._out_instance_id = None
        self._principal_info = None
        self._rule_info = None
        self._start_date = None
        self._type = None
        self._usage_info = None
        self._user_id = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def biz_use_scene(self):
        return self._biz_use_scene

    @biz_use_scene.setter
    def biz_use_scene(self, value):
        self._biz_use_scene = value
    @property
    def cash_voucher_value_info(self):
        return self._cash_voucher_value_info

    @cash_voucher_value_info.setter
    def cash_voucher_value_info(self, value):
        if isinstance(value, CashVoucherValueInfo):
            self._cash_voucher_value_info = value
        else:
            self._cash_voucher_value_info = CashVoucherValueInfo.from_alipay_dict(value)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def exchange_voucher_value_info(self):
        return self._exchange_voucher_value_info

    @exchange_voucher_value_info.setter
    def exchange_voucher_value_info(self, value):
        if isinstance(value, ExchangeVoucherValueInfo):
            self._exchange_voucher_value_info = value
        else:
            self._exchange_voucher_value_info = ExchangeVoucherValueInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_instance_id(self):
        return self._out_instance_id

    @out_instance_id.setter
    def out_instance_id(self, value):
        self._out_instance_id = value
    @property
    def principal_info(self):
        return self._principal_info

    @principal_info.setter
    def principal_info(self, value):
        if isinstance(value, VoucherPrincipalInfo):
            self._principal_info = value
        else:
            self._principal_info = VoucherPrincipalInfo.from_alipay_dict(value)
    @property
    def rule_info(self):
        return self._rule_info

    @rule_info.setter
    def rule_info(self, value):
        if isinstance(value, VoucherRuleInfo):
            self._rule_info = value
        else:
            self._rule_info = VoucherRuleInfo.from_alipay_dict(value)
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def usage_info(self):
        return self._usage_info

    @usage_info.setter
    def usage_info(self, value):
        if isinstance(value, VoucherUsageInfo):
            self._usage_info = value
        else:
            self._usage_info = VoucherUsageInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.biz_use_scene:
            if hasattr(self.biz_use_scene, 'to_alipay_dict'):
                params['biz_use_scene'] = self.biz_use_scene.to_alipay_dict()
            else:
                params['biz_use_scene'] = self.biz_use_scene
        if self.cash_voucher_value_info:
            if hasattr(self.cash_voucher_value_info, 'to_alipay_dict'):
                params['cash_voucher_value_info'] = self.cash_voucher_value_info.to_alipay_dict()
            else:
                params['cash_voucher_value_info'] = self.cash_voucher_value_info
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.exchange_voucher_value_info:
            if hasattr(self.exchange_voucher_value_info, 'to_alipay_dict'):
                params['exchange_voucher_value_info'] = self.exchange_voucher_value_info.to_alipay_dict()
            else:
                params['exchange_voucher_value_info'] = self.exchange_voucher_value_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_instance_id:
            if hasattr(self.out_instance_id, 'to_alipay_dict'):
                params['out_instance_id'] = self.out_instance_id.to_alipay_dict()
            else:
                params['out_instance_id'] = self.out_instance_id
        if self.principal_info:
            if hasattr(self.principal_info, 'to_alipay_dict'):
                params['principal_info'] = self.principal_info.to_alipay_dict()
            else:
                params['principal_info'] = self.principal_info
        if self.rule_info:
            if hasattr(self.rule_info, 'to_alipay_dict'):
                params['rule_info'] = self.rule_info.to_alipay_dict()
            else:
                params['rule_info'] = self.rule_info
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.usage_info:
            if hasattr(self.usage_info, 'to_alipay_dict'):
                params['usage_info'] = self.usage_info.to_alipay_dict()
            else:
                params['usage_info'] = self.usage_info
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
        o = AlipayUserKabaoVoucherCreateModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'biz_use_scene' in d:
            o.biz_use_scene = d['biz_use_scene']
        if 'cash_voucher_value_info' in d:
            o.cash_voucher_value_info = d['cash_voucher_value_info']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'exchange_voucher_value_info' in d:
            o.exchange_voucher_value_info = d['exchange_voucher_value_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_instance_id' in d:
            o.out_instance_id = d['out_instance_id']
        if 'principal_info' in d:
            o.principal_info = d['principal_info']
        if 'rule_info' in d:
            o.rule_info = d['rule_info']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'type' in d:
            o.type = d['type']
        if 'usage_info' in d:
            o.usage_info = d['usage_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


