#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentDistorderSendModel(object):

    def __init__(self):
        self._biz_order_id = None
        self._channel_buyer_id = None
        self._channel_order_id = None
        self._delivery_id = None
        self._distribution_channel = None
        self._sender_address = None
        self._sender_district_code = None
        self._sender_name = None
        self._sender_phone = None
        self._waybill_id = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def channel_buyer_id(self):
        return self._channel_buyer_id

    @channel_buyer_id.setter
    def channel_buyer_id(self, value):
        self._channel_buyer_id = value
    @property
    def channel_order_id(self):
        return self._channel_order_id

    @channel_order_id.setter
    def channel_order_id(self, value):
        self._channel_order_id = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def distribution_channel(self):
        return self._distribution_channel

    @distribution_channel.setter
    def distribution_channel(self, value):
        self._distribution_channel = value
    @property
    def sender_address(self):
        return self._sender_address

    @sender_address.setter
    def sender_address(self, value):
        self._sender_address = value
    @property
    def sender_district_code(self):
        return self._sender_district_code

    @sender_district_code.setter
    def sender_district_code(self, value):
        self._sender_district_code = value
    @property
    def sender_name(self):
        return self._sender_name

    @sender_name.setter
    def sender_name(self, value):
        self._sender_name = value
    @property
    def sender_phone(self):
        return self._sender_phone

    @sender_phone.setter
    def sender_phone(self, value):
        self._sender_phone = value
    @property
    def waybill_id(self):
        return self._waybill_id

    @waybill_id.setter
    def waybill_id(self, value):
        self._waybill_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.channel_buyer_id:
            if hasattr(self.channel_buyer_id, 'to_alipay_dict'):
                params['channel_buyer_id'] = self.channel_buyer_id.to_alipay_dict()
            else:
                params['channel_buyer_id'] = self.channel_buyer_id
        if self.channel_order_id:
            if hasattr(self.channel_order_id, 'to_alipay_dict'):
                params['channel_order_id'] = self.channel_order_id.to_alipay_dict()
            else:
                params['channel_order_id'] = self.channel_order_id
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        if self.distribution_channel:
            if hasattr(self.distribution_channel, 'to_alipay_dict'):
                params['distribution_channel'] = self.distribution_channel.to_alipay_dict()
            else:
                params['distribution_channel'] = self.distribution_channel
        if self.sender_address:
            if hasattr(self.sender_address, 'to_alipay_dict'):
                params['sender_address'] = self.sender_address.to_alipay_dict()
            else:
                params['sender_address'] = self.sender_address
        if self.sender_district_code:
            if hasattr(self.sender_district_code, 'to_alipay_dict'):
                params['sender_district_code'] = self.sender_district_code.to_alipay_dict()
            else:
                params['sender_district_code'] = self.sender_district_code
        if self.sender_name:
            if hasattr(self.sender_name, 'to_alipay_dict'):
                params['sender_name'] = self.sender_name.to_alipay_dict()
            else:
                params['sender_name'] = self.sender_name
        if self.sender_phone:
            if hasattr(self.sender_phone, 'to_alipay_dict'):
                params['sender_phone'] = self.sender_phone.to_alipay_dict()
            else:
                params['sender_phone'] = self.sender_phone
        if self.waybill_id:
            if hasattr(self.waybill_id, 'to_alipay_dict'):
                params['waybill_id'] = self.waybill_id.to_alipay_dict()
            else:
                params['waybill_id'] = self.waybill_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentDistorderSendModel()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'channel_buyer_id' in d:
            o.channel_buyer_id = d['channel_buyer_id']
        if 'channel_order_id' in d:
            o.channel_order_id = d['channel_order_id']
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'distribution_channel' in d:
            o.distribution_channel = d['distribution_channel']
        if 'sender_address' in d:
            o.sender_address = d['sender_address']
        if 'sender_district_code' in d:
            o.sender_district_code = d['sender_district_code']
        if 'sender_name' in d:
            o.sender_name = d['sender_name']
        if 'sender_phone' in d:
            o.sender_phone = d['sender_phone']
        if 'waybill_id' in d:
            o.waybill_id = d['waybill_id']
        return o


