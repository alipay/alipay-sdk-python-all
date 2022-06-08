#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEntertainmentItemUploadModel(object):

    def __init__(self):
        self._biz_scene = None
        self._enable = None
        self._item_extended_info = None
        self._item_id = None
        self._item_name = None
        self._item_url = None
        self._pic_source_url = None
        self._pricing_type = None
        self._promote_point = None
        self._promote_price = None
        self._promote_price_mode = None
        self._remain_inventory = None
        self._rule_id = None
        self._service_category = None
        self._tags = None
        self._total_inventory = None
        self._unit_price = None
        self._valid_time_end = None
        self._valid_time_start = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def item_extended_info(self):
        return self._item_extended_info

    @item_extended_info.setter
    def item_extended_info(self, value):
        self._item_extended_info = value
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
    def item_url(self):
        return self._item_url

    @item_url.setter
    def item_url(self, value):
        self._item_url = value
    @property
    def pic_source_url(self):
        return self._pic_source_url

    @pic_source_url.setter
    def pic_source_url(self, value):
        self._pic_source_url = value
    @property
    def pricing_type(self):
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, value):
        self._pricing_type = value
    @property
    def promote_point(self):
        return self._promote_point

    @promote_point.setter
    def promote_point(self, value):
        self._promote_point = value
    @property
    def promote_price(self):
        return self._promote_price

    @promote_price.setter
    def promote_price(self, value):
        self._promote_price = value
    @property
    def promote_price_mode(self):
        return self._promote_price_mode

    @promote_price_mode.setter
    def promote_price_mode(self, value):
        self._promote_price_mode = value
    @property
    def remain_inventory(self):
        return self._remain_inventory

    @remain_inventory.setter
    def remain_inventory(self, value):
        self._remain_inventory = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def service_category(self):
        return self._service_category

    @service_category.setter
    def service_category(self, value):
        self._service_category = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def total_inventory(self):
        return self._total_inventory

    @total_inventory.setter
    def total_inventory(self, value):
        self._total_inventory = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value
    @property
    def valid_time_end(self):
        return self._valid_time_end

    @valid_time_end.setter
    def valid_time_end(self, value):
        self._valid_time_end = value
    @property
    def valid_time_start(self):
        return self._valid_time_start

    @valid_time_start.setter
    def valid_time_start(self, value):
        self._valid_time_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.item_extended_info:
            if hasattr(self.item_extended_info, 'to_alipay_dict'):
                params['item_extended_info'] = self.item_extended_info.to_alipay_dict()
            else:
                params['item_extended_info'] = self.item_extended_info
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
        if self.item_url:
            if hasattr(self.item_url, 'to_alipay_dict'):
                params['item_url'] = self.item_url.to_alipay_dict()
            else:
                params['item_url'] = self.item_url
        if self.pic_source_url:
            if hasattr(self.pic_source_url, 'to_alipay_dict'):
                params['pic_source_url'] = self.pic_source_url.to_alipay_dict()
            else:
                params['pic_source_url'] = self.pic_source_url
        if self.pricing_type:
            if hasattr(self.pricing_type, 'to_alipay_dict'):
                params['pricing_type'] = self.pricing_type.to_alipay_dict()
            else:
                params['pricing_type'] = self.pricing_type
        if self.promote_point:
            if hasattr(self.promote_point, 'to_alipay_dict'):
                params['promote_point'] = self.promote_point.to_alipay_dict()
            else:
                params['promote_point'] = self.promote_point
        if self.promote_price:
            if hasattr(self.promote_price, 'to_alipay_dict'):
                params['promote_price'] = self.promote_price.to_alipay_dict()
            else:
                params['promote_price'] = self.promote_price
        if self.promote_price_mode:
            if hasattr(self.promote_price_mode, 'to_alipay_dict'):
                params['promote_price_mode'] = self.promote_price_mode.to_alipay_dict()
            else:
                params['promote_price_mode'] = self.promote_price_mode
        if self.remain_inventory:
            if hasattr(self.remain_inventory, 'to_alipay_dict'):
                params['remain_inventory'] = self.remain_inventory.to_alipay_dict()
            else:
                params['remain_inventory'] = self.remain_inventory
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.service_category:
            if hasattr(self.service_category, 'to_alipay_dict'):
                params['service_category'] = self.service_category.to_alipay_dict()
            else:
                params['service_category'] = self.service_category
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.total_inventory:
            if hasattr(self.total_inventory, 'to_alipay_dict'):
                params['total_inventory'] = self.total_inventory.to_alipay_dict()
            else:
                params['total_inventory'] = self.total_inventory
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        if self.valid_time_end:
            if hasattr(self.valid_time_end, 'to_alipay_dict'):
                params['valid_time_end'] = self.valid_time_end.to_alipay_dict()
            else:
                params['valid_time_end'] = self.valid_time_end
        if self.valid_time_start:
            if hasattr(self.valid_time_start, 'to_alipay_dict'):
                params['valid_time_start'] = self.valid_time_start.to_alipay_dict()
            else:
                params['valid_time_start'] = self.valid_time_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEntertainmentItemUploadModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'enable' in d:
            o.enable = d['enable']
        if 'item_extended_info' in d:
            o.item_extended_info = d['item_extended_info']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_url' in d:
            o.item_url = d['item_url']
        if 'pic_source_url' in d:
            o.pic_source_url = d['pic_source_url']
        if 'pricing_type' in d:
            o.pricing_type = d['pricing_type']
        if 'promote_point' in d:
            o.promote_point = d['promote_point']
        if 'promote_price' in d:
            o.promote_price = d['promote_price']
        if 'promote_price_mode' in d:
            o.promote_price_mode = d['promote_price_mode']
        if 'remain_inventory' in d:
            o.remain_inventory = d['remain_inventory']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'service_category' in d:
            o.service_category = d['service_category']
        if 'tags' in d:
            o.tags = d['tags']
        if 'total_inventory' in d:
            o.total_inventory = d['total_inventory']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        if 'valid_time_end' in d:
            o.valid_time_end = d['valid_time_end']
        if 'valid_time_start' in d:
            o.valid_time_start = d['valid_time_start']
        return o


