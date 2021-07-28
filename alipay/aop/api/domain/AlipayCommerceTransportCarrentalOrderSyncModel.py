#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarRentalInfo import CarRentalInfo
from alipay.aop.api.domain.CarRentalGoodsInfo import CarRentalGoodsInfo
from alipay.aop.api.domain.ExtraInfo import ExtraInfo
from alipay.aop.api.domain.CarRentalVehicleInfo import CarRentalVehicleInfo


class AlipayCommerceTransportCarrentalOrderSyncModel(object):

    def __init__(self):
        self._buyer_id = None
        self._car_rental_info = None
        self._discount_amount = None
        self._goods_info = None
        self._merchant_order_no = None
        self._order_amount = None
        self._order_create_time = None
        self._order_detail_url = None
        self._order_extra_info = None
        self._order_modify_time = None
        self._order_source = None
        self._order_type = None
        self._payment_amount = None
        self._payment_type = None
        self._record_id = None
        self._service_code = None
        self._status = None
        self._sub_service_type = None
        self._trade_no = None
        self._vehicle_info = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def car_rental_info(self):
        return self._car_rental_info

    @car_rental_info.setter
    def car_rental_info(self, value):
        if isinstance(value, CarRentalInfo):
            self._car_rental_info = value
        else:
            self._car_rental_info = CarRentalInfo.from_alipay_dict(value)
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, CarRentalGoodsInfo):
            self._goods_info = value
        else:
            self._goods_info = CarRentalGoodsInfo.from_alipay_dict(value)
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_extra_info(self):
        return self._order_extra_info

    @order_extra_info.setter
    def order_extra_info(self, value):
        if isinstance(value, list):
            self._order_extra_info = list()
            for i in value:
                if isinstance(i, ExtraInfo):
                    self._order_extra_info.append(i)
                else:
                    self._order_extra_info.append(ExtraInfo.from_alipay_dict(i))
    @property
    def order_modify_time(self):
        return self._order_modify_time

    @order_modify_time.setter
    def order_modify_time(self, value):
        self._order_modify_time = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_service_type(self):
        return self._sub_service_type

    @sub_service_type.setter
    def sub_service_type(self, value):
        self._sub_service_type = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def vehicle_info(self):
        return self._vehicle_info

    @vehicle_info.setter
    def vehicle_info(self, value):
        if isinstance(value, CarRentalVehicleInfo):
            self._vehicle_info = value
        else:
            self._vehicle_info = CarRentalVehicleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.car_rental_info:
            if hasattr(self.car_rental_info, 'to_alipay_dict'):
                params['car_rental_info'] = self.car_rental_info.to_alipay_dict()
            else:
                params['car_rental_info'] = self.car_rental_info
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_extra_info:
            if isinstance(self.order_extra_info, list):
                for i in range(0, len(self.order_extra_info)):
                    element = self.order_extra_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_extra_info[i] = element.to_alipay_dict()
            if hasattr(self.order_extra_info, 'to_alipay_dict'):
                params['order_extra_info'] = self.order_extra_info.to_alipay_dict()
            else:
                params['order_extra_info'] = self.order_extra_info
        if self.order_modify_time:
            if hasattr(self.order_modify_time, 'to_alipay_dict'):
                params['order_modify_time'] = self.order_modify_time.to_alipay_dict()
            else:
                params['order_modify_time'] = self.order_modify_time
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_service_type:
            if hasattr(self.sub_service_type, 'to_alipay_dict'):
                params['sub_service_type'] = self.sub_service_type.to_alipay_dict()
            else:
                params['sub_service_type'] = self.sub_service_type
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.vehicle_info:
            if hasattr(self.vehicle_info, 'to_alipay_dict'):
                params['vehicle_info'] = self.vehicle_info.to_alipay_dict()
            else:
                params['vehicle_info'] = self.vehicle_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportCarrentalOrderSyncModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'car_rental_info' in d:
            o.car_rental_info = d['car_rental_info']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_extra_info' in d:
            o.order_extra_info = d['order_extra_info']
        if 'order_modify_time' in d:
            o.order_modify_time = d['order_modify_time']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'status' in d:
            o.status = d['status']
        if 'sub_service_type' in d:
            o.sub_service_type = d['sub_service_type']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'vehicle_info' in d:
            o.vehicle_info = d['vehicle_info']
        return o


