#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherDescDetailModel import VoucherDescDetailModel


class DiscountInfo(object):

    def __init__(self):
        self._apply_condition = None
        self._buy_send_desc = None
        self._discount = None
        self._discount_notes = None
        self._distance = None
        self._end_time = None
        self._image_url = None
        self._item_id = None
        self._item_name = None
        self._label = None
        self._original_price = None
        self._per_price = None
        self._pid = None
        self._price = None
        self._reason = None
        self._send_item_name = None
        self._shop_id = None
        self._shop_name = None
        self._sold = None
        self._start_time = None
        self._threshold_price = None
        self._top_price = None
        self._type = None
        self._validity_period = None
        self._validity_period_range_from = None
        self._validity_period_range_to = None
        self._validity_period_type = None
        self._vol_type = None

    @property
    def apply_condition(self):
        return self._apply_condition

    @apply_condition.setter
    def apply_condition(self, value):
        self._apply_condition = value
    @property
    def buy_send_desc(self):
        return self._buy_send_desc

    @buy_send_desc.setter
    def buy_send_desc(self, value):
        self._buy_send_desc = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def discount_notes(self):
        return self._discount_notes

    @discount_notes.setter
    def discount_notes(self, value):
        if isinstance(value, list):
            self._discount_notes = list()
            for i in value:
                if isinstance(i, VoucherDescDetailModel):
                    self._discount_notes.append(i)
                else:
                    self._discount_notes.append(VoucherDescDetailModel.from_alipay_dict(i))
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
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
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def per_price(self):
        return self._per_price

    @per_price.setter
    def per_price(self, value):
        self._per_price = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def send_item_name(self):
        return self._send_item_name

    @send_item_name.setter
    def send_item_name(self, value):
        self._send_item_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def sold(self):
        return self._sold

    @sold.setter
    def sold(self, value):
        self._sold = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def threshold_price(self):
        return self._threshold_price

    @threshold_price.setter
    def threshold_price(self, value):
        self._threshold_price = value
    @property
    def top_price(self):
        return self._top_price

    @top_price.setter
    def top_price(self, value):
        self._top_price = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def validity_period(self):
        return self._validity_period

    @validity_period.setter
    def validity_period(self, value):
        self._validity_period = value
    @property
    def validity_period_range_from(self):
        return self._validity_period_range_from

    @validity_period_range_from.setter
    def validity_period_range_from(self, value):
        self._validity_period_range_from = value
    @property
    def validity_period_range_to(self):
        return self._validity_period_range_to

    @validity_period_range_to.setter
    def validity_period_range_to(self, value):
        self._validity_period_range_to = value
    @property
    def validity_period_type(self):
        return self._validity_period_type

    @validity_period_type.setter
    def validity_period_type(self, value):
        self._validity_period_type = value
    @property
    def vol_type(self):
        return self._vol_type

    @vol_type.setter
    def vol_type(self, value):
        self._vol_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_condition:
            if hasattr(self.apply_condition, 'to_alipay_dict'):
                params['apply_condition'] = self.apply_condition.to_alipay_dict()
            else:
                params['apply_condition'] = self.apply_condition
        if self.buy_send_desc:
            if hasattr(self.buy_send_desc, 'to_alipay_dict'):
                params['buy_send_desc'] = self.buy_send_desc.to_alipay_dict()
            else:
                params['buy_send_desc'] = self.buy_send_desc
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.discount_notes:
            if isinstance(self.discount_notes, list):
                for i in range(0, len(self.discount_notes)):
                    element = self.discount_notes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_notes[i] = element.to_alipay_dict()
            if hasattr(self.discount_notes, 'to_alipay_dict'):
                params['discount_notes'] = self.discount_notes.to_alipay_dict()
            else:
                params['discount_notes'] = self.discount_notes
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
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
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.per_price:
            if hasattr(self.per_price, 'to_alipay_dict'):
                params['per_price'] = self.per_price.to_alipay_dict()
            else:
                params['per_price'] = self.per_price
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.send_item_name:
            if hasattr(self.send_item_name, 'to_alipay_dict'):
                params['send_item_name'] = self.send_item_name.to_alipay_dict()
            else:
                params['send_item_name'] = self.send_item_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.sold:
            if hasattr(self.sold, 'to_alipay_dict'):
                params['sold'] = self.sold.to_alipay_dict()
            else:
                params['sold'] = self.sold
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.threshold_price:
            if hasattr(self.threshold_price, 'to_alipay_dict'):
                params['threshold_price'] = self.threshold_price.to_alipay_dict()
            else:
                params['threshold_price'] = self.threshold_price
        if self.top_price:
            if hasattr(self.top_price, 'to_alipay_dict'):
                params['top_price'] = self.top_price.to_alipay_dict()
            else:
                params['top_price'] = self.top_price
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.validity_period:
            if hasattr(self.validity_period, 'to_alipay_dict'):
                params['validity_period'] = self.validity_period.to_alipay_dict()
            else:
                params['validity_period'] = self.validity_period
        if self.validity_period_range_from:
            if hasattr(self.validity_period_range_from, 'to_alipay_dict'):
                params['validity_period_range_from'] = self.validity_period_range_from.to_alipay_dict()
            else:
                params['validity_period_range_from'] = self.validity_period_range_from
        if self.validity_period_range_to:
            if hasattr(self.validity_period_range_to, 'to_alipay_dict'):
                params['validity_period_range_to'] = self.validity_period_range_to.to_alipay_dict()
            else:
                params['validity_period_range_to'] = self.validity_period_range_to
        if self.validity_period_type:
            if hasattr(self.validity_period_type, 'to_alipay_dict'):
                params['validity_period_type'] = self.validity_period_type.to_alipay_dict()
            else:
                params['validity_period_type'] = self.validity_period_type
        if self.vol_type:
            if hasattr(self.vol_type, 'to_alipay_dict'):
                params['vol_type'] = self.vol_type.to_alipay_dict()
            else:
                params['vol_type'] = self.vol_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountInfo()
        if 'apply_condition' in d:
            o.apply_condition = d['apply_condition']
        if 'buy_send_desc' in d:
            o.buy_send_desc = d['buy_send_desc']
        if 'discount' in d:
            o.discount = d['discount']
        if 'discount_notes' in d:
            o.discount_notes = d['discount_notes']
        if 'distance' in d:
            o.distance = d['distance']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'label' in d:
            o.label = d['label']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'per_price' in d:
            o.per_price = d['per_price']
        if 'pid' in d:
            o.pid = d['pid']
        if 'price' in d:
            o.price = d['price']
        if 'reason' in d:
            o.reason = d['reason']
        if 'send_item_name' in d:
            o.send_item_name = d['send_item_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'sold' in d:
            o.sold = d['sold']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'threshold_price' in d:
            o.threshold_price = d['threshold_price']
        if 'top_price' in d:
            o.top_price = d['top_price']
        if 'type' in d:
            o.type = d['type']
        if 'validity_period' in d:
            o.validity_period = d['validity_period']
        if 'validity_period_range_from' in d:
            o.validity_period_range_from = d['validity_period_range_from']
        if 'validity_period_range_to' in d:
            o.validity_period_range_to = d['validity_period_range_to']
        if 'validity_period_type' in d:
            o.validity_period_type = d['validity_period_type']
        if 'vol_type' in d:
            o.vol_type = d['vol_type']
        return o


