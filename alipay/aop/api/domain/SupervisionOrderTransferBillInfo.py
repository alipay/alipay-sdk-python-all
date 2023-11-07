#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupervisionOrderTransferBillInfo(object):

    def __init__(self):
        self._account_no = None
        self._amount = None
        self._biz_scene = None
        self._currency = None
        self._out_flow_id = None
        self._relation_out_order_no = None
        self._transfer_scene = None
        self._transfer_status = None
        self._transfer_time = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def out_flow_id(self):
        return self._out_flow_id

    @out_flow_id.setter
    def out_flow_id(self, value):
        self._out_flow_id = value
    @property
    def relation_out_order_no(self):
        return self._relation_out_order_no

    @relation_out_order_no.setter
    def relation_out_order_no(self, value):
        self._relation_out_order_no = value
    @property
    def transfer_scene(self):
        return self._transfer_scene

    @transfer_scene.setter
    def transfer_scene(self, value):
        self._transfer_scene = value
    @property
    def transfer_status(self):
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, value):
        self._transfer_status = value
    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, value):
        self._transfer_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.out_flow_id:
            if hasattr(self.out_flow_id, 'to_alipay_dict'):
                params['out_flow_id'] = self.out_flow_id.to_alipay_dict()
            else:
                params['out_flow_id'] = self.out_flow_id
        if self.relation_out_order_no:
            if hasattr(self.relation_out_order_no, 'to_alipay_dict'):
                params['relation_out_order_no'] = self.relation_out_order_no.to_alipay_dict()
            else:
                params['relation_out_order_no'] = self.relation_out_order_no
        if self.transfer_scene:
            if hasattr(self.transfer_scene, 'to_alipay_dict'):
                params['transfer_scene'] = self.transfer_scene.to_alipay_dict()
            else:
                params['transfer_scene'] = self.transfer_scene
        if self.transfer_status:
            if hasattr(self.transfer_status, 'to_alipay_dict'):
                params['transfer_status'] = self.transfer_status.to_alipay_dict()
            else:
                params['transfer_status'] = self.transfer_status
        if self.transfer_time:
            if hasattr(self.transfer_time, 'to_alipay_dict'):
                params['transfer_time'] = self.transfer_time.to_alipay_dict()
            else:
                params['transfer_time'] = self.transfer_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupervisionOrderTransferBillInfo()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'currency' in d:
            o.currency = d['currency']
        if 'out_flow_id' in d:
            o.out_flow_id = d['out_flow_id']
        if 'relation_out_order_no' in d:
            o.relation_out_order_no = d['relation_out_order_no']
        if 'transfer_scene' in d:
            o.transfer_scene = d['transfer_scene']
        if 'transfer_status' in d:
            o.transfer_status = d['transfer_status']
        if 'transfer_time' in d:
            o.transfer_time = d['transfer_time']
        return o


