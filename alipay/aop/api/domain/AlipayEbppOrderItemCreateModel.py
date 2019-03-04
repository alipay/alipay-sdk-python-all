#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EbppOrderItemToCreate import EbppOrderItemToCreate


class AlipayEbppOrderItemCreateModel(object):

    def __init__(self):
        self._expire_at = None
        self._item_to_create = None
        self._qrcode_required = None

    @property
    def expire_at(self):
        return self._expire_at

    @expire_at.setter
    def expire_at(self, value):
        self._expire_at = value
    @property
    def item_to_create(self):
        return self._item_to_create

    @item_to_create.setter
    def item_to_create(self, value):
        if isinstance(value, EbppOrderItemToCreate):
            self._item_to_create = value
        else:
            self._item_to_create = EbppOrderItemToCreate.from_alipay_dict(value)
    @property
    def qrcode_required(self):
        return self._qrcode_required

    @qrcode_required.setter
    def qrcode_required(self, value):
        self._qrcode_required = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire_at:
            if hasattr(self.expire_at, 'to_alipay_dict'):
                params['expire_at'] = self.expire_at.to_alipay_dict()
            else:
                params['expire_at'] = self.expire_at
        if self.item_to_create:
            if hasattr(self.item_to_create, 'to_alipay_dict'):
                params['item_to_create'] = self.item_to_create.to_alipay_dict()
            else:
                params['item_to_create'] = self.item_to_create
        if self.qrcode_required:
            if hasattr(self.qrcode_required, 'to_alipay_dict'):
                params['qrcode_required'] = self.qrcode_required.to_alipay_dict()
            else:
                params['qrcode_required'] = self.qrcode_required
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppOrderItemCreateModel()
        if 'expire_at' in d:
            o.expire_at = d['expire_at']
        if 'item_to_create' in d:
            o.item_to_create = d['item_to_create']
        if 'qrcode_required' in d:
            o.qrcode_required = d['qrcode_required']
        return o


