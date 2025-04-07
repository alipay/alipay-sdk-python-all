#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DivinationBizContextDetail import DivinationBizContextDetail


class AnttechAiDevicePayCallbackModel(object):

    def __init__(self):
        self._biz_context = None
        self._biz_receipt = None
        self._device_id = None
        self._external_client_id = None
        self._external_client_name = None
        self._pay_amount = None
        self._pay_date = None
        self._pay_scene = None
        self._request_id = None

    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        if isinstance(value, DivinationBizContextDetail):
            self._biz_context = value
        else:
            self._biz_context = DivinationBizContextDetail.from_alipay_dict(value)
    @property
    def biz_receipt(self):
        return self._biz_receipt

    @biz_receipt.setter
    def biz_receipt(self, value):
        self._biz_receipt = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def external_client_id(self):
        return self._external_client_id

    @external_client_id.setter
    def external_client_id(self, value):
        self._external_client_id = value
    @property
    def external_client_name(self):
        return self._external_client_name

    @external_client_name.setter
    def external_client_name(self, value):
        self._external_client_name = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_scene(self):
        return self._pay_scene

    @pay_scene.setter
    def pay_scene(self, value):
        self._pay_scene = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.biz_receipt:
            if hasattr(self.biz_receipt, 'to_alipay_dict'):
                params['biz_receipt'] = self.biz_receipt.to_alipay_dict()
            else:
                params['biz_receipt'] = self.biz_receipt
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.external_client_id:
            if hasattr(self.external_client_id, 'to_alipay_dict'):
                params['external_client_id'] = self.external_client_id.to_alipay_dict()
            else:
                params['external_client_id'] = self.external_client_id
        if self.external_client_name:
            if hasattr(self.external_client_name, 'to_alipay_dict'):
                params['external_client_name'] = self.external_client_name.to_alipay_dict()
            else:
                params['external_client_name'] = self.external_client_name
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pay_scene:
            if hasattr(self.pay_scene, 'to_alipay_dict'):
                params['pay_scene'] = self.pay_scene.to_alipay_dict()
            else:
                params['pay_scene'] = self.pay_scene
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiDevicePayCallbackModel()
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'biz_receipt' in d:
            o.biz_receipt = d['biz_receipt']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'external_client_id' in d:
            o.external_client_id = d['external_client_id']
        if 'external_client_name' in d:
            o.external_client_name = d['external_client_name']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pay_scene' in d:
            o.pay_scene = d['pay_scene']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


