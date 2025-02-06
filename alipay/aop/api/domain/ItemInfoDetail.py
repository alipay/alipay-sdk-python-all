#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuInfoVO import SkuInfoVO


class ItemInfoDetail(object):

    def __init__(self):
        self._create_time = None
        self._insurance_status = None
        self._item_code = None
        self._item_id = None
        self._item_name = None
        self._item_status = None
        self._parent_tag_code = None
        self._parent_tag_id = None
        self._parent_tag_name = None
        self._sku_info_list = None
        self._tag_code = None
        self._tag_id = None
        self._tag_name = None
        self._update_time = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def insurance_status(self):
        return self._insurance_status

    @insurance_status.setter
    def insurance_status(self, value):
        self._insurance_status = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
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
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
    @property
    def parent_tag_code(self):
        return self._parent_tag_code

    @parent_tag_code.setter
    def parent_tag_code(self, value):
        self._parent_tag_code = value
    @property
    def parent_tag_id(self):
        return self._parent_tag_id

    @parent_tag_id.setter
    def parent_tag_id(self, value):
        self._parent_tag_id = value
    @property
    def parent_tag_name(self):
        return self._parent_tag_name

    @parent_tag_name.setter
    def parent_tag_name(self, value):
        self._parent_tag_name = value
    @property
    def sku_info_list(self):
        return self._sku_info_list

    @sku_info_list.setter
    def sku_info_list(self, value):
        if isinstance(value, SkuInfoVO):
            self._sku_info_list = value
        else:
            self._sku_info_list = SkuInfoVO.from_alipay_dict(value)
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.insurance_status:
            if hasattr(self.insurance_status, 'to_alipay_dict'):
                params['insurance_status'] = self.insurance_status.to_alipay_dict()
            else:
                params['insurance_status'] = self.insurance_status
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
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
        if self.item_status:
            if hasattr(self.item_status, 'to_alipay_dict'):
                params['item_status'] = self.item_status.to_alipay_dict()
            else:
                params['item_status'] = self.item_status
        if self.parent_tag_code:
            if hasattr(self.parent_tag_code, 'to_alipay_dict'):
                params['parent_tag_code'] = self.parent_tag_code.to_alipay_dict()
            else:
                params['parent_tag_code'] = self.parent_tag_code
        if self.parent_tag_id:
            if hasattr(self.parent_tag_id, 'to_alipay_dict'):
                params['parent_tag_id'] = self.parent_tag_id.to_alipay_dict()
            else:
                params['parent_tag_id'] = self.parent_tag_id
        if self.parent_tag_name:
            if hasattr(self.parent_tag_name, 'to_alipay_dict'):
                params['parent_tag_name'] = self.parent_tag_name.to_alipay_dict()
            else:
                params['parent_tag_name'] = self.parent_tag_name
        if self.sku_info_list:
            if hasattr(self.sku_info_list, 'to_alipay_dict'):
                params['sku_info_list'] = self.sku_info_list.to_alipay_dict()
            else:
                params['sku_info_list'] = self.sku_info_list
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemInfoDetail()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'insurance_status' in d:
            o.insurance_status = d['insurance_status']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_status' in d:
            o.item_status = d['item_status']
        if 'parent_tag_code' in d:
            o.parent_tag_code = d['parent_tag_code']
        if 'parent_tag_id' in d:
            o.parent_tag_id = d['parent_tag_id']
        if 'parent_tag_name' in d:
            o.parent_tag_name = d['parent_tag_name']
        if 'sku_info_list' in d:
            o.sku_info_list = d['sku_info_list']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


