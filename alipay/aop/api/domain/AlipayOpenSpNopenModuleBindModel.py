#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNopenModuleBindModel(object):

    def __init__(self):
        self._device_ad_id = None
        self._device_biz_tid = None
        self._device_item_id = None
        self._device_sn = None
        self._item_id = None
        self._sn = None
        self._supplier_id = None
        self._url = None

    @property
    def device_ad_id(self):
        return self._device_ad_id

    @device_ad_id.setter
    def device_ad_id(self, value):
        self._device_ad_id = value
    @property
    def device_biz_tid(self):
        return self._device_biz_tid

    @device_biz_tid.setter
    def device_biz_tid(self, value):
        self._device_biz_tid = value
    @property
    def device_item_id(self):
        return self._device_item_id

    @device_item_id.setter
    def device_item_id(self, value):
        self._device_item_id = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
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
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_ad_id:
            if hasattr(self.device_ad_id, 'to_alipay_dict'):
                params['device_ad_id'] = self.device_ad_id.to_alipay_dict()
            else:
                params['device_ad_id'] = self.device_ad_id
        if self.device_biz_tid:
            if hasattr(self.device_biz_tid, 'to_alipay_dict'):
                params['device_biz_tid'] = self.device_biz_tid.to_alipay_dict()
            else:
                params['device_biz_tid'] = self.device_biz_tid
        if self.device_item_id:
            if hasattr(self.device_item_id, 'to_alipay_dict'):
                params['device_item_id'] = self.device_item_id.to_alipay_dict()
            else:
                params['device_item_id'] = self.device_item_id
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
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
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNopenModuleBindModel()
        if 'device_ad_id' in d:
            o.device_ad_id = d['device_ad_id']
        if 'device_biz_tid' in d:
            o.device_biz_tid = d['device_biz_tid']
        if 'device_item_id' in d:
            o.device_item_id = d['device_item_id']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'url' in d:
            o.url = d['url']
        return o


