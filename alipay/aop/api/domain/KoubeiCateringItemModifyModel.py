#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AvailablePeriodInfo import AvailablePeriodInfo
from alipay.aop.api.domain.BuyerNotesInfo import BuyerNotesInfo
from alipay.aop.api.domain.ItemDishInfo import ItemDishInfo
from alipay.aop.api.domain.ItemPackageInfo import ItemPackageInfo
from alipay.aop.api.domain.IntroductionInfo import IntroductionInfo
from alipay.aop.api.domain.UnavailablePeriodInfo import UnavailablePeriodInfo


class KoubeiCateringItemModifyModel(object):

    def __init__(self):
        self._auth_code = None
        self._available_periods = None
        self._buyer_notes = None
        self._category_id = None
        self._cover = None
        self._external_code_inventory_id = None
        self._external_code_template_id = None
        self._gmt_end = None
        self._gmt_start = None
        self._inventory = None
        self._item_dishes = None
        self._item_display_channel = None
        self._item_id = None
        self._item_packages = None
        self._latest_notice = None
        self._memo = None
        self._merchant_introduction = None
        self._operator_type = None
        self._original_price = None
        self._package_notes = None
        self._picture_details = None
        self._price = None
        self._request_id = None
        self._shop_ids = None
        self._sku_id = None
        self._subject = None
        self._taobao_cover_image = None
        self._ticket_display_mode = None
        self._unavailable_periods = None
        self._validity_period = None
        self._weight = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def available_periods(self):
        return self._available_periods

    @available_periods.setter
    def available_periods(self, value):
        if isinstance(value, list):
            self._available_periods = list()
            for i in value:
                if isinstance(i, AvailablePeriodInfo):
                    self._available_periods.append(i)
                else:
                    self._available_periods.append(AvailablePeriodInfo.from_alipay_dict(i))
    @property
    def buyer_notes(self):
        return self._buyer_notes

    @buyer_notes.setter
    def buyer_notes(self, value):
        if isinstance(value, BuyerNotesInfo):
            self._buyer_notes = value
        else:
            self._buyer_notes = BuyerNotesInfo.from_alipay_dict(value)
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def external_code_inventory_id(self):
        return self._external_code_inventory_id

    @external_code_inventory_id.setter
    def external_code_inventory_id(self, value):
        self._external_code_inventory_id = value
    @property
    def external_code_template_id(self):
        return self._external_code_template_id

    @external_code_template_id.setter
    def external_code_template_id(self, value):
        self._external_code_template_id = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def item_dishes(self):
        return self._item_dishes

    @item_dishes.setter
    def item_dishes(self, value):
        if isinstance(value, list):
            self._item_dishes = list()
            for i in value:
                if isinstance(i, ItemDishInfo):
                    self._item_dishes.append(i)
                else:
                    self._item_dishes.append(ItemDishInfo.from_alipay_dict(i))
    @property
    def item_display_channel(self):
        return self._item_display_channel

    @item_display_channel.setter
    def item_display_channel(self, value):
        self._item_display_channel = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_packages(self):
        return self._item_packages

    @item_packages.setter
    def item_packages(self, value):
        if isinstance(value, list):
            self._item_packages = list()
            for i in value:
                if isinstance(i, ItemPackageInfo):
                    self._item_packages.append(i)
                else:
                    self._item_packages.append(ItemPackageInfo.from_alipay_dict(i))
    @property
    def latest_notice(self):
        return self._latest_notice

    @latest_notice.setter
    def latest_notice(self, value):
        self._latest_notice = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_introduction(self):
        return self._merchant_introduction

    @merchant_introduction.setter
    def merchant_introduction(self, value):
        if isinstance(value, IntroductionInfo):
            self._merchant_introduction = value
        else:
            self._merchant_introduction = IntroductionInfo.from_alipay_dict(value)
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def package_notes(self):
        return self._package_notes

    @package_notes.setter
    def package_notes(self, value):
        if isinstance(value, list):
            self._package_notes = list()
            for i in value:
                self._package_notes.append(i)
    @property
    def picture_details(self):
        return self._picture_details

    @picture_details.setter
    def picture_details(self, value):
        if isinstance(value, list):
            self._picture_details = list()
            for i in value:
                self._picture_details.append(i)
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def taobao_cover_image(self):
        return self._taobao_cover_image

    @taobao_cover_image.setter
    def taobao_cover_image(self, value):
        self._taobao_cover_image = value
    @property
    def ticket_display_mode(self):
        return self._ticket_display_mode

    @ticket_display_mode.setter
    def ticket_display_mode(self, value):
        self._ticket_display_mode = value
    @property
    def unavailable_periods(self):
        return self._unavailable_periods

    @unavailable_periods.setter
    def unavailable_periods(self, value):
        if isinstance(value, list):
            self._unavailable_periods = list()
            for i in value:
                if isinstance(i, UnavailablePeriodInfo):
                    self._unavailable_periods.append(i)
                else:
                    self._unavailable_periods.append(UnavailablePeriodInfo.from_alipay_dict(i))
    @property
    def validity_period(self):
        return self._validity_period

    @validity_period.setter
    def validity_period(self, value):
        self._validity_period = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.available_periods:
            if isinstance(self.available_periods, list):
                for i in range(0, len(self.available_periods)):
                    element = self.available_periods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_periods[i] = element.to_alipay_dict()
            if hasattr(self.available_periods, 'to_alipay_dict'):
                params['available_periods'] = self.available_periods.to_alipay_dict()
            else:
                params['available_periods'] = self.available_periods
        if self.buyer_notes:
            if hasattr(self.buyer_notes, 'to_alipay_dict'):
                params['buyer_notes'] = self.buyer_notes.to_alipay_dict()
            else:
                params['buyer_notes'] = self.buyer_notes
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.external_code_inventory_id:
            if hasattr(self.external_code_inventory_id, 'to_alipay_dict'):
                params['external_code_inventory_id'] = self.external_code_inventory_id.to_alipay_dict()
            else:
                params['external_code_inventory_id'] = self.external_code_inventory_id
        if self.external_code_template_id:
            if hasattr(self.external_code_template_id, 'to_alipay_dict'):
                params['external_code_template_id'] = self.external_code_template_id.to_alipay_dict()
            else:
                params['external_code_template_id'] = self.external_code_template_id
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_dishes:
            if isinstance(self.item_dishes, list):
                for i in range(0, len(self.item_dishes)):
                    element = self.item_dishes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_dishes[i] = element.to_alipay_dict()
            if hasattr(self.item_dishes, 'to_alipay_dict'):
                params['item_dishes'] = self.item_dishes.to_alipay_dict()
            else:
                params['item_dishes'] = self.item_dishes
        if self.item_display_channel:
            if hasattr(self.item_display_channel, 'to_alipay_dict'):
                params['item_display_channel'] = self.item_display_channel.to_alipay_dict()
            else:
                params['item_display_channel'] = self.item_display_channel
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_packages:
            if isinstance(self.item_packages, list):
                for i in range(0, len(self.item_packages)):
                    element = self.item_packages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_packages[i] = element.to_alipay_dict()
            if hasattr(self.item_packages, 'to_alipay_dict'):
                params['item_packages'] = self.item_packages.to_alipay_dict()
            else:
                params['item_packages'] = self.item_packages
        if self.latest_notice:
            if hasattr(self.latest_notice, 'to_alipay_dict'):
                params['latest_notice'] = self.latest_notice.to_alipay_dict()
            else:
                params['latest_notice'] = self.latest_notice
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_introduction:
            if hasattr(self.merchant_introduction, 'to_alipay_dict'):
                params['merchant_introduction'] = self.merchant_introduction.to_alipay_dict()
            else:
                params['merchant_introduction'] = self.merchant_introduction
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.package_notes:
            if isinstance(self.package_notes, list):
                for i in range(0, len(self.package_notes)):
                    element = self.package_notes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.package_notes[i] = element.to_alipay_dict()
            if hasattr(self.package_notes, 'to_alipay_dict'):
                params['package_notes'] = self.package_notes.to_alipay_dict()
            else:
                params['package_notes'] = self.package_notes
        if self.picture_details:
            if isinstance(self.picture_details, list):
                for i in range(0, len(self.picture_details)):
                    element = self.picture_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_details[i] = element.to_alipay_dict()
            if hasattr(self.picture_details, 'to_alipay_dict'):
                params['picture_details'] = self.picture_details.to_alipay_dict()
            else:
                params['picture_details'] = self.picture_details
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.taobao_cover_image:
            if hasattr(self.taobao_cover_image, 'to_alipay_dict'):
                params['taobao_cover_image'] = self.taobao_cover_image.to_alipay_dict()
            else:
                params['taobao_cover_image'] = self.taobao_cover_image
        if self.ticket_display_mode:
            if hasattr(self.ticket_display_mode, 'to_alipay_dict'):
                params['ticket_display_mode'] = self.ticket_display_mode.to_alipay_dict()
            else:
                params['ticket_display_mode'] = self.ticket_display_mode
        if self.unavailable_periods:
            if isinstance(self.unavailable_periods, list):
                for i in range(0, len(self.unavailable_periods)):
                    element = self.unavailable_periods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unavailable_periods[i] = element.to_alipay_dict()
            if hasattr(self.unavailable_periods, 'to_alipay_dict'):
                params['unavailable_periods'] = self.unavailable_periods.to_alipay_dict()
            else:
                params['unavailable_periods'] = self.unavailable_periods
        if self.validity_period:
            if hasattr(self.validity_period, 'to_alipay_dict'):
                params['validity_period'] = self.validity_period.to_alipay_dict()
            else:
                params['validity_period'] = self.validity_period
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringItemModifyModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'available_periods' in d:
            o.available_periods = d['available_periods']
        if 'buyer_notes' in d:
            o.buyer_notes = d['buyer_notes']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'cover' in d:
            o.cover = d['cover']
        if 'external_code_inventory_id' in d:
            o.external_code_inventory_id = d['external_code_inventory_id']
        if 'external_code_template_id' in d:
            o.external_code_template_id = d['external_code_template_id']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_dishes' in d:
            o.item_dishes = d['item_dishes']
        if 'item_display_channel' in d:
            o.item_display_channel = d['item_display_channel']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_packages' in d:
            o.item_packages = d['item_packages']
        if 'latest_notice' in d:
            o.latest_notice = d['latest_notice']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_introduction' in d:
            o.merchant_introduction = d['merchant_introduction']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'package_notes' in d:
            o.package_notes = d['package_notes']
        if 'picture_details' in d:
            o.picture_details = d['picture_details']
        if 'price' in d:
            o.price = d['price']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'taobao_cover_image' in d:
            o.taobao_cover_image = d['taobao_cover_image']
        if 'ticket_display_mode' in d:
            o.ticket_display_mode = d['ticket_display_mode']
        if 'unavailable_periods' in d:
            o.unavailable_periods = d['unavailable_periods']
        if 'validity_period' in d:
            o.validity_period = d['validity_period']
        if 'weight' in d:
            o.weight = d['weight']
        return o


