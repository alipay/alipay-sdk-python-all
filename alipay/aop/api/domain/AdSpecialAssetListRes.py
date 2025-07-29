#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdSpecialAssetListRes(object):

    def __init__(self):
        self._available_unfreeze_amount = None
        self._rtb_freeze_order_id = None
        self._special_name = None
        self._status = None

    @property
    def available_unfreeze_amount(self):
        return self._available_unfreeze_amount

    @available_unfreeze_amount.setter
    def available_unfreeze_amount(self, value):
        self._available_unfreeze_amount = value
    @property
    def rtb_freeze_order_id(self):
        return self._rtb_freeze_order_id

    @rtb_freeze_order_id.setter
    def rtb_freeze_order_id(self, value):
        self._rtb_freeze_order_id = value
    @property
    def special_name(self):
        return self._special_name

    @special_name.setter
    def special_name(self, value):
        self._special_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_unfreeze_amount:
            if hasattr(self.available_unfreeze_amount, 'to_alipay_dict'):
                params['available_unfreeze_amount'] = self.available_unfreeze_amount.to_alipay_dict()
            else:
                params['available_unfreeze_amount'] = self.available_unfreeze_amount
        if self.rtb_freeze_order_id:
            if hasattr(self.rtb_freeze_order_id, 'to_alipay_dict'):
                params['rtb_freeze_order_id'] = self.rtb_freeze_order_id.to_alipay_dict()
            else:
                params['rtb_freeze_order_id'] = self.rtb_freeze_order_id
        if self.special_name:
            if hasattr(self.special_name, 'to_alipay_dict'):
                params['special_name'] = self.special_name.to_alipay_dict()
            else:
                params['special_name'] = self.special_name
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
        o = AdSpecialAssetListRes()
        if 'available_unfreeze_amount' in d:
            o.available_unfreeze_amount = d['available_unfreeze_amount']
        if 'rtb_freeze_order_id' in d:
            o.rtb_freeze_order_id = d['rtb_freeze_order_id']
        if 'special_name' in d:
            o.special_name = d['special_name']
        if 'status' in d:
            o.status = d['status']
        return o


