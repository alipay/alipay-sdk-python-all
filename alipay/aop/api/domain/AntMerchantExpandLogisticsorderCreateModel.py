#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo


class AntMerchantExpandLogisticsorderCreateModel(object):

    def __init__(self):
        self._ext_info = None
        self._gmt_pick = None
        self._goods_type = None
        self._memo = None
        self._order_id = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._price = None
        self._receiver_addr = None
        self._receiver_area = None
        self._receiver_city = None
        self._receiver_latitude = None
        self._receiver_longitude = None
        self._receiver_name = None
        self._receiver_phone = None
        self._receiver_poi_addr = None
        self._receiver_province = None
        self._receiver_street = None
        self._sender_addr = None
        self._sender_area = None
        self._sender_city = None
        self._sender_latitude = None
        self._sender_longitude = None
        self._sender_name = None
        self._sender_phone = None
        self._sender_poi_addr = None
        self._sender_province = None
        self._sender_street = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def gmt_pick(self):
        return self._gmt_pick

    @gmt_pick.setter
    def gmt_pick(self, value):
        self._gmt_pick = value
    @property
    def goods_type(self):
        return self._goods_type

    @goods_type.setter
    def goods_type(self, value):
        self._goods_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def receiver_addr(self):
        return self._receiver_addr

    @receiver_addr.setter
    def receiver_addr(self, value):
        self._receiver_addr = value
    @property
    def receiver_area(self):
        return self._receiver_area

    @receiver_area.setter
    def receiver_area(self, value):
        self._receiver_area = value
    @property
    def receiver_city(self):
        return self._receiver_city

    @receiver_city.setter
    def receiver_city(self, value):
        self._receiver_city = value
    @property
    def receiver_latitude(self):
        return self._receiver_latitude

    @receiver_latitude.setter
    def receiver_latitude(self, value):
        self._receiver_latitude = value
    @property
    def receiver_longitude(self):
        return self._receiver_longitude

    @receiver_longitude.setter
    def receiver_longitude(self, value):
        self._receiver_longitude = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value
    @property
    def receiver_poi_addr(self):
        return self._receiver_poi_addr

    @receiver_poi_addr.setter
    def receiver_poi_addr(self, value):
        self._receiver_poi_addr = value
    @property
    def receiver_province(self):
        return self._receiver_province

    @receiver_province.setter
    def receiver_province(self, value):
        self._receiver_province = value
    @property
    def receiver_street(self):
        return self._receiver_street

    @receiver_street.setter
    def receiver_street(self, value):
        self._receiver_street = value
    @property
    def sender_addr(self):
        return self._sender_addr

    @sender_addr.setter
    def sender_addr(self, value):
        self._sender_addr = value
    @property
    def sender_area(self):
        return self._sender_area

    @sender_area.setter
    def sender_area(self, value):
        self._sender_area = value
    @property
    def sender_city(self):
        return self._sender_city

    @sender_city.setter
    def sender_city(self, value):
        self._sender_city = value
    @property
    def sender_latitude(self):
        return self._sender_latitude

    @sender_latitude.setter
    def sender_latitude(self, value):
        self._sender_latitude = value
    @property
    def sender_longitude(self):
        return self._sender_longitude

    @sender_longitude.setter
    def sender_longitude(self, value):
        self._sender_longitude = value
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
    def sender_poi_addr(self):
        return self._sender_poi_addr

    @sender_poi_addr.setter
    def sender_poi_addr(self, value):
        self._sender_poi_addr = value
    @property
    def sender_province(self):
        return self._sender_province

    @sender_province.setter
    def sender_province(self, value):
        self._sender_province = value
    @property
    def sender_street(self):
        return self._sender_street

    @sender_street.setter
    def sender_street(self, value):
        self._sender_street = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_pick:
            if hasattr(self.gmt_pick, 'to_alipay_dict'):
                params['gmt_pick'] = self.gmt_pick.to_alipay_dict()
            else:
                params['gmt_pick'] = self.gmt_pick
        if self.goods_type:
            if hasattr(self.goods_type, 'to_alipay_dict'):
                params['goods_type'] = self.goods_type.to_alipay_dict()
            else:
                params['goods_type'] = self.goods_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.receiver_addr:
            if hasattr(self.receiver_addr, 'to_alipay_dict'):
                params['receiver_addr'] = self.receiver_addr.to_alipay_dict()
            else:
                params['receiver_addr'] = self.receiver_addr
        if self.receiver_area:
            if hasattr(self.receiver_area, 'to_alipay_dict'):
                params['receiver_area'] = self.receiver_area.to_alipay_dict()
            else:
                params['receiver_area'] = self.receiver_area
        if self.receiver_city:
            if hasattr(self.receiver_city, 'to_alipay_dict'):
                params['receiver_city'] = self.receiver_city.to_alipay_dict()
            else:
                params['receiver_city'] = self.receiver_city
        if self.receiver_latitude:
            if hasattr(self.receiver_latitude, 'to_alipay_dict'):
                params['receiver_latitude'] = self.receiver_latitude.to_alipay_dict()
            else:
                params['receiver_latitude'] = self.receiver_latitude
        if self.receiver_longitude:
            if hasattr(self.receiver_longitude, 'to_alipay_dict'):
                params['receiver_longitude'] = self.receiver_longitude.to_alipay_dict()
            else:
                params['receiver_longitude'] = self.receiver_longitude
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        if self.receiver_poi_addr:
            if hasattr(self.receiver_poi_addr, 'to_alipay_dict'):
                params['receiver_poi_addr'] = self.receiver_poi_addr.to_alipay_dict()
            else:
                params['receiver_poi_addr'] = self.receiver_poi_addr
        if self.receiver_province:
            if hasattr(self.receiver_province, 'to_alipay_dict'):
                params['receiver_province'] = self.receiver_province.to_alipay_dict()
            else:
                params['receiver_province'] = self.receiver_province
        if self.receiver_street:
            if hasattr(self.receiver_street, 'to_alipay_dict'):
                params['receiver_street'] = self.receiver_street.to_alipay_dict()
            else:
                params['receiver_street'] = self.receiver_street
        if self.sender_addr:
            if hasattr(self.sender_addr, 'to_alipay_dict'):
                params['sender_addr'] = self.sender_addr.to_alipay_dict()
            else:
                params['sender_addr'] = self.sender_addr
        if self.sender_area:
            if hasattr(self.sender_area, 'to_alipay_dict'):
                params['sender_area'] = self.sender_area.to_alipay_dict()
            else:
                params['sender_area'] = self.sender_area
        if self.sender_city:
            if hasattr(self.sender_city, 'to_alipay_dict'):
                params['sender_city'] = self.sender_city.to_alipay_dict()
            else:
                params['sender_city'] = self.sender_city
        if self.sender_latitude:
            if hasattr(self.sender_latitude, 'to_alipay_dict'):
                params['sender_latitude'] = self.sender_latitude.to_alipay_dict()
            else:
                params['sender_latitude'] = self.sender_latitude
        if self.sender_longitude:
            if hasattr(self.sender_longitude, 'to_alipay_dict'):
                params['sender_longitude'] = self.sender_longitude.to_alipay_dict()
            else:
                params['sender_longitude'] = self.sender_longitude
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
        if self.sender_poi_addr:
            if hasattr(self.sender_poi_addr, 'to_alipay_dict'):
                params['sender_poi_addr'] = self.sender_poi_addr.to_alipay_dict()
            else:
                params['sender_poi_addr'] = self.sender_poi_addr
        if self.sender_province:
            if hasattr(self.sender_province, 'to_alipay_dict'):
                params['sender_province'] = self.sender_province.to_alipay_dict()
            else:
                params['sender_province'] = self.sender_province
        if self.sender_street:
            if hasattr(self.sender_street, 'to_alipay_dict'):
                params['sender_street'] = self.sender_street.to_alipay_dict()
            else:
                params['sender_street'] = self.sender_street
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandLogisticsorderCreateModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_pick' in d:
            o.gmt_pick = d['gmt_pick']
        if 'goods_type' in d:
            o.goods_type = d['goods_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'price' in d:
            o.price = d['price']
        if 'receiver_addr' in d:
            o.receiver_addr = d['receiver_addr']
        if 'receiver_area' in d:
            o.receiver_area = d['receiver_area']
        if 'receiver_city' in d:
            o.receiver_city = d['receiver_city']
        if 'receiver_latitude' in d:
            o.receiver_latitude = d['receiver_latitude']
        if 'receiver_longitude' in d:
            o.receiver_longitude = d['receiver_longitude']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        if 'receiver_poi_addr' in d:
            o.receiver_poi_addr = d['receiver_poi_addr']
        if 'receiver_province' in d:
            o.receiver_province = d['receiver_province']
        if 'receiver_street' in d:
            o.receiver_street = d['receiver_street']
        if 'sender_addr' in d:
            o.sender_addr = d['sender_addr']
        if 'sender_area' in d:
            o.sender_area = d['sender_area']
        if 'sender_city' in d:
            o.sender_city = d['sender_city']
        if 'sender_latitude' in d:
            o.sender_latitude = d['sender_latitude']
        if 'sender_longitude' in d:
            o.sender_longitude = d['sender_longitude']
        if 'sender_name' in d:
            o.sender_name = d['sender_name']
        if 'sender_phone' in d:
            o.sender_phone = d['sender_phone']
        if 'sender_poi_addr' in d:
            o.sender_poi_addr = d['sender_poi_addr']
        if 'sender_province' in d:
            o.sender_province = d['sender_province']
        if 'sender_street' in d:
            o.sender_street = d['sender_street']
        return o


