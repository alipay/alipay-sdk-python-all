#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo
from alipay.aop.api.domain.ScenicTrafficUserInfo import ScenicTrafficUserInfo
from alipay.aop.api.domain.TrafficProductInfo import TrafficProductInfo


class ScenicTrafficTicketInfo(object):

    def __init__(self):
        self._check_time = None
        self._departure_outer_scenic_id = None
        self._destination_outer_scenic_id = None
        self._ext_info = None
        self._passengers = None
        self._pic = None
        self._product_info = None
        self._ticket_count = None
        self._ticket_name = None
        self._ticket_no = None
        self._ticket_specs = None
        self._ticket_status = None
        self._ticket_use_type = None
        self._use_end_time = None
        self._use_start_time = None

    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
    @property
    def departure_outer_scenic_id(self):
        return self._departure_outer_scenic_id

    @departure_outer_scenic_id.setter
    def departure_outer_scenic_id(self, value):
        self._departure_outer_scenic_id = value
    @property
    def destination_outer_scenic_id(self):
        return self._destination_outer_scenic_id

    @destination_outer_scenic_id.setter
    def destination_outer_scenic_id(self, value):
        self._destination_outer_scenic_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ScenicExtInfo):
            self._ext_info = value
        else:
            self._ext_info = ScenicExtInfo.from_alipay_dict(value)
    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        if isinstance(value, ScenicTrafficUserInfo):
            self._passengers = value
        else:
            self._passengers = ScenicTrafficUserInfo.from_alipay_dict(value)
    @property
    def pic(self):
        return self._pic

    @pic.setter
    def pic(self, value):
        self._pic = value
    @property
    def product_info(self):
        return self._product_info

    @product_info.setter
    def product_info(self, value):
        if isinstance(value, TrafficProductInfo):
            self._product_info = value
        else:
            self._product_info = TrafficProductInfo.from_alipay_dict(value)
    @property
    def ticket_count(self):
        return self._ticket_count

    @ticket_count.setter
    def ticket_count(self, value):
        self._ticket_count = value
    @property
    def ticket_name(self):
        return self._ticket_name

    @ticket_name.setter
    def ticket_name(self, value):
        self._ticket_name = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value
    @property
    def ticket_specs(self):
        return self._ticket_specs

    @ticket_specs.setter
    def ticket_specs(self, value):
        self._ticket_specs = value
    @property
    def ticket_status(self):
        return self._ticket_status

    @ticket_status.setter
    def ticket_status(self, value):
        self._ticket_status = value
    @property
    def ticket_use_type(self):
        return self._ticket_use_type

    @ticket_use_type.setter
    def ticket_use_type(self, value):
        self._ticket_use_type = value
    @property
    def use_end_time(self):
        return self._use_end_time

    @use_end_time.setter
    def use_end_time(self, value):
        self._use_end_time = value
    @property
    def use_start_time(self):
        return self._use_start_time

    @use_start_time.setter
    def use_start_time(self, value):
        self._use_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
        if self.departure_outer_scenic_id:
            if hasattr(self.departure_outer_scenic_id, 'to_alipay_dict'):
                params['departure_outer_scenic_id'] = self.departure_outer_scenic_id.to_alipay_dict()
            else:
                params['departure_outer_scenic_id'] = self.departure_outer_scenic_id
        if self.destination_outer_scenic_id:
            if hasattr(self.destination_outer_scenic_id, 'to_alipay_dict'):
                params['destination_outer_scenic_id'] = self.destination_outer_scenic_id.to_alipay_dict()
            else:
                params['destination_outer_scenic_id'] = self.destination_outer_scenic_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.passengers:
            if hasattr(self.passengers, 'to_alipay_dict'):
                params['passengers'] = self.passengers.to_alipay_dict()
            else:
                params['passengers'] = self.passengers
        if self.pic:
            if hasattr(self.pic, 'to_alipay_dict'):
                params['pic'] = self.pic.to_alipay_dict()
            else:
                params['pic'] = self.pic
        if self.product_info:
            if hasattr(self.product_info, 'to_alipay_dict'):
                params['product_info'] = self.product_info.to_alipay_dict()
            else:
                params['product_info'] = self.product_info
        if self.ticket_count:
            if hasattr(self.ticket_count, 'to_alipay_dict'):
                params['ticket_count'] = self.ticket_count.to_alipay_dict()
            else:
                params['ticket_count'] = self.ticket_count
        if self.ticket_name:
            if hasattr(self.ticket_name, 'to_alipay_dict'):
                params['ticket_name'] = self.ticket_name.to_alipay_dict()
            else:
                params['ticket_name'] = self.ticket_name
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
        if self.ticket_specs:
            if hasattr(self.ticket_specs, 'to_alipay_dict'):
                params['ticket_specs'] = self.ticket_specs.to_alipay_dict()
            else:
                params['ticket_specs'] = self.ticket_specs
        if self.ticket_status:
            if hasattr(self.ticket_status, 'to_alipay_dict'):
                params['ticket_status'] = self.ticket_status.to_alipay_dict()
            else:
                params['ticket_status'] = self.ticket_status
        if self.ticket_use_type:
            if hasattr(self.ticket_use_type, 'to_alipay_dict'):
                params['ticket_use_type'] = self.ticket_use_type.to_alipay_dict()
            else:
                params['ticket_use_type'] = self.ticket_use_type
        if self.use_end_time:
            if hasattr(self.use_end_time, 'to_alipay_dict'):
                params['use_end_time'] = self.use_end_time.to_alipay_dict()
            else:
                params['use_end_time'] = self.use_end_time
        if self.use_start_time:
            if hasattr(self.use_start_time, 'to_alipay_dict'):
                params['use_start_time'] = self.use_start_time.to_alipay_dict()
            else:
                params['use_start_time'] = self.use_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicTrafficTicketInfo()
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'departure_outer_scenic_id' in d:
            o.departure_outer_scenic_id = d['departure_outer_scenic_id']
        if 'destination_outer_scenic_id' in d:
            o.destination_outer_scenic_id = d['destination_outer_scenic_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'passengers' in d:
            o.passengers = d['passengers']
        if 'pic' in d:
            o.pic = d['pic']
        if 'product_info' in d:
            o.product_info = d['product_info']
        if 'ticket_count' in d:
            o.ticket_count = d['ticket_count']
        if 'ticket_name' in d:
            o.ticket_name = d['ticket_name']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        if 'ticket_specs' in d:
            o.ticket_specs = d['ticket_specs']
        if 'ticket_status' in d:
            o.ticket_status = d['ticket_status']
        if 'ticket_use_type' in d:
            o.ticket_use_type = d['ticket_use_type']
        if 'use_end_time' in d:
            o.use_end_time = d['use_end_time']
        if 'use_start_time' in d:
            o.use_start_time = d['use_start_time']
        return o


