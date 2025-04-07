#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityInfoModifyDTO import ActivityInfoModifyDTO
from alipay.aop.api.domain.MiniReceiverAddressInfoDTO import MiniReceiverAddressInfoDTO
from alipay.aop.api.domain.BookingInfoDTO import BookingInfoDTO
from alipay.aop.api.domain.ContactInfoDTO import ContactInfoDTO
from alipay.aop.api.domain.GoodsInfoModifyDTO import GoodsInfoModifyDTO
from alipay.aop.api.domain.PriceInfoModifyDTO import PriceInfoModifyDTO
from alipay.aop.api.domain.SendOrderContactInfoDTO import SendOrderContactInfoDTO
from alipay.aop.api.domain.TicketInfoModifyDTO import TicketInfoModifyDTO
from alipay.aop.api.domain.TourInfoDTO import TourInfoDTO


class AlipayOpenMiniOrderDeliveryModifyModel(object):

    def __init__(self):
        self._activity_infos = None
        self._address_info = None
        self._booking_info = None
        self._contact_info = None
        self._item_infos = None
        self._open_id = None
        self._order_id = None
        self._order_inspect_price = None
        self._out_order_id = None
        self._price_info = None
        self._reason_code = None
        self._send_order_contact_info = None
        self._status = None
        self._ticket_infos = None
        self._tour_info = None
        self._user_id = None

    @property
    def activity_infos(self):
        return self._activity_infos

    @activity_infos.setter
    def activity_infos(self, value):
        if isinstance(value, list):
            self._activity_infos = list()
            for i in value:
                if isinstance(i, ActivityInfoModifyDTO):
                    self._activity_infos.append(i)
                else:
                    self._activity_infos.append(ActivityInfoModifyDTO.from_alipay_dict(i))
    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, MiniReceiverAddressInfoDTO):
            self._address_info = value
        else:
            self._address_info = MiniReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def booking_info(self):
        return self._booking_info

    @booking_info.setter
    def booking_info(self, value):
        if isinstance(value, BookingInfoDTO):
            self._booking_info = value
        else:
            self._booking_info = BookingInfoDTO.from_alipay_dict(value)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, ContactInfoDTO):
            self._contact_info = value
        else:
            self._contact_info = ContactInfoDTO.from_alipay_dict(value)
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, GoodsInfoModifyDTO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(GoodsInfoModifyDTO.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_inspect_price(self):
        return self._order_inspect_price

    @order_inspect_price.setter
    def order_inspect_price(self, value):
        self._order_inspect_price = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, PriceInfoModifyDTO):
            self._price_info = value
        else:
            self._price_info = PriceInfoModifyDTO.from_alipay_dict(value)
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def send_order_contact_info(self):
        return self._send_order_contact_info

    @send_order_contact_info.setter
    def send_order_contact_info(self, value):
        if isinstance(value, SendOrderContactInfoDTO):
            self._send_order_contact_info = value
        else:
            self._send_order_contact_info = SendOrderContactInfoDTO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def ticket_infos(self):
        return self._ticket_infos

    @ticket_infos.setter
    def ticket_infos(self, value):
        if isinstance(value, list):
            self._ticket_infos = list()
            for i in value:
                if isinstance(i, TicketInfoModifyDTO):
                    self._ticket_infos.append(i)
                else:
                    self._ticket_infos.append(TicketInfoModifyDTO.from_alipay_dict(i))
    @property
    def tour_info(self):
        return self._tour_info

    @tour_info.setter
    def tour_info(self, value):
        if isinstance(value, TourInfoDTO):
            self._tour_info = value
        else:
            self._tour_info = TourInfoDTO.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_infos:
            if isinstance(self.activity_infos, list):
                for i in range(0, len(self.activity_infos)):
                    element = self.activity_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_infos[i] = element.to_alipay_dict()
            if hasattr(self.activity_infos, 'to_alipay_dict'):
                params['activity_infos'] = self.activity_infos.to_alipay_dict()
            else:
                params['activity_infos'] = self.activity_infos
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.booking_info:
            if hasattr(self.booking_info, 'to_alipay_dict'):
                params['booking_info'] = self.booking_info.to_alipay_dict()
            else:
                params['booking_info'] = self.booking_info
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_inspect_price:
            if hasattr(self.order_inspect_price, 'to_alipay_dict'):
                params['order_inspect_price'] = self.order_inspect_price.to_alipay_dict()
            else:
                params['order_inspect_price'] = self.order_inspect_price
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.send_order_contact_info:
            if hasattr(self.send_order_contact_info, 'to_alipay_dict'):
                params['send_order_contact_info'] = self.send_order_contact_info.to_alipay_dict()
            else:
                params['send_order_contact_info'] = self.send_order_contact_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.ticket_infos:
            if isinstance(self.ticket_infos, list):
                for i in range(0, len(self.ticket_infos)):
                    element = self.ticket_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ticket_infos[i] = element.to_alipay_dict()
            if hasattr(self.ticket_infos, 'to_alipay_dict'):
                params['ticket_infos'] = self.ticket_infos.to_alipay_dict()
            else:
                params['ticket_infos'] = self.ticket_infos
        if self.tour_info:
            if hasattr(self.tour_info, 'to_alipay_dict'):
                params['tour_info'] = self.tour_info.to_alipay_dict()
            else:
                params['tour_info'] = self.tour_info
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderDeliveryModifyModel()
        if 'activity_infos' in d:
            o.activity_infos = d['activity_infos']
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'booking_info' in d:
            o.booking_info = d['booking_info']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_inspect_price' in d:
            o.order_inspect_price = d['order_inspect_price']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'send_order_contact_info' in d:
            o.send_order_contact_info = d['send_order_contact_info']
        if 'status' in d:
            o.status = d['status']
        if 'ticket_infos' in d:
            o.ticket_infos = d['ticket_infos']
        if 'tour_info' in d:
            o.tour_info = d['tour_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


