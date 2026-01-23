#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreightFlowOrderSupInfo(object):

    def __init__(self):
        self._buyer_cell_phone = None
        self._buyer_city = None
        self._buyer_name = None
        self._buyer_province = None
        self._deliver_time = None
        self._goods_name = None
        self._order_time = None
        self._receive_time = None
        self._seller_card_no = None
        self._seller_cell_phone = None
        self._seller_city = None
        self._seller_name = None
        self._seller_out_id = None
        self._seller_province = None

    @property
    def buyer_cell_phone(self):
        return self._buyer_cell_phone

    @buyer_cell_phone.setter
    def buyer_cell_phone(self, value):
        self._buyer_cell_phone = value
    @property
    def buyer_city(self):
        return self._buyer_city

    @buyer_city.setter
    def buyer_city(self, value):
        self._buyer_city = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_province(self):
        return self._buyer_province

    @buyer_province.setter
    def buyer_province(self, value):
        self._buyer_province = value
    @property
    def deliver_time(self):
        return self._deliver_time

    @deliver_time.setter
    def deliver_time(self, value):
        self._deliver_time = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def seller_card_no(self):
        return self._seller_card_no

    @seller_card_no.setter
    def seller_card_no(self, value):
        self._seller_card_no = value
    @property
    def seller_cell_phone(self):
        return self._seller_cell_phone

    @seller_cell_phone.setter
    def seller_cell_phone(self, value):
        self._seller_cell_phone = value
    @property
    def seller_city(self):
        return self._seller_city

    @seller_city.setter
    def seller_city(self, value):
        self._seller_city = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_out_id(self):
        return self._seller_out_id

    @seller_out_id.setter
    def seller_out_id(self, value):
        self._seller_out_id = value
    @property
    def seller_province(self):
        return self._seller_province

    @seller_province.setter
    def seller_province(self, value):
        self._seller_province = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_cell_phone:
            if hasattr(self.buyer_cell_phone, 'to_alipay_dict'):
                params['buyer_cell_phone'] = self.buyer_cell_phone.to_alipay_dict()
            else:
                params['buyer_cell_phone'] = self.buyer_cell_phone
        if self.buyer_city:
            if hasattr(self.buyer_city, 'to_alipay_dict'):
                params['buyer_city'] = self.buyer_city.to_alipay_dict()
            else:
                params['buyer_city'] = self.buyer_city
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_province:
            if hasattr(self.buyer_province, 'to_alipay_dict'):
                params['buyer_province'] = self.buyer_province.to_alipay_dict()
            else:
                params['buyer_province'] = self.buyer_province
        if self.deliver_time:
            if hasattr(self.deliver_time, 'to_alipay_dict'):
                params['deliver_time'] = self.deliver_time.to_alipay_dict()
            else:
                params['deliver_time'] = self.deliver_time
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.receive_time:
            if hasattr(self.receive_time, 'to_alipay_dict'):
                params['receive_time'] = self.receive_time.to_alipay_dict()
            else:
                params['receive_time'] = self.receive_time
        if self.seller_card_no:
            if hasattr(self.seller_card_no, 'to_alipay_dict'):
                params['seller_card_no'] = self.seller_card_no.to_alipay_dict()
            else:
                params['seller_card_no'] = self.seller_card_no
        if self.seller_cell_phone:
            if hasattr(self.seller_cell_phone, 'to_alipay_dict'):
                params['seller_cell_phone'] = self.seller_cell_phone.to_alipay_dict()
            else:
                params['seller_cell_phone'] = self.seller_cell_phone
        if self.seller_city:
            if hasattr(self.seller_city, 'to_alipay_dict'):
                params['seller_city'] = self.seller_city.to_alipay_dict()
            else:
                params['seller_city'] = self.seller_city
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.seller_out_id:
            if hasattr(self.seller_out_id, 'to_alipay_dict'):
                params['seller_out_id'] = self.seller_out_id.to_alipay_dict()
            else:
                params['seller_out_id'] = self.seller_out_id
        if self.seller_province:
            if hasattr(self.seller_province, 'to_alipay_dict'):
                params['seller_province'] = self.seller_province.to_alipay_dict()
            else:
                params['seller_province'] = self.seller_province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreightFlowOrderSupInfo()
        if 'buyer_cell_phone' in d:
            o.buyer_cell_phone = d['buyer_cell_phone']
        if 'buyer_city' in d:
            o.buyer_city = d['buyer_city']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_province' in d:
            o.buyer_province = d['buyer_province']
        if 'deliver_time' in d:
            o.deliver_time = d['deliver_time']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'receive_time' in d:
            o.receive_time = d['receive_time']
        if 'seller_card_no' in d:
            o.seller_card_no = d['seller_card_no']
        if 'seller_cell_phone' in d:
            o.seller_cell_phone = d['seller_cell_phone']
        if 'seller_city' in d:
            o.seller_city = d['seller_city']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'seller_out_id' in d:
            o.seller_out_id = d['seller_out_id']
        if 'seller_province' in d:
            o.seller_province = d['seller_province']
        return o


