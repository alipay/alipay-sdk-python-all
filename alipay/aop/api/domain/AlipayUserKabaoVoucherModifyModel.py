#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExchangeVoucherValueInfo import ExchangeVoucherValueInfo


class AlipayUserKabaoVoucherModifyModel(object):

    def __init__(self):
        self._exchange_voucher_value_info = None
        self._instance_id = None
        self._open_id = None
        self._status = None
        self._user_id = None

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
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_voucher_value_info:
            if hasattr(self.exchange_voucher_value_info, 'to_alipay_dict'):
                params['exchange_voucher_value_info'] = self.exchange_voucher_value_info.to_alipay_dict()
            else:
                params['exchange_voucher_value_info'] = self.exchange_voucher_value_info
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayUserKabaoVoucherModifyModel()
        if 'exchange_voucher_value_info' in d:
            o.exchange_voucher_value_info = d['exchange_voucher_value_info']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


