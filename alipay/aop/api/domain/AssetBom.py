#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetBomAttribute import AssetBomAttribute
from alipay.aop.api.domain.AssetBomItem import AssetBomItem
from alipay.aop.api.domain.AssetStandard import AssetStandard


class AssetBom(object):

    def __init__(self):
        self._asset_sub_type = None
        self._attributes = None
        self._biz_type = None
        self._bom_items = None
        self._effect_img = None
        self._include_qrcode = None
        self._is_suite = None
        self._item_id = None
        self._item_name = None
        self._item_type = None
        self._release_status = None
        self._request_id = None
        self._status = None
        self._std = None

    @property
    def asset_sub_type(self):
        return self._asset_sub_type

    @asset_sub_type.setter
    def asset_sub_type(self, value):
        self._asset_sub_type = value
    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        if isinstance(value, list):
            self._attributes = list()
            for i in value:
                if isinstance(i, AssetBomAttribute):
                    self._attributes.append(i)
                else:
                    self._attributes.append(AssetBomAttribute.from_alipay_dict(i))
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def bom_items(self):
        return self._bom_items

    @bom_items.setter
    def bom_items(self, value):
        if isinstance(value, list):
            self._bom_items = list()
            for i in value:
                if isinstance(i, AssetBomItem):
                    self._bom_items.append(i)
                else:
                    self._bom_items.append(AssetBomItem.from_alipay_dict(i))
    @property
    def effect_img(self):
        return self._effect_img

    @effect_img.setter
    def effect_img(self, value):
        self._effect_img = value
    @property
    def include_qrcode(self):
        return self._include_qrcode

    @include_qrcode.setter
    def include_qrcode(self, value):
        self._include_qrcode = value
    @property
    def is_suite(self):
        return self._is_suite

    @is_suite.setter
    def is_suite(self, value):
        self._is_suite = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def release_status(self):
        return self._release_status

    @release_status.setter
    def release_status(self, value):
        self._release_status = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def std(self):
        return self._std

    @std.setter
    def std(self, value):
        if isinstance(value, AssetStandard):
            self._std = value
        else:
            self._std = AssetStandard.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_sub_type:
            if hasattr(self.asset_sub_type, 'to_alipay_dict'):
                params['asset_sub_type'] = self.asset_sub_type.to_alipay_dict()
            else:
                params['asset_sub_type'] = self.asset_sub_type
        if self.attributes:
            if isinstance(self.attributes, list):
                for i in range(0, len(self.attributes)):
                    element = self.attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attributes[i] = element.to_alipay_dict()
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.bom_items:
            if isinstance(self.bom_items, list):
                for i in range(0, len(self.bom_items)):
                    element = self.bom_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bom_items[i] = element.to_alipay_dict()
            if hasattr(self.bom_items, 'to_alipay_dict'):
                params['bom_items'] = self.bom_items.to_alipay_dict()
            else:
                params['bom_items'] = self.bom_items
        if self.effect_img:
            if hasattr(self.effect_img, 'to_alipay_dict'):
                params['effect_img'] = self.effect_img.to_alipay_dict()
            else:
                params['effect_img'] = self.effect_img
        if self.include_qrcode:
            if hasattr(self.include_qrcode, 'to_alipay_dict'):
                params['include_qrcode'] = self.include_qrcode.to_alipay_dict()
            else:
                params['include_qrcode'] = self.include_qrcode
        if self.is_suite:
            if hasattr(self.is_suite, 'to_alipay_dict'):
                params['is_suite'] = self.is_suite.to_alipay_dict()
            else:
                params['is_suite'] = self.is_suite
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.release_status:
            if hasattr(self.release_status, 'to_alipay_dict'):
                params['release_status'] = self.release_status.to_alipay_dict()
            else:
                params['release_status'] = self.release_status
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.std:
            if hasattr(self.std, 'to_alipay_dict'):
                params['std'] = self.std.to_alipay_dict()
            else:
                params['std'] = self.std
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetBom()
        if 'asset_sub_type' in d:
            o.asset_sub_type = d['asset_sub_type']
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'bom_items' in d:
            o.bom_items = d['bom_items']
        if 'effect_img' in d:
            o.effect_img = d['effect_img']
        if 'include_qrcode' in d:
            o.include_qrcode = d['include_qrcode']
        if 'is_suite' in d:
            o.is_suite = d['is_suite']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'release_status' in d:
            o.release_status = d['release_status']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'status' in d:
            o.status = d['status']
        if 'std' in d:
            o.std = d['std']
        return o


