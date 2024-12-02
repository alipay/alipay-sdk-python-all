#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChinaMobileVerificationSyncData(object):

    def __init__(self):
        self._channel_order_id = None
        self._comment = None
        self._coupon = None
        self._create_time = None
        self._discount_amount = None
        self._mid = None
        self._order_item_id = None
        self._phone = None
        self._real_amount = None
        self._retain = None
        self._sku_id = None
        self._source = None
        self._status = None
        self._store_id = None
        self._total_amount = None
        self._verification_id = None
        self._verification_skucode = None

    @property
    def channel_order_id(self):
        return self._channel_order_id

    @channel_order_id.setter
    def channel_order_id(self, value):
        self._channel_order_id = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def coupon(self):
        return self._coupon

    @coupon.setter
    def coupon(self, value):
        self._coupon = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def order_item_id(self):
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, value):
        self._order_item_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def retain(self):
        return self._retain

    @retain.setter
    def retain(self, value):
        self._retain = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def verification_id(self):
        return self._verification_id

    @verification_id.setter
    def verification_id(self, value):
        self._verification_id = value
    @property
    def verification_skucode(self):
        return self._verification_skucode

    @verification_skucode.setter
    def verification_skucode(self, value):
        self._verification_skucode = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_order_id:
            if hasattr(self.channel_order_id, 'to_alipay_dict'):
                params['channel_order_id'] = self.channel_order_id.to_alipay_dict()
            else:
                params['channel_order_id'] = self.channel_order_id
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.coupon:
            if hasattr(self.coupon, 'to_alipay_dict'):
                params['coupon'] = self.coupon.to_alipay_dict()
            else:
                params['coupon'] = self.coupon
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.order_item_id:
            if hasattr(self.order_item_id, 'to_alipay_dict'):
                params['order_item_id'] = self.order_item_id.to_alipay_dict()
            else:
                params['order_item_id'] = self.order_item_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.retain:
            if hasattr(self.retain, 'to_alipay_dict'):
                params['retain'] = self.retain.to_alipay_dict()
            else:
                params['retain'] = self.retain
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.verification_id:
            if hasattr(self.verification_id, 'to_alipay_dict'):
                params['verification_id'] = self.verification_id.to_alipay_dict()
            else:
                params['verification_id'] = self.verification_id
        if self.verification_skucode:
            if hasattr(self.verification_skucode, 'to_alipay_dict'):
                params['verification_skucode'] = self.verification_skucode.to_alipay_dict()
            else:
                params['verification_skucode'] = self.verification_skucode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChinaMobileVerificationSyncData()
        if 'channel_order_id' in d:
            o.channel_order_id = d['channel_order_id']
        if 'comment' in d:
            o.comment = d['comment']
        if 'coupon' in d:
            o.coupon = d['coupon']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'mid' in d:
            o.mid = d['mid']
        if 'order_item_id' in d:
            o.order_item_id = d['order_item_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'retain' in d:
            o.retain = d['retain']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'verification_id' in d:
            o.verification_id = d['verification_id']
        if 'verification_skucode' in d:
            o.verification_skucode = d['verification_skucode']
        return o


