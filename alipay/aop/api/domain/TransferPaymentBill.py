#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferUser import TransferUser
from alipay.aop.api.domain.TransferAmount import TransferAmount
from alipay.aop.api.domain.TransferPaymentItem import TransferPaymentItem


class TransferPaymentBill(object):

    def __init__(self):
        self._account_owner = None
        self._bill_amount = None
        self._channel_payment_ref = None
        self._channel_remit_time = None
        self._expect_transfer_time = None
        self._payment_account_no = None
        self._payment_expiry_time = None
        self._payment_items = None
        self._reference_goods_id = None
        self._transfer_base_time = None

    @property
    def account_owner(self):
        return self._account_owner

    @account_owner.setter
    def account_owner(self, value):
        if isinstance(value, TransferUser):
            self._account_owner = value
        else:
            self._account_owner = TransferUser.from_alipay_dict(value)
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        if isinstance(value, TransferAmount):
            self._bill_amount = value
        else:
            self._bill_amount = TransferAmount.from_alipay_dict(value)
    @property
    def channel_payment_ref(self):
        return self._channel_payment_ref

    @channel_payment_ref.setter
    def channel_payment_ref(self, value):
        self._channel_payment_ref = value
    @property
    def channel_remit_time(self):
        return self._channel_remit_time

    @channel_remit_time.setter
    def channel_remit_time(self, value):
        self._channel_remit_time = value
    @property
    def expect_transfer_time(self):
        return self._expect_transfer_time

    @expect_transfer_time.setter
    def expect_transfer_time(self, value):
        self._expect_transfer_time = value
    @property
    def payment_account_no(self):
        return self._payment_account_no

    @payment_account_no.setter
    def payment_account_no(self, value):
        self._payment_account_no = value
    @property
    def payment_expiry_time(self):
        return self._payment_expiry_time

    @payment_expiry_time.setter
    def payment_expiry_time(self, value):
        self._payment_expiry_time = value
    @property
    def payment_items(self):
        return self._payment_items

    @payment_items.setter
    def payment_items(self, value):
        if isinstance(value, list):
            self._payment_items = list()
            for i in value:
                if isinstance(i, TransferPaymentItem):
                    self._payment_items.append(i)
                else:
                    self._payment_items.append(TransferPaymentItem.from_alipay_dict(i))
    @property
    def reference_goods_id(self):
        return self._reference_goods_id

    @reference_goods_id.setter
    def reference_goods_id(self, value):
        self._reference_goods_id = value
    @property
    def transfer_base_time(self):
        return self._transfer_base_time

    @transfer_base_time.setter
    def transfer_base_time(self, value):
        self._transfer_base_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_owner:
            if hasattr(self.account_owner, 'to_alipay_dict'):
                params['account_owner'] = self.account_owner.to_alipay_dict()
            else:
                params['account_owner'] = self.account_owner
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.channel_payment_ref:
            if hasattr(self.channel_payment_ref, 'to_alipay_dict'):
                params['channel_payment_ref'] = self.channel_payment_ref.to_alipay_dict()
            else:
                params['channel_payment_ref'] = self.channel_payment_ref
        if self.channel_remit_time:
            if hasattr(self.channel_remit_time, 'to_alipay_dict'):
                params['channel_remit_time'] = self.channel_remit_time.to_alipay_dict()
            else:
                params['channel_remit_time'] = self.channel_remit_time
        if self.expect_transfer_time:
            if hasattr(self.expect_transfer_time, 'to_alipay_dict'):
                params['expect_transfer_time'] = self.expect_transfer_time.to_alipay_dict()
            else:
                params['expect_transfer_time'] = self.expect_transfer_time
        if self.payment_account_no:
            if hasattr(self.payment_account_no, 'to_alipay_dict'):
                params['payment_account_no'] = self.payment_account_no.to_alipay_dict()
            else:
                params['payment_account_no'] = self.payment_account_no
        if self.payment_expiry_time:
            if hasattr(self.payment_expiry_time, 'to_alipay_dict'):
                params['payment_expiry_time'] = self.payment_expiry_time.to_alipay_dict()
            else:
                params['payment_expiry_time'] = self.payment_expiry_time
        if self.payment_items:
            if isinstance(self.payment_items, list):
                for i in range(0, len(self.payment_items)):
                    element = self.payment_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_items[i] = element.to_alipay_dict()
            if hasattr(self.payment_items, 'to_alipay_dict'):
                params['payment_items'] = self.payment_items.to_alipay_dict()
            else:
                params['payment_items'] = self.payment_items
        if self.reference_goods_id:
            if hasattr(self.reference_goods_id, 'to_alipay_dict'):
                params['reference_goods_id'] = self.reference_goods_id.to_alipay_dict()
            else:
                params['reference_goods_id'] = self.reference_goods_id
        if self.transfer_base_time:
            if hasattr(self.transfer_base_time, 'to_alipay_dict'):
                params['transfer_base_time'] = self.transfer_base_time.to_alipay_dict()
            else:
                params['transfer_base_time'] = self.transfer_base_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferPaymentBill()
        if 'account_owner' in d:
            o.account_owner = d['account_owner']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'channel_payment_ref' in d:
            o.channel_payment_ref = d['channel_payment_ref']
        if 'channel_remit_time' in d:
            o.channel_remit_time = d['channel_remit_time']
        if 'expect_transfer_time' in d:
            o.expect_transfer_time = d['expect_transfer_time']
        if 'payment_account_no' in d:
            o.payment_account_no = d['payment_account_no']
        if 'payment_expiry_time' in d:
            o.payment_expiry_time = d['payment_expiry_time']
        if 'payment_items' in d:
            o.payment_items = d['payment_items']
        if 'reference_goods_id' in d:
            o.reference_goods_id = d['reference_goods_id']
        if 'transfer_base_time' in d:
            o.transfer_base_time = d['transfer_base_time']
        return o


