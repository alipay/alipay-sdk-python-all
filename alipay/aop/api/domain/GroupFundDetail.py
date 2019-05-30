#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupFundDetail(object):

    def __init__(self):
        self._amount = None
        self._receiver_user_id = None
        self._sender_user_id = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def receiver_user_id(self):
        return self._receiver_user_id

    @receiver_user_id.setter
    def receiver_user_id(self, value):
        self._receiver_user_id = value
    @property
    def sender_user_id(self):
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, value):
        self._sender_user_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.receiver_user_id:
            if hasattr(self.receiver_user_id, 'to_alipay_dict'):
                params['receiver_user_id'] = self.receiver_user_id.to_alipay_dict()
            else:
                params['receiver_user_id'] = self.receiver_user_id
        if self.sender_user_id:
            if hasattr(self.sender_user_id, 'to_alipay_dict'):
                params['sender_user_id'] = self.sender_user_id.to_alipay_dict()
            else:
                params['sender_user_id'] = self.sender_user_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupFundDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'receiver_user_id' in d:
            o.receiver_user_id = d['receiver_user_id']
        if 'sender_user_id' in d:
            o.sender_user_id = d['sender_user_id']
        if 'status' in d:
            o.status = d['status']
        return o


