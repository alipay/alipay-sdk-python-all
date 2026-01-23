#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentServiceTicketReceiverAddressInfoDTO import RentServiceTicketReceiverAddressInfoDTO


class RentServiceTicketInfo(object):

    def __init__(self):
        self._address_info = None
        self._biz_main_status = None
        self._biz_sub_status = None
        self._create_time = None
        self._service_ticket_id = None
        self._type = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RentServiceTicketReceiverAddressInfoDTO):
            self._address_info = value
        else:
            self._address_info = RentServiceTicketReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def biz_main_status(self):
        return self._biz_main_status

    @biz_main_status.setter
    def biz_main_status(self, value):
        self._biz_main_status = value
    @property
    def biz_sub_status(self):
        return self._biz_sub_status

    @biz_sub_status.setter
    def biz_sub_status(self, value):
        self._biz_sub_status = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def service_ticket_id(self):
        return self._service_ticket_id

    @service_ticket_id.setter
    def service_ticket_id(self, value):
        self._service_ticket_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.biz_main_status:
            if hasattr(self.biz_main_status, 'to_alipay_dict'):
                params['biz_main_status'] = self.biz_main_status.to_alipay_dict()
            else:
                params['biz_main_status'] = self.biz_main_status
        if self.biz_sub_status:
            if hasattr(self.biz_sub_status, 'to_alipay_dict'):
                params['biz_sub_status'] = self.biz_sub_status.to_alipay_dict()
            else:
                params['biz_sub_status'] = self.biz_sub_status
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.service_ticket_id:
            if hasattr(self.service_ticket_id, 'to_alipay_dict'):
                params['service_ticket_id'] = self.service_ticket_id.to_alipay_dict()
            else:
                params['service_ticket_id'] = self.service_ticket_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentServiceTicketInfo()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'biz_main_status' in d:
            o.biz_main_status = d['biz_main_status']
        if 'biz_sub_status' in d:
            o.biz_sub_status = d['biz_sub_status']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'service_ticket_id' in d:
            o.service_ticket_id = d['service_ticket_id']
        if 'type' in d:
            o.type = d['type']
        return o


