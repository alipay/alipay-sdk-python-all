#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JourneyLocation import JourneyLocation
from alipay.aop.api.domain.JourneyLocation import JourneyLocation
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.FunctionalService import FunctionalService
from alipay.aop.api.domain.JourneyLocation import JourneyLocation
from alipay.aop.api.domain.SeatInfo import SeatInfo
from alipay.aop.api.domain.OrderParticipantInfo import OrderParticipantInfo
from alipay.aop.api.domain.OrderShopInfo import OrderShopInfo
from alipay.aop.api.domain.UserInfomation import UserInfomation
from alipay.aop.api.domain.OrderVehicleInfo import OrderVehicleInfo


class TicketOrderInfo(object):

    def __init__(self):
        self._arrival = None
        self._content = None
        self._departure = None
        self._effective_num = None
        self._end_time = None
        self._ext_info = None
        self._face_value = None
        self._functional_services = None
        self._invalid_reason = None
        self._locations = None
        self._merchant_ticket_no = None
        self._seat_infos = None
        self._service_provider = None
        self._shops = None
        self._start_time = None
        self._status = None
        self._ticket_create_time = None
        self._ticket_modify_time = None
        self._ticket_num = None
        self._ticket_users = None
        self._title = None
        self._vehicle_info = None

    @property
    def arrival(self):
        return self._arrival

    @arrival.setter
    def arrival(self, value):
        if isinstance(value, JourneyLocation):
            self._arrival = value
        else:
            self._arrival = JourneyLocation.from_alipay_dict(value)
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):
        if isinstance(value, JourneyLocation):
            self._departure = value
        else:
            self._departure = JourneyLocation.from_alipay_dict(value)
    @property
    def effective_num(self):
        return self._effective_num

    @effective_num.setter
    def effective_num(self, value):
        self._effective_num = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
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
    def face_value(self):
        return self._face_value

    @face_value.setter
    def face_value(self, value):
        self._face_value = value
    @property
    def functional_services(self):
        return self._functional_services

    @functional_services.setter
    def functional_services(self, value):
        if isinstance(value, list):
            self._functional_services = list()
            for i in value:
                if isinstance(i, FunctionalService):
                    self._functional_services.append(i)
                else:
                    self._functional_services.append(FunctionalService.from_alipay_dict(i))
    @property
    def invalid_reason(self):
        return self._invalid_reason

    @invalid_reason.setter
    def invalid_reason(self, value):
        self._invalid_reason = value
    @property
    def locations(self):
        return self._locations

    @locations.setter
    def locations(self, value):
        if isinstance(value, list):
            self._locations = list()
            for i in value:
                if isinstance(i, JourneyLocation):
                    self._locations.append(i)
                else:
                    self._locations.append(JourneyLocation.from_alipay_dict(i))
    @property
    def merchant_ticket_no(self):
        return self._merchant_ticket_no

    @merchant_ticket_no.setter
    def merchant_ticket_no(self, value):
        self._merchant_ticket_no = value
    @property
    def seat_infos(self):
        return self._seat_infos

    @seat_infos.setter
    def seat_infos(self, value):
        if isinstance(value, list):
            self._seat_infos = list()
            for i in value:
                if isinstance(i, SeatInfo):
                    self._seat_infos.append(i)
                else:
                    self._seat_infos.append(SeatInfo.from_alipay_dict(i))
    @property
    def service_provider(self):
        return self._service_provider

    @service_provider.setter
    def service_provider(self, value):
        if isinstance(value, OrderParticipantInfo):
            self._service_provider = value
        else:
            self._service_provider = OrderParticipantInfo.from_alipay_dict(value)
    @property
    def shops(self):
        return self._shops

    @shops.setter
    def shops(self, value):
        if isinstance(value, list):
            self._shops = list()
            for i in value:
                if isinstance(i, OrderShopInfo):
                    self._shops.append(i)
                else:
                    self._shops.append(OrderShopInfo.from_alipay_dict(i))
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
    def ticket_create_time(self):
        return self._ticket_create_time

    @ticket_create_time.setter
    def ticket_create_time(self, value):
        self._ticket_create_time = value
    @property
    def ticket_modify_time(self):
        return self._ticket_modify_time

    @ticket_modify_time.setter
    def ticket_modify_time(self, value):
        self._ticket_modify_time = value
    @property
    def ticket_num(self):
        return self._ticket_num

    @ticket_num.setter
    def ticket_num(self, value):
        self._ticket_num = value
    @property
    def ticket_users(self):
        return self._ticket_users

    @ticket_users.setter
    def ticket_users(self, value):
        if isinstance(value, list):
            self._ticket_users = list()
            for i in value:
                if isinstance(i, UserInfomation):
                    self._ticket_users.append(i)
                else:
                    self._ticket_users.append(UserInfomation.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def vehicle_info(self):
        return self._vehicle_info

    @vehicle_info.setter
    def vehicle_info(self, value):
        if isinstance(value, OrderVehicleInfo):
            self._vehicle_info = value
        else:
            self._vehicle_info = OrderVehicleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.arrival:
            if hasattr(self.arrival, 'to_alipay_dict'):
                params['arrival'] = self.arrival.to_alipay_dict()
            else:
                params['arrival'] = self.arrival
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.departure:
            if hasattr(self.departure, 'to_alipay_dict'):
                params['departure'] = self.departure.to_alipay_dict()
            else:
                params['departure'] = self.departure
        if self.effective_num:
            if hasattr(self.effective_num, 'to_alipay_dict'):
                params['effective_num'] = self.effective_num.to_alipay_dict()
            else:
                params['effective_num'] = self.effective_num
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
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
        if self.face_value:
            if hasattr(self.face_value, 'to_alipay_dict'):
                params['face_value'] = self.face_value.to_alipay_dict()
            else:
                params['face_value'] = self.face_value
        if self.functional_services:
            if isinstance(self.functional_services, list):
                for i in range(0, len(self.functional_services)):
                    element = self.functional_services[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.functional_services[i] = element.to_alipay_dict()
            if hasattr(self.functional_services, 'to_alipay_dict'):
                params['functional_services'] = self.functional_services.to_alipay_dict()
            else:
                params['functional_services'] = self.functional_services
        if self.invalid_reason:
            if hasattr(self.invalid_reason, 'to_alipay_dict'):
                params['invalid_reason'] = self.invalid_reason.to_alipay_dict()
            else:
                params['invalid_reason'] = self.invalid_reason
        if self.locations:
            if isinstance(self.locations, list):
                for i in range(0, len(self.locations)):
                    element = self.locations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.locations[i] = element.to_alipay_dict()
            if hasattr(self.locations, 'to_alipay_dict'):
                params['locations'] = self.locations.to_alipay_dict()
            else:
                params['locations'] = self.locations
        if self.merchant_ticket_no:
            if hasattr(self.merchant_ticket_no, 'to_alipay_dict'):
                params['merchant_ticket_no'] = self.merchant_ticket_no.to_alipay_dict()
            else:
                params['merchant_ticket_no'] = self.merchant_ticket_no
        if self.seat_infos:
            if isinstance(self.seat_infos, list):
                for i in range(0, len(self.seat_infos)):
                    element = self.seat_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.seat_infos[i] = element.to_alipay_dict()
            if hasattr(self.seat_infos, 'to_alipay_dict'):
                params['seat_infos'] = self.seat_infos.to_alipay_dict()
            else:
                params['seat_infos'] = self.seat_infos
        if self.service_provider:
            if hasattr(self.service_provider, 'to_alipay_dict'):
                params['service_provider'] = self.service_provider.to_alipay_dict()
            else:
                params['service_provider'] = self.service_provider
        if self.shops:
            if isinstance(self.shops, list):
                for i in range(0, len(self.shops)):
                    element = self.shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shops[i] = element.to_alipay_dict()
            if hasattr(self.shops, 'to_alipay_dict'):
                params['shops'] = self.shops.to_alipay_dict()
            else:
                params['shops'] = self.shops
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
        if self.ticket_create_time:
            if hasattr(self.ticket_create_time, 'to_alipay_dict'):
                params['ticket_create_time'] = self.ticket_create_time.to_alipay_dict()
            else:
                params['ticket_create_time'] = self.ticket_create_time
        if self.ticket_modify_time:
            if hasattr(self.ticket_modify_time, 'to_alipay_dict'):
                params['ticket_modify_time'] = self.ticket_modify_time.to_alipay_dict()
            else:
                params['ticket_modify_time'] = self.ticket_modify_time
        if self.ticket_num:
            if hasattr(self.ticket_num, 'to_alipay_dict'):
                params['ticket_num'] = self.ticket_num.to_alipay_dict()
            else:
                params['ticket_num'] = self.ticket_num
        if self.ticket_users:
            if isinstance(self.ticket_users, list):
                for i in range(0, len(self.ticket_users)):
                    element = self.ticket_users[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ticket_users[i] = element.to_alipay_dict()
            if hasattr(self.ticket_users, 'to_alipay_dict'):
                params['ticket_users'] = self.ticket_users.to_alipay_dict()
            else:
                params['ticket_users'] = self.ticket_users
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = TicketOrderInfo()
        if 'arrival' in d:
            o.arrival = d['arrival']
        if 'content' in d:
            o.content = d['content']
        if 'departure' in d:
            o.departure = d['departure']
        if 'effective_num' in d:
            o.effective_num = d['effective_num']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'face_value' in d:
            o.face_value = d['face_value']
        if 'functional_services' in d:
            o.functional_services = d['functional_services']
        if 'invalid_reason' in d:
            o.invalid_reason = d['invalid_reason']
        if 'locations' in d:
            o.locations = d['locations']
        if 'merchant_ticket_no' in d:
            o.merchant_ticket_no = d['merchant_ticket_no']
        if 'seat_infos' in d:
            o.seat_infos = d['seat_infos']
        if 'service_provider' in d:
            o.service_provider = d['service_provider']
        if 'shops' in d:
            o.shops = d['shops']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'ticket_create_time' in d:
            o.ticket_create_time = d['ticket_create_time']
        if 'ticket_modify_time' in d:
            o.ticket_modify_time = d['ticket_modify_time']
        if 'ticket_num' in d:
            o.ticket_num = d['ticket_num']
        if 'ticket_users' in d:
            o.ticket_users = d['ticket_users']
        if 'title' in d:
            o.title = d['title']
        if 'vehicle_info' in d:
            o.vehicle_info = d['vehicle_info']
        return o


