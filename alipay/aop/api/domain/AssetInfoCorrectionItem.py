#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetInfoCorrectionItem(object):

    def __init__(self):
        self._assign_item_id = None
        self._change_reason = None
        self._change_type = None
        self._item_id = None
        self._new_asset_value = None
        self._new_item_id = None
        self._original_asset_value = None
        self._original_supplier_id = None
        self._request_id = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def change_reason(self):
        return self._change_reason

    @change_reason.setter
    def change_reason(self, value):
        self._change_reason = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def new_asset_value(self):
        return self._new_asset_value

    @new_asset_value.setter
    def new_asset_value(self, value):
        self._new_asset_value = value
    @property
    def new_item_id(self):
        return self._new_item_id

    @new_item_id.setter
    def new_item_id(self, value):
        self._new_item_id = value
    @property
    def original_asset_value(self):
        return self._original_asset_value

    @original_asset_value.setter
    def original_asset_value(self, value):
        self._original_asset_value = value
    @property
    def original_supplier_id(self):
        return self._original_supplier_id

    @original_supplier_id.setter
    def original_supplier_id(self, value):
        self._original_supplier_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.change_reason:
            if hasattr(self.change_reason, 'to_alipay_dict'):
                params['change_reason'] = self.change_reason.to_alipay_dict()
            else:
                params['change_reason'] = self.change_reason
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.new_asset_value:
            if hasattr(self.new_asset_value, 'to_alipay_dict'):
                params['new_asset_value'] = self.new_asset_value.to_alipay_dict()
            else:
                params['new_asset_value'] = self.new_asset_value
        if self.new_item_id:
            if hasattr(self.new_item_id, 'to_alipay_dict'):
                params['new_item_id'] = self.new_item_id.to_alipay_dict()
            else:
                params['new_item_id'] = self.new_item_id
        if self.original_asset_value:
            if hasattr(self.original_asset_value, 'to_alipay_dict'):
                params['original_asset_value'] = self.original_asset_value.to_alipay_dict()
            else:
                params['original_asset_value'] = self.original_asset_value
        if self.original_supplier_id:
            if hasattr(self.original_supplier_id, 'to_alipay_dict'):
                params['original_supplier_id'] = self.original_supplier_id.to_alipay_dict()
            else:
                params['original_supplier_id'] = self.original_supplier_id
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
        o = AssetInfoCorrectionItem()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'change_reason' in d:
            o.change_reason = d['change_reason']
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'new_asset_value' in d:
            o.new_asset_value = d['new_asset_value']
        if 'new_item_id' in d:
            o.new_item_id = d['new_item_id']
        if 'original_asset_value' in d:
            o.original_asset_value = d['original_asset_value']
        if 'original_supplier_id' in d:
            o.original_supplier_id = d['original_supplier_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


