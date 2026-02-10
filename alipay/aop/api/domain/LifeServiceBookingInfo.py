#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LifeServiceAttr import LifeServiceAttr


class LifeServiceBookingInfo(object):

    def __init__(self):
        self._booking_attrs = None
        self._booking_create_time = None
        self._booking_date = None
        self._booking_id = None
        self._end_time = None
        self._item_id = None
        self._nick = None
        self._order_id = None
        self._out_item_id = None
        self._out_room_id = None
        self._out_service_id = None
        self._out_sku_id = None
        self._out_technician_id = None
        self._phone = None
        self._remark = None
        self._room_id = None
        self._service_id = None
        self._shop_id = None
        self._sku_id = None
        self._start_time = None
        self._status = None
        self._technician_id = None

    @property
    def booking_attrs(self):
        return self._booking_attrs

    @booking_attrs.setter
    def booking_attrs(self, value):
        if isinstance(value, list):
            self._booking_attrs = list()
            for i in value:
                if isinstance(i, LifeServiceAttr):
                    self._booking_attrs.append(i)
                else:
                    self._booking_attrs.append(LifeServiceAttr.from_alipay_dict(i))
    @property
    def booking_create_time(self):
        return self._booking_create_time

    @booking_create_time.setter
    def booking_create_time(self, value):
        self._booking_create_time = value
    @property
    def booking_date(self):
        return self._booking_date

    @booking_date.setter
    def booking_date(self, value):
        self._booking_date = value
    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, value):
        self._booking_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def out_service_id(self):
        return self._out_service_id

    @out_service_id.setter
    def out_service_id(self, value):
        self._out_service_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def out_technician_id(self):
        return self._out_technician_id

    @out_technician_id.setter
    def out_technician_id(self, value):
        self._out_technician_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def technician_id(self):
        return self._technician_id

    @technician_id.setter
    def technician_id(self, value):
        self._technician_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.booking_attrs:
            if isinstance(self.booking_attrs, list):
                for i in range(0, len(self.booking_attrs)):
                    element = self.booking_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.booking_attrs[i] = element.to_alipay_dict()
            if hasattr(self.booking_attrs, 'to_alipay_dict'):
                params['booking_attrs'] = self.booking_attrs.to_alipay_dict()
            else:
                params['booking_attrs'] = self.booking_attrs
        if self.booking_create_time:
            if hasattr(self.booking_create_time, 'to_alipay_dict'):
                params['booking_create_time'] = self.booking_create_time.to_alipay_dict()
            else:
                params['booking_create_time'] = self.booking_create_time
        if self.booking_date:
            if hasattr(self.booking_date, 'to_alipay_dict'):
                params['booking_date'] = self.booking_date.to_alipay_dict()
            else:
                params['booking_date'] = self.booking_date
        if self.booking_id:
            if hasattr(self.booking_id, 'to_alipay_dict'):
                params['booking_id'] = self.booking_id.to_alipay_dict()
            else:
                params['booking_id'] = self.booking_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.out_service_id:
            if hasattr(self.out_service_id, 'to_alipay_dict'):
                params['out_service_id'] = self.out_service_id.to_alipay_dict()
            else:
                params['out_service_id'] = self.out_service_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.out_technician_id:
            if hasattr(self.out_technician_id, 'to_alipay_dict'):
                params['out_technician_id'] = self.out_technician_id.to_alipay_dict()
            else:
                params['out_technician_id'] = self.out_technician_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.technician_id:
            if hasattr(self.technician_id, 'to_alipay_dict'):
                params['technician_id'] = self.technician_id.to_alipay_dict()
            else:
                params['technician_id'] = self.technician_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceBookingInfo()
        if 'booking_attrs' in d:
            o.booking_attrs = d['booking_attrs']
        if 'booking_create_time' in d:
            o.booking_create_time = d['booking_create_time']
        if 'booking_date' in d:
            o.booking_date = d['booking_date']
        if 'booking_id' in d:
            o.booking_id = d['booking_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'nick' in d:
            o.nick = d['nick']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'out_service_id' in d:
            o.out_service_id = d['out_service_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'out_technician_id' in d:
            o.out_technician_id = d['out_technician_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'remark' in d:
            o.remark = d['remark']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'technician_id' in d:
            o.technician_id = d['technician_id']
        return o


