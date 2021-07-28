#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeadsOrderInfo(object):

    def __init__(self):
        self._biz_type = None
        self._camp_name = None
        self._channel = None
        self._contact_mobile = None
        self._contact_name = None
        self._create_time = None
        self._ext_info = None
        self._gift_name = None
        self._is_answer = None
        self._item_name = None
        self._memo = None
        self._reservation_record_id = None
        self._shop_city = None
        self._shop_name = None
        self._status = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def camp_name(self):
        return self._camp_name

    @camp_name.setter
    def camp_name(self, value):
        self._camp_name = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gift_name(self):
        return self._gift_name

    @gift_name.setter
    def gift_name(self, value):
        self._gift_name = value
    @property
    def is_answer(self):
        return self._is_answer

    @is_answer.setter
    def is_answer(self, value):
        self._is_answer = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def reservation_record_id(self):
        return self._reservation_record_id

    @reservation_record_id.setter
    def reservation_record_id(self, value):
        self._reservation_record_id = value
    @property
    def shop_city(self):
        return self._shop_city

    @shop_city.setter
    def shop_city(self, value):
        self._shop_city = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.camp_name:
            if hasattr(self.camp_name, 'to_alipay_dict'):
                params['camp_name'] = self.camp_name.to_alipay_dict()
            else:
                params['camp_name'] = self.camp_name
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gift_name:
            if hasattr(self.gift_name, 'to_alipay_dict'):
                params['gift_name'] = self.gift_name.to_alipay_dict()
            else:
                params['gift_name'] = self.gift_name
        if self.is_answer:
            if hasattr(self.is_answer, 'to_alipay_dict'):
                params['is_answer'] = self.is_answer.to_alipay_dict()
            else:
                params['is_answer'] = self.is_answer
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.reservation_record_id:
            if hasattr(self.reservation_record_id, 'to_alipay_dict'):
                params['reservation_record_id'] = self.reservation_record_id.to_alipay_dict()
            else:
                params['reservation_record_id'] = self.reservation_record_id
        if self.shop_city:
            if hasattr(self.shop_city, 'to_alipay_dict'):
                params['shop_city'] = self.shop_city.to_alipay_dict()
            else:
                params['shop_city'] = self.shop_city
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeadsOrderInfo()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'camp_name' in d:
            o.camp_name = d['camp_name']
        if 'channel' in d:
            o.channel = d['channel']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gift_name' in d:
            o.gift_name = d['gift_name']
        if 'is_answer' in d:
            o.is_answer = d['is_answer']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'reservation_record_id' in d:
            o.reservation_record_id = d['reservation_record_id']
        if 'shop_city' in d:
            o.shop_city = d['shop_city']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'status' in d:
            o.status = d['status']
        return o


