#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarJvorderSyncModel(object):

    def __init__(self):
        self._actual_pick_up_time = None
        self._discount_amount = None
        self._drop_off_store_name = None
        self._finish_time = None
        self._jv_discount_amount = None
        self._open_id = None
        self._order_channel = None
        self._order_create_time = None
        self._order_status = None
        self._order_type = None
        self._other_discount_amount = None
        self._out_order_no = None
        self._partner_id = None
        self._pay_amount = None
        self._pick_up_store_name = None
        self._plan_drop_off_time = None
        self._plan_pick_up_time = None
        self._total_amount = None
        self._user_id = None
        self._vehicle_brand_name = None
        self._vehicle_color = None
        self._vehicle_plate_no = None
        self._vehicle_seat_num = None
        self._vehicle_series_name = None
        self._vehicle_show_name = None

    @property
    def actual_pick_up_time(self):
        return self._actual_pick_up_time

    @actual_pick_up_time.setter
    def actual_pick_up_time(self, value):
        self._actual_pick_up_time = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def drop_off_store_name(self):
        return self._drop_off_store_name

    @drop_off_store_name.setter
    def drop_off_store_name(self, value):
        self._drop_off_store_name = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def jv_discount_amount(self):
        return self._jv_discount_amount

    @jv_discount_amount.setter
    def jv_discount_amount(self, value):
        self._jv_discount_amount = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_channel(self):
        return self._order_channel

    @order_channel.setter
    def order_channel(self, value):
        self._order_channel = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
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
    def other_discount_amount(self):
        return self._other_discount_amount

    @other_discount_amount.setter
    def other_discount_amount(self, value):
        self._other_discount_amount = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pick_up_store_name(self):
        return self._pick_up_store_name

    @pick_up_store_name.setter
    def pick_up_store_name(self, value):
        self._pick_up_store_name = value
    @property
    def plan_drop_off_time(self):
        return self._plan_drop_off_time

    @plan_drop_off_time.setter
    def plan_drop_off_time(self, value):
        self._plan_drop_off_time = value
    @property
    def plan_pick_up_time(self):
        return self._plan_pick_up_time

    @plan_pick_up_time.setter
    def plan_pick_up_time(self, value):
        self._plan_pick_up_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
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
    def vehicle_color(self):
        return self._vehicle_color

    @vehicle_color.setter
    def vehicle_color(self, value):
        self._vehicle_color = value
    @property
    def vehicle_plate_no(self):
        return self._vehicle_plate_no

    @vehicle_plate_no.setter
    def vehicle_plate_no(self, value):
        self._vehicle_plate_no = value
    @property
    def vehicle_seat_num(self):
        return self._vehicle_seat_num

    @vehicle_seat_num.setter
    def vehicle_seat_num(self, value):
        self._vehicle_seat_num = value
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
        if self.actual_pick_up_time:
            if hasattr(self.actual_pick_up_time, 'to_alipay_dict'):
                params['actual_pick_up_time'] = self.actual_pick_up_time.to_alipay_dict()
            else:
                params['actual_pick_up_time'] = self.actual_pick_up_time
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.drop_off_store_name:
            if hasattr(self.drop_off_store_name, 'to_alipay_dict'):
                params['drop_off_store_name'] = self.drop_off_store_name.to_alipay_dict()
            else:
                params['drop_off_store_name'] = self.drop_off_store_name
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.jv_discount_amount:
            if hasattr(self.jv_discount_amount, 'to_alipay_dict'):
                params['jv_discount_amount'] = self.jv_discount_amount.to_alipay_dict()
            else:
                params['jv_discount_amount'] = self.jv_discount_amount
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_channel:
            if hasattr(self.order_channel, 'to_alipay_dict'):
                params['order_channel'] = self.order_channel.to_alipay_dict()
            else:
                params['order_channel'] = self.order_channel
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
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
        if self.other_discount_amount:
            if hasattr(self.other_discount_amount, 'to_alipay_dict'):
                params['other_discount_amount'] = self.other_discount_amount.to_alipay_dict()
            else:
                params['other_discount_amount'] = self.other_discount_amount
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pick_up_store_name:
            if hasattr(self.pick_up_store_name, 'to_alipay_dict'):
                params['pick_up_store_name'] = self.pick_up_store_name.to_alipay_dict()
            else:
                params['pick_up_store_name'] = self.pick_up_store_name
        if self.plan_drop_off_time:
            if hasattr(self.plan_drop_off_time, 'to_alipay_dict'):
                params['plan_drop_off_time'] = self.plan_drop_off_time.to_alipay_dict()
            else:
                params['plan_drop_off_time'] = self.plan_drop_off_time
        if self.plan_pick_up_time:
            if hasattr(self.plan_pick_up_time, 'to_alipay_dict'):
                params['plan_pick_up_time'] = self.plan_pick_up_time.to_alipay_dict()
            else:
                params['plan_pick_up_time'] = self.plan_pick_up_time
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        if self.vehicle_color:
            if hasattr(self.vehicle_color, 'to_alipay_dict'):
                params['vehicle_color'] = self.vehicle_color.to_alipay_dict()
            else:
                params['vehicle_color'] = self.vehicle_color
        if self.vehicle_plate_no:
            if hasattr(self.vehicle_plate_no, 'to_alipay_dict'):
                params['vehicle_plate_no'] = self.vehicle_plate_no.to_alipay_dict()
            else:
                params['vehicle_plate_no'] = self.vehicle_plate_no
        if self.vehicle_seat_num:
            if hasattr(self.vehicle_seat_num, 'to_alipay_dict'):
                params['vehicle_seat_num'] = self.vehicle_seat_num.to_alipay_dict()
            else:
                params['vehicle_seat_num'] = self.vehicle_seat_num
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
        o = AlipayEcoMycarRentcarJvorderSyncModel()
        if 'actual_pick_up_time' in d:
            o.actual_pick_up_time = d['actual_pick_up_time']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'drop_off_store_name' in d:
            o.drop_off_store_name = d['drop_off_store_name']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'jv_discount_amount' in d:
            o.jv_discount_amount = d['jv_discount_amount']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_channel' in d:
            o.order_channel = d['order_channel']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'other_discount_amount' in d:
            o.other_discount_amount = d['other_discount_amount']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pick_up_store_name' in d:
            o.pick_up_store_name = d['pick_up_store_name']
        if 'plan_drop_off_time' in d:
            o.plan_drop_off_time = d['plan_drop_off_time']
        if 'plan_pick_up_time' in d:
            o.plan_pick_up_time = d['plan_pick_up_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vehicle_brand_name' in d:
            o.vehicle_brand_name = d['vehicle_brand_name']
        if 'vehicle_color' in d:
            o.vehicle_color = d['vehicle_color']
        if 'vehicle_plate_no' in d:
            o.vehicle_plate_no = d['vehicle_plate_no']
        if 'vehicle_seat_num' in d:
            o.vehicle_seat_num = d['vehicle_seat_num']
        if 'vehicle_series_name' in d:
            o.vehicle_series_name = d['vehicle_series_name']
        if 'vehicle_show_name' in d:
            o.vehicle_show_name = d['vehicle_show_name']
        return o


