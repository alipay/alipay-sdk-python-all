#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherDetailInfoDTO import VoucherDetailInfoDTO


class PayInfoVO(object):

    def __init__(self):
        self._pay_channels = None
        self._pay_time = None
        self._transaction_id = None
        self._voucher_detail_list = None

    @property
    def pay_channels(self):
        return self._pay_channels

    @pay_channels.setter
    def pay_channels(self, value):
        if isinstance(value, list):
            self._pay_channels = list()
            for i in value:
                self._pay_channels.append(i)
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    @property
    def voucher_detail_list(self):
        return self._voucher_detail_list

    @voucher_detail_list.setter
    def voucher_detail_list(self, value):
        if isinstance(value, list):
            self._voucher_detail_list = list()
            for i in value:
                if isinstance(i, VoucherDetailInfoDTO):
                    self._voucher_detail_list.append(i)
                else:
                    self._voucher_detail_list.append(VoucherDetailInfoDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.pay_channels:
            if isinstance(self.pay_channels, list):
                for i in range(0, len(self.pay_channels)):
                    element = self.pay_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_channels[i] = element.to_alipay_dict()
            if hasattr(self.pay_channels, 'to_alipay_dict'):
                params['pay_channels'] = self.pay_channels.to_alipay_dict()
            else:
                params['pay_channels'] = self.pay_channels
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        if self.voucher_detail_list:
            if isinstance(self.voucher_detail_list, list):
                for i in range(0, len(self.voucher_detail_list)):
                    element = self.voucher_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_detail_list, 'to_alipay_dict'):
                params['voucher_detail_list'] = self.voucher_detail_list.to_alipay_dict()
            else:
                params['voucher_detail_list'] = self.voucher_detail_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayInfoVO()
        if 'pay_channels' in d:
            o.pay_channels = d['pay_channels']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        if 'voucher_detail_list' in d:
            o.voucher_detail_list = d['voucher_detail_list']
        return o


