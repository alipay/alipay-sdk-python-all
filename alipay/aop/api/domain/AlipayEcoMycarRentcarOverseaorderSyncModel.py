#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddRentTradeInfo import AddRentTradeInfo


class AlipayEcoMycarRentcarOverseaorderSyncModel(object):

    def __init__(self):
        self._add_rent_trade_list = None
        self._applets_service_amount = None
        self._applets_service_category = None
        self._cancelled_amount = None
        self._carlife_vehicle_id = None
        self._deposit_amount = None
        self._deposit_deduct_amount = None
        self._discount_amount = None
        self._displacement = None
        self._driver_mobile = None
        self._driver_name = None
        self._driving_distance = None
        self._drop_off_address = None
        self._drop_off_city_code = None
        self._drop_off_city_name = None
        self._drop_off_region_code = None
        self._drop_off_region_name = None
        self._drop_off_store_name = None
        self._drop_off_time = None
        self._fill_amount = None
        self._has_continue_rent = None
        self._has_damage = None
        self._has_early_give_back = None
        self._has_violation = None
        self._home_get_and_send = None
        self._open_id = None
        self._order_status = None
        self._other_drop_off = None
        self._out_order_no = None
        self._out_order_time = None
        self._pay_amount = None
        self._pay_time = None
        self._pick_up_address = None
        self._pick_up_city_code = None
        self._pick_up_city_name = None
        self._pick_up_region_code = None
        self._pick_up_region_name = None
        self._pick_up_store_name = None
        self._pick_up_time = None
        self._refund_amount = None
        self._refund_reason = None
        self._refund_time = None
        self._rent_company_name = None
        self._store_drop_off_phone = None
        self._store_pick_up_phone = None
        self._total_amount = None
        self._trade_no = None
        self._transmission_type = None
        self._unit_amount = None
        self._user_id = None
        self._vehicle_brand_name = None
        self._vehicle_plate_no = None
        self._vehicle_series_name = None
        self._vehicle_show_name = None

    @property
    def add_rent_trade_list(self):
        return self._add_rent_trade_list

    @add_rent_trade_list.setter
    def add_rent_trade_list(self, value):
        if isinstance(value, AddRentTradeInfo):
            self._add_rent_trade_list = value
        else:
            self._add_rent_trade_list = AddRentTradeInfo.from_alipay_dict(value)
    @property
    def applets_service_amount(self):
        return self._applets_service_amount

    @applets_service_amount.setter
    def applets_service_amount(self, value):
        self._applets_service_amount = value
    @property
    def applets_service_category(self):
        return self._applets_service_category

    @applets_service_category.setter
    def applets_service_category(self, value):
        self._applets_service_category = value
    @property
    def cancelled_amount(self):
        return self._cancelled_amount

    @cancelled_amount.setter
    def cancelled_amount(self, value):
        self._cancelled_amount = value
    @property
    def carlife_vehicle_id(self):
        return self._carlife_vehicle_id

    @carlife_vehicle_id.setter
    def carlife_vehicle_id(self, value):
        self._carlife_vehicle_id = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def deposit_deduct_amount(self):
        return self._deposit_deduct_amount

    @deposit_deduct_amount.setter
    def deposit_deduct_amount(self, value):
        self._deposit_deduct_amount = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value
    @property
    def driver_mobile(self):
        return self._driver_mobile

    @driver_mobile.setter
    def driver_mobile(self, value):
        self._driver_mobile = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driving_distance(self):
        return self._driving_distance

    @driving_distance.setter
    def driving_distance(self, value):
        self._driving_distance = value
    @property
    def drop_off_address(self):
        return self._drop_off_address

    @drop_off_address.setter
    def drop_off_address(self, value):
        self._drop_off_address = value
    @property
    def drop_off_city_code(self):
        return self._drop_off_city_code

    @drop_off_city_code.setter
    def drop_off_city_code(self, value):
        self._drop_off_city_code = value
    @property
    def drop_off_city_name(self):
        return self._drop_off_city_name

    @drop_off_city_name.setter
    def drop_off_city_name(self, value):
        self._drop_off_city_name = value
    @property
    def drop_off_region_code(self):
        return self._drop_off_region_code

    @drop_off_region_code.setter
    def drop_off_region_code(self, value):
        self._drop_off_region_code = value
    @property
    def drop_off_region_name(self):
        return self._drop_off_region_name

    @drop_off_region_name.setter
    def drop_off_region_name(self, value):
        self._drop_off_region_name = value
    @property
    def drop_off_store_name(self):
        return self._drop_off_store_name

    @drop_off_store_name.setter
    def drop_off_store_name(self, value):
        self._drop_off_store_name = value
    @property
    def drop_off_time(self):
        return self._drop_off_time

    @drop_off_time.setter
    def drop_off_time(self, value):
        self._drop_off_time = value
    @property
    def fill_amount(self):
        return self._fill_amount

    @fill_amount.setter
    def fill_amount(self, value):
        self._fill_amount = value
    @property
    def has_continue_rent(self):
        return self._has_continue_rent

    @has_continue_rent.setter
    def has_continue_rent(self, value):
        self._has_continue_rent = value
    @property
    def has_damage(self):
        return self._has_damage

    @has_damage.setter
    def has_damage(self, value):
        self._has_damage = value
    @property
    def has_early_give_back(self):
        return self._has_early_give_back

    @has_early_give_back.setter
    def has_early_give_back(self, value):
        self._has_early_give_back = value
    @property
    def has_violation(self):
        return self._has_violation

    @has_violation.setter
    def has_violation(self, value):
        self._has_violation = value
    @property
    def home_get_and_send(self):
        return self._home_get_and_send

    @home_get_and_send.setter
    def home_get_and_send(self, value):
        self._home_get_and_send = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def other_drop_off(self):
        return self._other_drop_off

    @other_drop_off.setter
    def other_drop_off(self, value):
        self._other_drop_off = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_order_time(self):
        return self._out_order_time

    @out_order_time.setter
    def out_order_time(self, value):
        self._out_order_time = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pick_up_address(self):
        return self._pick_up_address

    @pick_up_address.setter
    def pick_up_address(self, value):
        self._pick_up_address = value
    @property
    def pick_up_city_code(self):
        return self._pick_up_city_code

    @pick_up_city_code.setter
    def pick_up_city_code(self, value):
        self._pick_up_city_code = value
    @property
    def pick_up_city_name(self):
        return self._pick_up_city_name

    @pick_up_city_name.setter
    def pick_up_city_name(self, value):
        self._pick_up_city_name = value
    @property
    def pick_up_region_code(self):
        return self._pick_up_region_code

    @pick_up_region_code.setter
    def pick_up_region_code(self, value):
        self._pick_up_region_code = value
    @property
    def pick_up_region_name(self):
        return self._pick_up_region_name

    @pick_up_region_name.setter
    def pick_up_region_name(self, value):
        self._pick_up_region_name = value
    @property
    def pick_up_store_name(self):
        return self._pick_up_store_name

    @pick_up_store_name.setter
    def pick_up_store_name(self, value):
        self._pick_up_store_name = value
    @property
    def pick_up_time(self):
        return self._pick_up_time

    @pick_up_time.setter
    def pick_up_time(self, value):
        self._pick_up_time = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def rent_company_name(self):
        return self._rent_company_name

    @rent_company_name.setter
    def rent_company_name(self, value):
        self._rent_company_name = value
    @property
    def store_drop_off_phone(self):
        return self._store_drop_off_phone

    @store_drop_off_phone.setter
    def store_drop_off_phone(self, value):
        self._store_drop_off_phone = value
    @property
    def store_pick_up_phone(self):
        return self._store_pick_up_phone

    @store_pick_up_phone.setter
    def store_pick_up_phone(self, value):
        self._store_pick_up_phone = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def transmission_type(self):
        return self._transmission_type

    @transmission_type.setter
    def transmission_type(self, value):
        self._transmission_type = value
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vehicle_brand_name(self):
        return self._vehicle_brand_name

    @vehicle_brand_name.setter
    def vehicle_brand_name(self, value):
        self._vehicle_brand_name = value
    @property
    def vehicle_plate_no(self):
        return self._vehicle_plate_no

    @vehicle_plate_no.setter
    def vehicle_plate_no(self, value):
        self._vehicle_plate_no = value
    @property
    def vehicle_series_name(self):
        return self._vehicle_series_name

    @vehicle_series_name.setter
    def vehicle_series_name(self, value):
        self._vehicle_series_name = value
    @property
    def vehicle_show_name(self):
        return self._vehicle_show_name

    @vehicle_show_name.setter
    def vehicle_show_name(self, value):
        self._vehicle_show_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_rent_trade_list:
            if hasattr(self.add_rent_trade_list, 'to_alipay_dict'):
                params['add_rent_trade_list'] = self.add_rent_trade_list.to_alipay_dict()
            else:
                params['add_rent_trade_list'] = self.add_rent_trade_list
        if self.applets_service_amount:
            if hasattr(self.applets_service_amount, 'to_alipay_dict'):
                params['applets_service_amount'] = self.applets_service_amount.to_alipay_dict()
            else:
                params['applets_service_amount'] = self.applets_service_amount
        if self.applets_service_category:
            if hasattr(self.applets_service_category, 'to_alipay_dict'):
                params['applets_service_category'] = self.applets_service_category.to_alipay_dict()
            else:
                params['applets_service_category'] = self.applets_service_category
        if self.cancelled_amount:
            if hasattr(self.cancelled_amount, 'to_alipay_dict'):
                params['cancelled_amount'] = self.cancelled_amount.to_alipay_dict()
            else:
                params['cancelled_amount'] = self.cancelled_amount
        if self.carlife_vehicle_id:
            if hasattr(self.carlife_vehicle_id, 'to_alipay_dict'):
                params['carlife_vehicle_id'] = self.carlife_vehicle_id.to_alipay_dict()
            else:
                params['carlife_vehicle_id'] = self.carlife_vehicle_id
        if self.deposit_amount:
            if hasattr(self.deposit_amount, 'to_alipay_dict'):
                params['deposit_amount'] = self.deposit_amount.to_alipay_dict()
            else:
                params['deposit_amount'] = self.deposit_amount
        if self.deposit_deduct_amount:
            if hasattr(self.deposit_deduct_amount, 'to_alipay_dict'):
                params['deposit_deduct_amount'] = self.deposit_deduct_amount.to_alipay_dict()
            else:
                params['deposit_deduct_amount'] = self.deposit_deduct_amount
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.displacement:
            if hasattr(self.displacement, 'to_alipay_dict'):
                params['displacement'] = self.displacement.to_alipay_dict()
            else:
                params['displacement'] = self.displacement
        if self.driver_mobile:
            if hasattr(self.driver_mobile, 'to_alipay_dict'):
                params['driver_mobile'] = self.driver_mobile.to_alipay_dict()
            else:
                params['driver_mobile'] = self.driver_mobile
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driving_distance:
            if hasattr(self.driving_distance, 'to_alipay_dict'):
                params['driving_distance'] = self.driving_distance.to_alipay_dict()
            else:
                params['driving_distance'] = self.driving_distance
        if self.drop_off_address:
            if hasattr(self.drop_off_address, 'to_alipay_dict'):
                params['drop_off_address'] = self.drop_off_address.to_alipay_dict()
            else:
                params['drop_off_address'] = self.drop_off_address
        if self.drop_off_city_code:
            if hasattr(self.drop_off_city_code, 'to_alipay_dict'):
                params['drop_off_city_code'] = self.drop_off_city_code.to_alipay_dict()
            else:
                params['drop_off_city_code'] = self.drop_off_city_code
        if self.drop_off_city_name:
            if hasattr(self.drop_off_city_name, 'to_alipay_dict'):
                params['drop_off_city_name'] = self.drop_off_city_name.to_alipay_dict()
            else:
                params['drop_off_city_name'] = self.drop_off_city_name
        if self.drop_off_region_code:
            if hasattr(self.drop_off_region_code, 'to_alipay_dict'):
                params['drop_off_region_code'] = self.drop_off_region_code.to_alipay_dict()
            else:
                params['drop_off_region_code'] = self.drop_off_region_code
        if self.drop_off_region_name:
            if hasattr(self.drop_off_region_name, 'to_alipay_dict'):
                params['drop_off_region_name'] = self.drop_off_region_name.to_alipay_dict()
            else:
                params['drop_off_region_name'] = self.drop_off_region_name
        if self.drop_off_store_name:
            if hasattr(self.drop_off_store_name, 'to_alipay_dict'):
                params['drop_off_store_name'] = self.drop_off_store_name.to_alipay_dict()
            else:
                params['drop_off_store_name'] = self.drop_off_store_name
        if self.drop_off_time:
            if hasattr(self.drop_off_time, 'to_alipay_dict'):
                params['drop_off_time'] = self.drop_off_time.to_alipay_dict()
            else:
                params['drop_off_time'] = self.drop_off_time
        if self.fill_amount:
            if hasattr(self.fill_amount, 'to_alipay_dict'):
                params['fill_amount'] = self.fill_amount.to_alipay_dict()
            else:
                params['fill_amount'] = self.fill_amount
        if self.has_continue_rent:
            if hasattr(self.has_continue_rent, 'to_alipay_dict'):
                params['has_continue_rent'] = self.has_continue_rent.to_alipay_dict()
            else:
                params['has_continue_rent'] = self.has_continue_rent
        if self.has_damage:
            if hasattr(self.has_damage, 'to_alipay_dict'):
                params['has_damage'] = self.has_damage.to_alipay_dict()
            else:
                params['has_damage'] = self.has_damage
        if self.has_early_give_back:
            if hasattr(self.has_early_give_back, 'to_alipay_dict'):
                params['has_early_give_back'] = self.has_early_give_back.to_alipay_dict()
            else:
                params['has_early_give_back'] = self.has_early_give_back
        if self.has_violation:
            if hasattr(self.has_violation, 'to_alipay_dict'):
                params['has_violation'] = self.has_violation.to_alipay_dict()
            else:
                params['has_violation'] = self.has_violation
        if self.home_get_and_send:
            if hasattr(self.home_get_and_send, 'to_alipay_dict'):
                params['home_get_and_send'] = self.home_get_and_send.to_alipay_dict()
            else:
                params['home_get_and_send'] = self.home_get_and_send
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.other_drop_off:
            if hasattr(self.other_drop_off, 'to_alipay_dict'):
                params['other_drop_off'] = self.other_drop_off.to_alipay_dict()
            else:
                params['other_drop_off'] = self.other_drop_off
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_order_time:
            if hasattr(self.out_order_time, 'to_alipay_dict'):
                params['out_order_time'] = self.out_order_time.to_alipay_dict()
            else:
                params['out_order_time'] = self.out_order_time
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.pick_up_address:
            if hasattr(self.pick_up_address, 'to_alipay_dict'):
                params['pick_up_address'] = self.pick_up_address.to_alipay_dict()
            else:
                params['pick_up_address'] = self.pick_up_address
        if self.pick_up_city_code:
            if hasattr(self.pick_up_city_code, 'to_alipay_dict'):
                params['pick_up_city_code'] = self.pick_up_city_code.to_alipay_dict()
            else:
                params['pick_up_city_code'] = self.pick_up_city_code
        if self.pick_up_city_name:
            if hasattr(self.pick_up_city_name, 'to_alipay_dict'):
                params['pick_up_city_name'] = self.pick_up_city_name.to_alipay_dict()
            else:
                params['pick_up_city_name'] = self.pick_up_city_name
        if self.pick_up_region_code:
            if hasattr(self.pick_up_region_code, 'to_alipay_dict'):
                params['pick_up_region_code'] = self.pick_up_region_code.to_alipay_dict()
            else:
                params['pick_up_region_code'] = self.pick_up_region_code
        if self.pick_up_region_name:
            if hasattr(self.pick_up_region_name, 'to_alipay_dict'):
                params['pick_up_region_name'] = self.pick_up_region_name.to_alipay_dict()
            else:
                params['pick_up_region_name'] = self.pick_up_region_name
        if self.pick_up_store_name:
            if hasattr(self.pick_up_store_name, 'to_alipay_dict'):
                params['pick_up_store_name'] = self.pick_up_store_name.to_alipay_dict()
            else:
                params['pick_up_store_name'] = self.pick_up_store_name
        if self.pick_up_time:
            if hasattr(self.pick_up_time, 'to_alipay_dict'):
                params['pick_up_time'] = self.pick_up_time.to_alipay_dict()
            else:
                params['pick_up_time'] = self.pick_up_time
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.rent_company_name:
            if hasattr(self.rent_company_name, 'to_alipay_dict'):
                params['rent_company_name'] = self.rent_company_name.to_alipay_dict()
            else:
                params['rent_company_name'] = self.rent_company_name
        if self.store_drop_off_phone:
            if hasattr(self.store_drop_off_phone, 'to_alipay_dict'):
                params['store_drop_off_phone'] = self.store_drop_off_phone.to_alipay_dict()
            else:
                params['store_drop_off_phone'] = self.store_drop_off_phone
        if self.store_pick_up_phone:
            if hasattr(self.store_pick_up_phone, 'to_alipay_dict'):
                params['store_pick_up_phone'] = self.store_pick_up_phone.to_alipay_dict()
            else:
                params['store_pick_up_phone'] = self.store_pick_up_phone
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.transmission_type:
            if hasattr(self.transmission_type, 'to_alipay_dict'):
                params['transmission_type'] = self.transmission_type.to_alipay_dict()
            else:
                params['transmission_type'] = self.transmission_type
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vehicle_brand_name:
            if hasattr(self.vehicle_brand_name, 'to_alipay_dict'):
                params['vehicle_brand_name'] = self.vehicle_brand_name.to_alipay_dict()
            else:
                params['vehicle_brand_name'] = self.vehicle_brand_name
        if self.vehicle_plate_no:
            if hasattr(self.vehicle_plate_no, 'to_alipay_dict'):
                params['vehicle_plate_no'] = self.vehicle_plate_no.to_alipay_dict()
            else:
                params['vehicle_plate_no'] = self.vehicle_plate_no
        if self.vehicle_series_name:
            if hasattr(self.vehicle_series_name, 'to_alipay_dict'):
                params['vehicle_series_name'] = self.vehicle_series_name.to_alipay_dict()
            else:
                params['vehicle_series_name'] = self.vehicle_series_name
        if self.vehicle_show_name:
            if hasattr(self.vehicle_show_name, 'to_alipay_dict'):
                params['vehicle_show_name'] = self.vehicle_show_name.to_alipay_dict()
            else:
                params['vehicle_show_name'] = self.vehicle_show_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarRentcarOverseaorderSyncModel()
        if 'add_rent_trade_list' in d:
            o.add_rent_trade_list = d['add_rent_trade_list']
        if 'applets_service_amount' in d:
            o.applets_service_amount = d['applets_service_amount']
        if 'applets_service_category' in d:
            o.applets_service_category = d['applets_service_category']
        if 'cancelled_amount' in d:
            o.cancelled_amount = d['cancelled_amount']
        if 'carlife_vehicle_id' in d:
            o.carlife_vehicle_id = d['carlife_vehicle_id']
        if 'deposit_amount' in d:
            o.deposit_amount = d['deposit_amount']
        if 'deposit_deduct_amount' in d:
            o.deposit_deduct_amount = d['deposit_deduct_amount']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'displacement' in d:
            o.displacement = d['displacement']
        if 'driver_mobile' in d:
            o.driver_mobile = d['driver_mobile']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driving_distance' in d:
            o.driving_distance = d['driving_distance']
        if 'drop_off_address' in d:
            o.drop_off_address = d['drop_off_address']
        if 'drop_off_city_code' in d:
            o.drop_off_city_code = d['drop_off_city_code']
        if 'drop_off_city_name' in d:
            o.drop_off_city_name = d['drop_off_city_name']
        if 'drop_off_region_code' in d:
            o.drop_off_region_code = d['drop_off_region_code']
        if 'drop_off_region_name' in d:
            o.drop_off_region_name = d['drop_off_region_name']
        if 'drop_off_store_name' in d:
            o.drop_off_store_name = d['drop_off_store_name']
        if 'drop_off_time' in d:
            o.drop_off_time = d['drop_off_time']
        if 'fill_amount' in d:
            o.fill_amount = d['fill_amount']
        if 'has_continue_rent' in d:
            o.has_continue_rent = d['has_continue_rent']
        if 'has_damage' in d:
            o.has_damage = d['has_damage']
        if 'has_early_give_back' in d:
            o.has_early_give_back = d['has_early_give_back']
        if 'has_violation' in d:
            o.has_violation = d['has_violation']
        if 'home_get_and_send' in d:
            o.home_get_and_send = d['home_get_and_send']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'other_drop_off' in d:
            o.other_drop_off = d['other_drop_off']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_order_time' in d:
            o.out_order_time = d['out_order_time']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'pick_up_address' in d:
            o.pick_up_address = d['pick_up_address']
        if 'pick_up_city_code' in d:
            o.pick_up_city_code = d['pick_up_city_code']
        if 'pick_up_city_name' in d:
            o.pick_up_city_name = d['pick_up_city_name']
        if 'pick_up_region_code' in d:
            o.pick_up_region_code = d['pick_up_region_code']
        if 'pick_up_region_name' in d:
            o.pick_up_region_name = d['pick_up_region_name']
        if 'pick_up_store_name' in d:
            o.pick_up_store_name = d['pick_up_store_name']
        if 'pick_up_time' in d:
            o.pick_up_time = d['pick_up_time']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'rent_company_name' in d:
            o.rent_company_name = d['rent_company_name']
        if 'store_drop_off_phone' in d:
            o.store_drop_off_phone = d['store_drop_off_phone']
        if 'store_pick_up_phone' in d:
            o.store_pick_up_phone = d['store_pick_up_phone']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'transmission_type' in d:
            o.transmission_type = d['transmission_type']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vehicle_brand_name' in d:
            o.vehicle_brand_name = d['vehicle_brand_name']
        if 'vehicle_plate_no' in d:
            o.vehicle_plate_no = d['vehicle_plate_no']
        if 'vehicle_series_name' in d:
            o.vehicle_series_name = d['vehicle_series_name']
        if 'vehicle_show_name' in d:
            o.vehicle_show_name = d['vehicle_show_name']
        return o


