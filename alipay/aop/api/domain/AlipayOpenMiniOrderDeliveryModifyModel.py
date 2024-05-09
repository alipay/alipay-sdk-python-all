#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityInfoModifyDTO import ActivityInfoModifyDTO
from alipay.aop.api.domain.BookingInfoDTO import BookingInfoDTO
from alipay.aop.api.domain.ContactInfoDTO import ContactInfoDTO
from alipay.aop.api.domain.TicketInfoModifyDTO import TicketInfoModifyDTO
from alipay.aop.api.domain.TourInfoDTO import TourInfoDTO


class AlipayOpenMiniOrderDeliveryModifyModel(object):

    def __init__(self):
        self._activity_infos = None
        self._booking_info = None
        self._contact_info = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
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
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
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
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
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
        if 'booking_info' in d:
            o.booking_info = d['booking_info']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'status' in d:
            o.status = d['status']
        if 'ticket_infos' in d:
            o.ticket_infos = d['ticket_infos']
        if 'tour_info' in d:
            o.tour_info = d['tour_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


