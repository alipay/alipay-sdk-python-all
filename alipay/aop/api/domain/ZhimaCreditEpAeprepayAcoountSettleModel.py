#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmEpAePrepayExtParam import ZmEpAePrepayExtParam
from alipay.aop.api.domain.ZmepAePrepayWriteOffDetailDTO import ZmepAePrepayWriteOffDetailDTO


class ZhimaCreditEpAeprepayAcoountSettleModel(object):

    def __init__(self):
        self._actual_amount = None
        self._actual_amount_currency = None
        self._apply_amount = None
        self._apply_amount_currency = None
        self._channel = None
        self._ext_param = None
        self._seller_login_id = None
        self._write_off_apply_no = None
        self._write_off_order_param_list = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def actual_amount_currency(self):
        return self._actual_amount_currency

    @actual_amount_currency.setter
    def actual_amount_currency(self, value):
        self._actual_amount_currency = value
    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def apply_amount_currency(self):
        return self._apply_amount_currency

    @apply_amount_currency.setter
    def apply_amount_currency(self, value):
        self._apply_amount_currency = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        if isinstance(value, ZmEpAePrepayExtParam):
            self._ext_param = value
        else:
            self._ext_param = ZmEpAePrepayExtParam.from_alipay_dict(value)
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def write_off_apply_no(self):
        return self._write_off_apply_no

    @write_off_apply_no.setter
    def write_off_apply_no(self, value):
        self._write_off_apply_no = value
    @property
    def write_off_order_param_list(self):
        return self._write_off_order_param_list

    @write_off_order_param_list.setter
    def write_off_order_param_list(self, value):
        if isinstance(value, list):
            self._write_off_order_param_list = list()
            for i in value:
                if isinstance(i, ZmepAePrepayWriteOffDetailDTO):
                    self._write_off_order_param_list.append(i)
                else:
                    self._write_off_order_param_list.append(ZmepAePrepayWriteOffDetailDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.actual_amount_currency:
            if hasattr(self.actual_amount_currency, 'to_alipay_dict'):
                params['actual_amount_currency'] = self.actual_amount_currency.to_alipay_dict()
            else:
                params['actual_amount_currency'] = self.actual_amount_currency
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.apply_amount_currency:
            if hasattr(self.apply_amount_currency, 'to_alipay_dict'):
                params['apply_amount_currency'] = self.apply_amount_currency.to_alipay_dict()
            else:
                params['apply_amount_currency'] = self.apply_amount_currency
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.write_off_apply_no:
            if hasattr(self.write_off_apply_no, 'to_alipay_dict'):
                params['write_off_apply_no'] = self.write_off_apply_no.to_alipay_dict()
            else:
                params['write_off_apply_no'] = self.write_off_apply_no
        if self.write_off_order_param_list:
            if isinstance(self.write_off_order_param_list, list):
                for i in range(0, len(self.write_off_order_param_list)):
                    element = self.write_off_order_param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.write_off_order_param_list[i] = element.to_alipay_dict()
            if hasattr(self.write_off_order_param_list, 'to_alipay_dict'):
                params['write_off_order_param_list'] = self.write_off_order_param_list.to_alipay_dict()
            else:
                params['write_off_order_param_list'] = self.write_off_order_param_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAeprepayAcoountSettleModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'actual_amount_currency' in d:
            o.actual_amount_currency = d['actual_amount_currency']
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'apply_amount_currency' in d:
            o.apply_amount_currency = d['apply_amount_currency']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'write_off_apply_no' in d:
            o.write_off_apply_no = d['write_off_apply_no']
        if 'write_off_order_param_list' in d:
            o.write_off_order_param_list = d['write_off_order_param_list']
        return o


