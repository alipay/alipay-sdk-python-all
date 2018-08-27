#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertAdvSingleVoucherResponse import KbAdvertAdvSingleVoucherResponse


class KbAdvertAdvResponse(object):

    def __init__(self):
        self._adv_id = None
        self._name = None
        self._single_voucher = None
        self._type = None

    @property
    def adv_id(self):
        return self._adv_id

    @adv_id.setter
    def adv_id(self, value):
        self._adv_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def single_voucher(self):
        return self._single_voucher

    @single_voucher.setter
    def single_voucher(self, value):
        if isinstance(value, KbAdvertAdvSingleVoucherResponse):
            self._single_voucher = value
        else:
            self._single_voucher = KbAdvertAdvSingleVoucherResponse.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.adv_id:
            if hasattr(self.adv_id, 'to_alipay_dict'):
                params['adv_id'] = self.adv_id.to_alipay_dict()
            else:
                params['adv_id'] = self.adv_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.single_voucher:
            if hasattr(self.single_voucher, 'to_alipay_dict'):
                params['single_voucher'] = self.single_voucher.to_alipay_dict()
            else:
                params['single_voucher'] = self.single_voucher
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertAdvResponse()
        if 'adv_id' in d:
            o.adv_id = d['adv_id']
        if 'name' in d:
            o.name = d['name']
        if 'single_voucher' in d:
            o.single_voucher = d['single_voucher']
        if 'type' in d:
            o.type = d['type']
        return o


