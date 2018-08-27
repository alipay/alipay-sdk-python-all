#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignRetailDmQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignRetailDmQueryResponse, self).__init__()
        self._action_url = None
        self._activity_end_time = None
        self._activity_start_time = None
        self._brief = None
        self._campaign_end_time = None
        self._campaign_type = None
        self._coupon_type = None
        self._description = None
        self._ext_info = None
        self._image_id = None
        self._item_brand = None
        self._item_category = None
        self._item_code = None
        self._item_name = None
        self._member_only = None
        self._shop_ids = None
        self._status = None
        self._thumbnail_image_id = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def activity_end_time(self):
        return self._activity_end_time

    @activity_end_time.setter
    def activity_end_time(self, value):
        self._activity_end_time = value
    @property
    def activity_start_time(self):
        return self._activity_start_time

    @activity_start_time.setter
    def activity_start_time(self, value):
        self._activity_start_time = value
    @property
    def brief(self):
        return self._brief

    @brief.setter
    def brief(self, value):
        self._brief = value
    @property
    def campaign_end_time(self):
        return self._campaign_end_time

    @campaign_end_time.setter
    def campaign_end_time(self, value):
        self._campaign_end_time = value
    @property
    def campaign_type(self):
        return self._campaign_type

    @campaign_type.setter
    def campaign_type(self, value):
        self._campaign_type = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def item_brand(self):
        return self._item_brand

    @item_brand.setter
    def item_brand(self, value):
        self._item_brand = value
    @property
    def item_category(self):
        return self._item_category

    @item_category.setter
    def item_category(self, value):
        self._item_category = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def member_only(self):
        return self._member_only

    @member_only.setter
    def member_only(self, value):
        self._member_only = value
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def thumbnail_image_id(self):
        return self._thumbnail_image_id

    @thumbnail_image_id.setter
    def thumbnail_image_id(self, value):
        self._thumbnail_image_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignRetailDmQueryResponse, self).parse_response_content(response_content)
        if 'action_url' in response:
            self.action_url = response['action_url']
        if 'activity_end_time' in response:
            self.activity_end_time = response['activity_end_time']
        if 'activity_start_time' in response:
            self.activity_start_time = response['activity_start_time']
        if 'brief' in response:
            self.brief = response['brief']
        if 'campaign_end_time' in response:
            self.campaign_end_time = response['campaign_end_time']
        if 'campaign_type' in response:
            self.campaign_type = response['campaign_type']
        if 'coupon_type' in response:
            self.coupon_type = response['coupon_type']
        if 'description' in response:
            self.description = response['description']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'image_id' in response:
            self.image_id = response['image_id']
        if 'item_brand' in response:
            self.item_brand = response['item_brand']
        if 'item_category' in response:
            self.item_category = response['item_category']
        if 'item_code' in response:
            self.item_code = response['item_code']
        if 'item_name' in response:
            self.item_name = response['item_name']
        if 'member_only' in response:
            self.member_only = response['member_only']
        if 'shop_ids' in response:
            self.shop_ids = response['shop_ids']
        if 'status' in response:
            self.status = response['status']
        if 'thumbnail_image_id' in response:
            self.thumbnail_image_id = response['thumbnail_image_id']
