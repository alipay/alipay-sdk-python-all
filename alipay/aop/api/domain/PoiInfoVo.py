#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PoiInfoVo(object):

    def __init__(self):
        self._address = None
        self._audio_text = None
        self._audio_url = None
        self._avatar = None
        self._buy_url = None
        self._description = None
        self._distance = None
        self._img_list = None
        self._item_id = None
        self._latitude = None
        self._longitude = None
        self._meters = None
        self._photo_suggest_image_list = None
        self._photo_suggest_text = None
        self._poi_type = None
        self._related_merchant_list = None
        self._related_ticket_list = None
        self._tags = None
        self._title = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def audio_text(self):
        return self._audio_text

    @audio_text.setter
    def audio_text(self, value):
        self._audio_text = value
    @property
    def audio_url(self):
        return self._audio_url

    @audio_url.setter
    def audio_url(self, value):
        self._audio_url = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def buy_url(self):
        return self._buy_url

    @buy_url.setter
    def buy_url(self, value):
        self._buy_url = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def img_list(self):
        return self._img_list

    @img_list.setter
    def img_list(self, value):
        if isinstance(value, list):
            self._img_list = list()
            for i in value:
                self._img_list.append(i)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, value):
        self._meters = value
    @property
    def photo_suggest_image_list(self):
        return self._photo_suggest_image_list

    @photo_suggest_image_list.setter
    def photo_suggest_image_list(self, value):
        if isinstance(value, list):
            self._photo_suggest_image_list = list()
            for i in value:
                self._photo_suggest_image_list.append(i)
    @property
    def photo_suggest_text(self):
        return self._photo_suggest_text

    @photo_suggest_text.setter
    def photo_suggest_text(self, value):
        self._photo_suggest_text = value
    @property
    def poi_type(self):
        return self._poi_type

    @poi_type.setter
    def poi_type(self, value):
        self._poi_type = value
    @property
    def related_merchant_list(self):
        return self._related_merchant_list

    @related_merchant_list.setter
    def related_merchant_list(self, value):
        if isinstance(value, list):
            self._related_merchant_list = list()
            for i in value:
                self._related_merchant_list.append(i)
    @property
    def related_ticket_list(self):
        return self._related_ticket_list

    @related_ticket_list.setter
    def related_ticket_list(self, value):
        if isinstance(value, list):
            self._related_ticket_list = list()
            for i in value:
                self._related_ticket_list.append(i)
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.audio_text:
            if hasattr(self.audio_text, 'to_alipay_dict'):
                params['audio_text'] = self.audio_text.to_alipay_dict()
            else:
                params['audio_text'] = self.audio_text
        if self.audio_url:
            if hasattr(self.audio_url, 'to_alipay_dict'):
                params['audio_url'] = self.audio_url.to_alipay_dict()
            else:
                params['audio_url'] = self.audio_url
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.buy_url:
            if hasattr(self.buy_url, 'to_alipay_dict'):
                params['buy_url'] = self.buy_url.to_alipay_dict()
            else:
                params['buy_url'] = self.buy_url
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.img_list:
            if isinstance(self.img_list, list):
                for i in range(0, len(self.img_list)):
                    element = self.img_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.img_list[i] = element.to_alipay_dict()
            if hasattr(self.img_list, 'to_alipay_dict'):
                params['img_list'] = self.img_list.to_alipay_dict()
            else:
                params['img_list'] = self.img_list
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.meters:
            if hasattr(self.meters, 'to_alipay_dict'):
                params['meters'] = self.meters.to_alipay_dict()
            else:
                params['meters'] = self.meters
        if self.photo_suggest_image_list:
            if isinstance(self.photo_suggest_image_list, list):
                for i in range(0, len(self.photo_suggest_image_list)):
                    element = self.photo_suggest_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.photo_suggest_image_list[i] = element.to_alipay_dict()
            if hasattr(self.photo_suggest_image_list, 'to_alipay_dict'):
                params['photo_suggest_image_list'] = self.photo_suggest_image_list.to_alipay_dict()
            else:
                params['photo_suggest_image_list'] = self.photo_suggest_image_list
        if self.photo_suggest_text:
            if hasattr(self.photo_suggest_text, 'to_alipay_dict'):
                params['photo_suggest_text'] = self.photo_suggest_text.to_alipay_dict()
            else:
                params['photo_suggest_text'] = self.photo_suggest_text
        if self.poi_type:
            if hasattr(self.poi_type, 'to_alipay_dict'):
                params['poi_type'] = self.poi_type.to_alipay_dict()
            else:
                params['poi_type'] = self.poi_type
        if self.related_merchant_list:
            if isinstance(self.related_merchant_list, list):
                for i in range(0, len(self.related_merchant_list)):
                    element = self.related_merchant_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_merchant_list[i] = element.to_alipay_dict()
            if hasattr(self.related_merchant_list, 'to_alipay_dict'):
                params['related_merchant_list'] = self.related_merchant_list.to_alipay_dict()
            else:
                params['related_merchant_list'] = self.related_merchant_list
        if self.related_ticket_list:
            if isinstance(self.related_ticket_list, list):
                for i in range(0, len(self.related_ticket_list)):
                    element = self.related_ticket_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_ticket_list[i] = element.to_alipay_dict()
            if hasattr(self.related_ticket_list, 'to_alipay_dict'):
                params['related_ticket_list'] = self.related_ticket_list.to_alipay_dict()
            else:
                params['related_ticket_list'] = self.related_ticket_list
        if self.tags:
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoiInfoVo()
        if 'address' in d:
            o.address = d['address']
        if 'audio_text' in d:
            o.audio_text = d['audio_text']
        if 'audio_url' in d:
            o.audio_url = d['audio_url']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'buy_url' in d:
            o.buy_url = d['buy_url']
        if 'description' in d:
            o.description = d['description']
        if 'distance' in d:
            o.distance = d['distance']
        if 'img_list' in d:
            o.img_list = d['img_list']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'meters' in d:
            o.meters = d['meters']
        if 'photo_suggest_image_list' in d:
            o.photo_suggest_image_list = d['photo_suggest_image_list']
        if 'photo_suggest_text' in d:
            o.photo_suggest_text = d['photo_suggest_text']
        if 'poi_type' in d:
            o.poi_type = d['poi_type']
        if 'related_merchant_list' in d:
            o.related_merchant_list = d['related_merchant_list']
        if 'related_ticket_list' in d:
            o.related_ticket_list = d['related_ticket_list']
        if 'tags' in d:
            o.tags = d['tags']
        if 'title' in d:
            o.title = d['title']
        return o


