#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetReverseGoodsItem import AssetReverseGoodsItem
from alipay.aop.api.domain.AssetDeliveryAddress import AssetDeliveryAddress
from alipay.aop.api.domain.AssetDeliveryAddress import AssetDeliveryAddress


class AssetReverseItem(object):

    def __init__(self):
        self._action_type = None
        self._apply_order_id = None
        self._apply_order_item_id = None
        self._asset_reverse_goods_items = None
        self._assign_item_id = None
        self._biz_line = None
        self._biz_tag = None
        self._count = None
        self._from_address = None
        self._item_id = None
        self._item_name = None
        self._original_apply_order_id = None
        self._original_apply_order_item_id = None
        self._original_deliver_order_id = None
        self._original_deliver_order_item_id = None
        self._original_delivery_assign_item_id = None
        self._original_record_type = None
        self._ou_code = None
        self._ou_name = None
        self._reverse_apply_order_id = None
        self._reverse_apply_order_item_id = None
        self._reverse_type = None
        self._to_address = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def apply_order_item_id(self):
        return self._apply_order_item_id

    @apply_order_item_id.setter
    def apply_order_item_id(self, value):
        self._apply_order_item_id = value
    @property
    def asset_reverse_goods_items(self):
        return self._asset_reverse_goods_items

    @asset_reverse_goods_items.setter
    def asset_reverse_goods_items(self, value):
        if isinstance(value, AssetReverseGoodsItem):
            self._asset_reverse_goods_items = value
        else:
            self._asset_reverse_goods_items = AssetReverseGoodsItem.from_alipay_dict(value)
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def biz_line(self):
        return self._biz_line

    @biz_line.setter
    def biz_line(self, value):
        self._biz_line = value
    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def from_address(self):
        return self._from_address

    @from_address.setter
    def from_address(self, value):
        if isinstance(value, AssetDeliveryAddress):
            self._from_address = value
        else:
            self._from_address = AssetDeliveryAddress.from_alipay_dict(value)
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
    def original_apply_order_id(self):
        return self._original_apply_order_id

    @original_apply_order_id.setter
    def original_apply_order_id(self, value):
        self._original_apply_order_id = value
    @property
    def original_apply_order_item_id(self):
        return self._original_apply_order_item_id

    @original_apply_order_item_id.setter
    def original_apply_order_item_id(self, value):
        self._original_apply_order_item_id = value
    @property
    def original_deliver_order_id(self):
        return self._original_deliver_order_id

    @original_deliver_order_id.setter
    def original_deliver_order_id(self, value):
        self._original_deliver_order_id = value
    @property
    def original_deliver_order_item_id(self):
        return self._original_deliver_order_item_id

    @original_deliver_order_item_id.setter
    def original_deliver_order_item_id(self, value):
        self._original_deliver_order_item_id = value
    @property
    def original_delivery_assign_item_id(self):
        return self._original_delivery_assign_item_id

    @original_delivery_assign_item_id.setter
    def original_delivery_assign_item_id(self, value):
        self._original_delivery_assign_item_id = value
    @property
    def original_record_type(self):
        return self._original_record_type

    @original_record_type.setter
    def original_record_type(self, value):
        self._original_record_type = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def ou_name(self):
        return self._ou_name

    @ou_name.setter
    def ou_name(self, value):
        self._ou_name = value
    @property
    def reverse_apply_order_id(self):
        return self._reverse_apply_order_id

    @reverse_apply_order_id.setter
    def reverse_apply_order_id(self, value):
        self._reverse_apply_order_id = value
    @property
    def reverse_apply_order_item_id(self):
        return self._reverse_apply_order_item_id

    @reverse_apply_order_item_id.setter
    def reverse_apply_order_item_id(self, value):
        self._reverse_apply_order_item_id = value
    @property
    def reverse_type(self):
        return self._reverse_type

    @reverse_type.setter
    def reverse_type(self, value):
        self._reverse_type = value
    @property
    def to_address(self):
        return self._to_address

    @to_address.setter
    def to_address(self, value):
        if isinstance(value, AssetDeliveryAddress):
            self._to_address = value
        else:
            self._to_address = AssetDeliveryAddress.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        if self.apply_order_item_id:
            if hasattr(self.apply_order_item_id, 'to_alipay_dict'):
                params['apply_order_item_id'] = self.apply_order_item_id.to_alipay_dict()
            else:
                params['apply_order_item_id'] = self.apply_order_item_id
        if self.asset_reverse_goods_items:
            if hasattr(self.asset_reverse_goods_items, 'to_alipay_dict'):
                params['asset_reverse_goods_items'] = self.asset_reverse_goods_items.to_alipay_dict()
            else:
                params['asset_reverse_goods_items'] = self.asset_reverse_goods_items
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.biz_line:
            if hasattr(self.biz_line, 'to_alipay_dict'):
                params['biz_line'] = self.biz_line.to_alipay_dict()
            else:
                params['biz_line'] = self.biz_line
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.from_address:
            if hasattr(self.from_address, 'to_alipay_dict'):
                params['from_address'] = self.from_address.to_alipay_dict()
            else:
                params['from_address'] = self.from_address
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
        if self.original_apply_order_id:
            if hasattr(self.original_apply_order_id, 'to_alipay_dict'):
                params['original_apply_order_id'] = self.original_apply_order_id.to_alipay_dict()
            else:
                params['original_apply_order_id'] = self.original_apply_order_id
        if self.original_apply_order_item_id:
            if hasattr(self.original_apply_order_item_id, 'to_alipay_dict'):
                params['original_apply_order_item_id'] = self.original_apply_order_item_id.to_alipay_dict()
            else:
                params['original_apply_order_item_id'] = self.original_apply_order_item_id
        if self.original_deliver_order_id:
            if hasattr(self.original_deliver_order_id, 'to_alipay_dict'):
                params['original_deliver_order_id'] = self.original_deliver_order_id.to_alipay_dict()
            else:
                params['original_deliver_order_id'] = self.original_deliver_order_id
        if self.original_deliver_order_item_id:
            if hasattr(self.original_deliver_order_item_id, 'to_alipay_dict'):
                params['original_deliver_order_item_id'] = self.original_deliver_order_item_id.to_alipay_dict()
            else:
                params['original_deliver_order_item_id'] = self.original_deliver_order_item_id
        if self.original_delivery_assign_item_id:
            if hasattr(self.original_delivery_assign_item_id, 'to_alipay_dict'):
                params['original_delivery_assign_item_id'] = self.original_delivery_assign_item_id.to_alipay_dict()
            else:
                params['original_delivery_assign_item_id'] = self.original_delivery_assign_item_id
        if self.original_record_type:
            if hasattr(self.original_record_type, 'to_alipay_dict'):
                params['original_record_type'] = self.original_record_type.to_alipay_dict()
            else:
                params['original_record_type'] = self.original_record_type
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.ou_name:
            if hasattr(self.ou_name, 'to_alipay_dict'):
                params['ou_name'] = self.ou_name.to_alipay_dict()
            else:
                params['ou_name'] = self.ou_name
        if self.reverse_apply_order_id:
            if hasattr(self.reverse_apply_order_id, 'to_alipay_dict'):
                params['reverse_apply_order_id'] = self.reverse_apply_order_id.to_alipay_dict()
            else:
                params['reverse_apply_order_id'] = self.reverse_apply_order_id
        if self.reverse_apply_order_item_id:
            if hasattr(self.reverse_apply_order_item_id, 'to_alipay_dict'):
                params['reverse_apply_order_item_id'] = self.reverse_apply_order_item_id.to_alipay_dict()
            else:
                params['reverse_apply_order_item_id'] = self.reverse_apply_order_item_id
        if self.reverse_type:
            if hasattr(self.reverse_type, 'to_alipay_dict'):
                params['reverse_type'] = self.reverse_type.to_alipay_dict()
            else:
                params['reverse_type'] = self.reverse_type
        if self.to_address:
            if hasattr(self.to_address, 'to_alipay_dict'):
                params['to_address'] = self.to_address.to_alipay_dict()
            else:
                params['to_address'] = self.to_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetReverseItem()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        if 'apply_order_item_id' in d:
            o.apply_order_item_id = d['apply_order_item_id']
        if 'asset_reverse_goods_items' in d:
            o.asset_reverse_goods_items = d['asset_reverse_goods_items']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'biz_line' in d:
            o.biz_line = d['biz_line']
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'count' in d:
            o.count = d['count']
        if 'from_address' in d:
            o.from_address = d['from_address']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'original_apply_order_id' in d:
            o.original_apply_order_id = d['original_apply_order_id']
        if 'original_apply_order_item_id' in d:
            o.original_apply_order_item_id = d['original_apply_order_item_id']
        if 'original_deliver_order_id' in d:
            o.original_deliver_order_id = d['original_deliver_order_id']
        if 'original_deliver_order_item_id' in d:
            o.original_deliver_order_item_id = d['original_deliver_order_item_id']
        if 'original_delivery_assign_item_id' in d:
            o.original_delivery_assign_item_id = d['original_delivery_assign_item_id']
        if 'original_record_type' in d:
            o.original_record_type = d['original_record_type']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'ou_name' in d:
            o.ou_name = d['ou_name']
        if 'reverse_apply_order_id' in d:
            o.reverse_apply_order_id = d['reverse_apply_order_id']
        if 'reverse_apply_order_item_id' in d:
            o.reverse_apply_order_item_id = d['reverse_apply_order_item_id']
        if 'reverse_type' in d:
            o.reverse_type = d['reverse_type']
        if 'to_address' in d:
            o.to_address = d['to_address']
        return o


