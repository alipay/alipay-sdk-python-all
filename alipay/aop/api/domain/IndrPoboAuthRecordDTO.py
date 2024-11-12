#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO


class IndrPoboAuthRecordDTO(object):

    def __init__(self):
        self._auth_amount = None
        self._auth_result = None
        self._channel_message = None
        self._create_time = None
        self._mcc = None
        self._merchant_name = None
        self._transaction_id = None

    @property
    def auth_amount(self):
        return self._auth_amount

    @auth_amount.setter
    def auth_amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._auth_amount = value
        else:
            self._auth_amount = IndrMoneyDTO.from_alipay_dict(value)
    @property
    def auth_result(self):
        return self._auth_result

    @auth_result.setter
    def auth_result(self, value):
        self._auth_result = value
    @property
    def channel_message(self):
        return self._channel_message

    @channel_message.setter
    def channel_message(self, value):
        self._channel_message = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_amount:
            if hasattr(self.auth_amount, 'to_alipay_dict'):
                params['auth_amount'] = self.auth_amount.to_alipay_dict()
            else:
                params['auth_amount'] = self.auth_amount
        if self.auth_result:
            if hasattr(self.auth_result, 'to_alipay_dict'):
                params['auth_result'] = self.auth_result.to_alipay_dict()
            else:
                params['auth_result'] = self.auth_result
        if self.channel_message:
            if hasattr(self.channel_message, 'to_alipay_dict'):
                params['channel_message'] = self.channel_message.to_alipay_dict()
            else:
                params['channel_message'] = self.channel_message
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrPoboAuthRecordDTO()
        if 'auth_amount' in d:
            o.auth_amount = d['auth_amount']
        if 'auth_result' in d:
            o.auth_result = d['auth_result']
        if 'channel_message' in d:
            o.channel_message = d['channel_message']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


