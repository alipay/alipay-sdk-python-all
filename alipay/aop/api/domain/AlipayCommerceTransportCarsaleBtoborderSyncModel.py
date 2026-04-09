#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarSaleVehicleInfoDTO import CarSaleVehicleInfoDTO


class AlipayCommerceTransportCarsaleBtoborderSyncModel(object):

    def __init__(self):
        self._buy_city_code = None
        self._buy_mobile_no = None
        self._car_city_code = None
        self._charge_amount = None
        self._open_id = None
        self._order_amount = None
        self._order_id = None
        self._order_status = None
        self._order_type = None
        self._out_order_no = None
        self._pay_amount = None
        self._pay_channel = None
        self._plate_no = None
        self._second_pid = None
        self._sell_mobile_no = None
        self._sell_open_id = None
        self._sell_user_id = None
        self._unpay_amount = None
        self._user_id = None
        self._vehicle_info = None
        self._vin = None

    @property
    def buy_city_code(self):
        return self._buy_city_code

    @buy_city_code.setter
    def buy_city_code(self, value):
        self._buy_city_code = value
    @property
    def buy_mobile_no(self):
        return self._buy_mobile_no

    @buy_mobile_no.setter
    def buy_mobile_no(self, value):
        self._buy_mobile_no = value
    @property
    def car_city_code(self):
        return self._car_city_code

    @car_city_code.setter
    def car_city_code(self, value):
        self._car_city_code = value
    @property
    def charge_amount(self):
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, value):
        self._charge_amount = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def second_pid(self):
        return self._second_pid

    @second_pid.setter
    def second_pid(self, value):
        self._second_pid = value
    @property
    def sell_mobile_no(self):
        return self._sell_mobile_no

    @sell_mobile_no.setter
    def sell_mobile_no(self, value):
        self._sell_mobile_no = value
    @property
    def sell_open_id(self):
        return self._sell_open_id

    @sell_open_id.setter
    def sell_open_id(self, value):
        self._sell_open_id = value
    @property
    def sell_user_id(self):
        return self._sell_user_id

    @sell_user_id.setter
    def sell_user_id(self, value):
        self._sell_user_id = value
    @property
    def unpay_amount(self):
        return self._unpay_amount

    @unpay_amount.setter
    def unpay_amount(self, value):
        self._unpay_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vehicle_info(self):
        return self._vehicle_info

    @vehicle_info.setter
    def vehicle_info(self, value):
        if isinstance(value, CarSaleVehicleInfoDTO):
            self._vehicle_info = value
        else:
            self._vehicle_info = CarSaleVehicleInfoDTO.from_alipay_dict(value)
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_city_code:
            if hasattr(self.buy_city_code, 'to_alipay_dict'):
                params['buy_city_code'] = self.buy_city_code.to_alipay_dict()
            else:
                params['buy_city_code'] = self.buy_city_code
        if self.buy_mobile_no:
            if hasattr(self.buy_mobile_no, 'to_alipay_dict'):
                params['buy_mobile_no'] = self.buy_mobile_no.to_alipay_dict()
            else:
                params['buy_mobile_no'] = self.buy_mobile_no
        if self.car_city_code:
            if hasattr(self.car_city_code, 'to_alipay_dict'):
                params['car_city_code'] = self.car_city_code.to_alipay_dict()
            else:
                params['car_city_code'] = self.car_city_code
        if self.charge_amount:
            if hasattr(self.charge_amount, 'to_alipay_dict'):
                params['charge_amount'] = self.charge_amount.to_alipay_dict()
            else:
                params['charge_amount'] = self.charge_amount
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.second_pid:
            if hasattr(self.second_pid, 'to_alipay_dict'):
                params['second_pid'] = self.second_pid.to_alipay_dict()
            else:
                params['second_pid'] = self.second_pid
        if self.sell_mobile_no:
            if hasattr(self.sell_mobile_no, 'to_alipay_dict'):
                params['sell_mobile_no'] = self.sell_mobile_no.to_alipay_dict()
            else:
                params['sell_mobile_no'] = self.sell_mobile_no
        if self.sell_open_id:
            if hasattr(self.sell_open_id, 'to_alipay_dict'):
                params['sell_open_id'] = self.sell_open_id.to_alipay_dict()
            else:
                params['sell_open_id'] = self.sell_open_id
        if self.sell_user_id:
            if hasattr(self.sell_user_id, 'to_alipay_dict'):
                params['sell_user_id'] = self.sell_user_id.to_alipay_dict()
            else:
                params['sell_user_id'] = self.sell_user_id
        if self.unpay_amount:
            if hasattr(self.unpay_amount, 'to_alipay_dict'):
                params['unpay_amount'] = self.unpay_amount.to_alipay_dict()
            else:
                params['unpay_amount'] = self.unpay_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vehicle_info:
            if hasattr(self.vehicle_info, 'to_alipay_dict'):
                params['vehicle_info'] = self.vehicle_info.to_alipay_dict()
            else:
                params['vehicle_info'] = self.vehicle_info
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportCarsaleBtoborderSyncModel()
        if 'buy_city_code' in d:
            o.buy_city_code = d['buy_city_code']
        if 'buy_mobile_no' in d:
            o.buy_mobile_no = d['buy_mobile_no']
        if 'car_city_code' in d:
            o.car_city_code = d['car_city_code']
        if 'charge_amount' in d:
            o.charge_amount = d['charge_amount']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'second_pid' in d:
            o.second_pid = d['second_pid']
        if 'sell_mobile_no' in d:
            o.sell_mobile_no = d['sell_mobile_no']
        if 'sell_open_id' in d:
            o.sell_open_id = d['sell_open_id']
        if 'sell_user_id' in d:
            o.sell_user_id = d['sell_user_id']
        if 'unpay_amount' in d:
            o.unpay_amount = d['unpay_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vehicle_info' in d:
            o.vehicle_info = d['vehicle_info']
        if 'vin' in d:
            o.vin = d['vin']
        return o


