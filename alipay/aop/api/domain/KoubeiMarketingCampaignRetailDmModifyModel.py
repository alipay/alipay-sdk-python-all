#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignRetailDmModifyModel(object):

    def __init__(self):
        self._action_url = None
        self._activity_end_time = None
        self._activity_start_time = None
        self._brief = None
        self._campaign_end_time = None
        self._campaign_type = None
        self._content_id = None
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
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
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
    def thumbnail_image_id(self):
        return self._thumbnail_image_id

    @thumbnail_image_id.setter
    def thumbnail_image_id(self, value):
        self._thumbnail_image_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.activity_end_time:
            if hasattr(self.activity_end_time, 'to_alipay_dict'):
                params['activity_end_time'] = self.activity_end_time.to_alipay_dict()
            else:
                params['activity_end_time'] = self.activity_end_time
        if self.activity_start_time:
            if hasattr(self.activity_start_time, 'to_alipay_dict'):
                params['activity_start_time'] = self.activity_start_time.to_alipay_dict()
            else:
                params['activity_start_time'] = self.activity_start_time
        if self.brief:
            if hasattr(self.brief, 'to_alipay_dict'):
                params['brief'] = self.brief.to_alipay_dict()
            else:
                params['brief'] = self.brief
        if self.campaign_end_time:
            if hasattr(self.campaign_end_time, 'to_alipay_dict'):
                params['campaign_end_time'] = self.campaign_end_time.to_alipay_dict()
            else:
                params['campaign_end_time'] = self.campaign_end_time
        if self.campaign_type:
            if hasattr(self.campaign_type, 'to_alipay_dict'):
                params['campaign_type'] = self.campaign_type.to_alipay_dict()
            else:
                params['campaign_type'] = self.campaign_type
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.coupon_type:
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.item_brand:
            if hasattr(self.item_brand, 'to_alipay_dict'):
                params['item_brand'] = self.item_brand.to_alipay_dict()
            else:
                params['item_brand'] = self.item_brand
        if self.item_category:
            if hasattr(self.item_category, 'to_alipay_dict'):
                params['item_category'] = self.item_category.to_alipay_dict()
            else:
                params['item_category'] = self.item_category
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.member_only:
            if hasattr(self.member_only, 'to_alipay_dict'):
                params['member_only'] = self.member_only.to_alipay_dict()
            else:
                params['member_only'] = self.member_only
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
        if self.thumbnail_image_id:
            if hasattr(self.thumbnail_image_id, 'to_alipay_dict'):
                params['thumbnail_image_id'] = self.thumbnail_image_id.to_alipay_dict()
            else:
                params['thumbnail_image_id'] = self.thumbnail_image_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignRetailDmModifyModel()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'activity_end_time' in d:
            o.activity_end_time = d['activity_end_time']
        if 'activity_start_time' in d:
            o.activity_start_time = d['activity_start_time']
        if 'brief' in d:
            o.brief = d['brief']
        if 'campaign_end_time' in d:
            o.campaign_end_time = d['campaign_end_time']
        if 'campaign_type' in d:
            o.campaign_type = d['campaign_type']
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'description' in d:
            o.description = d['description']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'item_brand' in d:
            o.item_brand = d['item_brand']
        if 'item_category' in d:
            o.item_category = d['item_category']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'member_only' in d:
            o.member_only = d['member_only']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'thumbnail_image_id' in d:
            o.thumbnail_image_id = d['thumbnail_image_id']
        return o


