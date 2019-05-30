#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAlideviceinfoOfflinecodeCreateModel(object):

    def __init__(self):
        self._biz_tag = None
        self._biz_tid = None
        self._biz_type = None
        self._item_id = None
        self._merchant_pid = None
        self._product_code = None
        self._protocol_version = None
        self._sn = None
        self._supplier_id = None

    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def protocol_version(self):
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, value):
        self._protocol_version = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.protocol_version:
            if hasattr(self.protocol_version, 'to_alipay_dict'):
                params['protocol_version'] = self.protocol_version.to_alipay_dict()
            else:
                params['protocol_version'] = self.protocol_version
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAlideviceinfoOfflinecodeCreateModel()
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'protocol_version' in d:
            o.protocol_version = d['protocol_version']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


