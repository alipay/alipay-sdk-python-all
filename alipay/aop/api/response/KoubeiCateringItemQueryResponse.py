#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AvailablePeriodInfo import AvailablePeriodInfo
from alipay.aop.api.domain.BuyerNotesInfo import BuyerNotesInfo
from alipay.aop.api.domain.ItemDishInfo import ItemDishInfo
from alipay.aop.api.domain.ItemPackageInfo import ItemPackageInfo
from alipay.aop.api.domain.IntroductionInfo import IntroductionInfo
from alipay.aop.api.domain.UnavailablePeriodInfo import UnavailablePeriodInfo


class KoubeiCateringItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringItemQueryResponse, self).__init__()
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
        self._item_status = None
        self._latest_notice = None
        self._memo = None
        self._merchant_introduction = None
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
        if isinstance(value, list):
            self._buyer_notes = list()
            for i in value:
                if isinstance(i, BuyerNotesInfo):
                    self._buyer_notes.append(i)
                else:
                    self._buyer_notes.append(BuyerNotesInfo.from_alipay_dict(i))
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
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value
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

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringItemQueryResponse, self).parse_response_content(response_content)
        if 'available_periods' in response:
            self.available_periods = response['available_periods']
        if 'buyer_notes' in response:
            self.buyer_notes = response['buyer_notes']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'cover' in response:
            self.cover = response['cover']
        if 'external_code_inventory_id' in response:
            self.external_code_inventory_id = response['external_code_inventory_id']
        if 'external_code_template_id' in response:
            self.external_code_template_id = response['external_code_template_id']
        if 'gmt_end' in response:
            self.gmt_end = response['gmt_end']
        if 'gmt_start' in response:
            self.gmt_start = response['gmt_start']
        if 'inventory' in response:
            self.inventory = response['inventory']
        if 'item_dishes' in response:
            self.item_dishes = response['item_dishes']
        if 'item_display_channel' in response:
            self.item_display_channel = response['item_display_channel']
        if 'item_id' in response:
            self.item_id = response['item_id']
        if 'item_packages' in response:
            self.item_packages = response['item_packages']
        if 'item_status' in response:
            self.item_status = response['item_status']
        if 'latest_notice' in response:
            self.latest_notice = response['latest_notice']
        if 'memo' in response:
            self.memo = response['memo']
        if 'merchant_introduction' in response:
            self.merchant_introduction = response['merchant_introduction']
        if 'original_price' in response:
            self.original_price = response['original_price']
        if 'package_notes' in response:
            self.package_notes = response['package_notes']
        if 'picture_details' in response:
            self.picture_details = response['picture_details']
        if 'price' in response:
            self.price = response['price']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'shop_ids' in response:
            self.shop_ids = response['shop_ids']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
        if 'subject' in response:
            self.subject = response['subject']
        if 'taobao_cover_image' in response:
            self.taobao_cover_image = response['taobao_cover_image']
        if 'ticket_display_mode' in response:
            self.ticket_display_mode = response['ticket_display_mode']
        if 'unavailable_periods' in response:
            self.unavailable_periods = response['unavailable_periods']
        if 'validity_period' in response:
            self.validity_period = response['validity_period']
        if 'weight' in response:
            self.weight = response['weight']
