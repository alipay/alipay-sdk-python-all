#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JourneyLocation import JourneyLocation
from alipay.aop.api.domain.JourneyLocation import JourneyLocation
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.FunctionalService import FunctionalService
from alipay.aop.api.domain.UserInfomation import UserInfomation
from alipay.aop.api.domain.JourneyServiceChangeInfo import JourneyServiceChangeInfo
from alipay.aop.api.domain.JourneyMerchantInfo import JourneyMerchantInfo


class OrderJourneyElement(object):

    def __init__(self):
        self._arrival = None
        self._departure = None
        self._duration = None
        self._end_time = None
        self._end_time_desc = None
        self._ext_info = None
        self._functional_services = None
        self._passagers = None
        self._service_change_info = None
        self._service_provider = None
        self._start_time = None
        self._start_time_desc = None

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
    def departure(self):
        return self._departure

    @departure.setter
    def departure(self, value):
        if isinstance(value, JourneyLocation):
            self._departure = value
        else:
            self._departure = JourneyLocation.from_alipay_dict(value)
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def end_time_desc(self):
        return self._end_time_desc

    @end_time_desc.setter
    def end_time_desc(self, value):
        self._end_time_desc = value
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
    def passagers(self):
        return self._passagers

    @passagers.setter
    def passagers(self, value):
        if isinstance(value, list):
            self._passagers = list()
            for i in value:
                if isinstance(i, UserInfomation):
                    self._passagers.append(i)
                else:
                    self._passagers.append(UserInfomation.from_alipay_dict(i))
    @property
    def service_change_info(self):
        return self._service_change_info

    @service_change_info.setter
    def service_change_info(self, value):
        if isinstance(value, JourneyServiceChangeInfo):
            self._service_change_info = value
        else:
            self._service_change_info = JourneyServiceChangeInfo.from_alipay_dict(value)
    @property
    def service_provider(self):
        return self._service_provider

    @service_provider.setter
    def service_provider(self, value):
        if isinstance(value, JourneyMerchantInfo):
            self._service_provider = value
        else:
            self._service_provider = JourneyMerchantInfo.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def start_time_desc(self):
        return self._start_time_desc

    @start_time_desc.setter
    def start_time_desc(self, value):
        self._start_time_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrival:
            if hasattr(self.arrival, 'to_alipay_dict'):
                params['arrival'] = self.arrival.to_alipay_dict()
            else:
                params['arrival'] = self.arrival
        if self.departure:
            if hasattr(self.departure, 'to_alipay_dict'):
                params['departure'] = self.departure.to_alipay_dict()
            else:
                params['departure'] = self.departure
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.end_time_desc:
            if hasattr(self.end_time_desc, 'to_alipay_dict'):
                params['end_time_desc'] = self.end_time_desc.to_alipay_dict()
            else:
                params['end_time_desc'] = self.end_time_desc
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
        if self.passagers:
            if isinstance(self.passagers, list):
                for i in range(0, len(self.passagers)):
                    element = self.passagers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passagers[i] = element.to_alipay_dict()
            if hasattr(self.passagers, 'to_alipay_dict'):
                params['passagers'] = self.passagers.to_alipay_dict()
            else:
                params['passagers'] = self.passagers
        if self.service_change_info:
            if hasattr(self.service_change_info, 'to_alipay_dict'):
                params['service_change_info'] = self.service_change_info.to_alipay_dict()
            else:
                params['service_change_info'] = self.service_change_info
        if self.service_provider:
            if hasattr(self.service_provider, 'to_alipay_dict'):
                params['service_provider'] = self.service_provider.to_alipay_dict()
            else:
                params['service_provider'] = self.service_provider
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.start_time_desc:
            if hasattr(self.start_time_desc, 'to_alipay_dict'):
                params['start_time_desc'] = self.start_time_desc.to_alipay_dict()
            else:
                params['start_time_desc'] = self.start_time_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderJourneyElement()
        if 'arrival' in d:
            o.arrival = d['arrival']
        if 'departure' in d:
            o.departure = d['departure']
        if 'duration' in d:
            o.duration = d['duration']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'end_time_desc' in d:
            o.end_time_desc = d['end_time_desc']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'functional_services' in d:
            o.functional_services = d['functional_services']
        if 'passagers' in d:
            o.passagers = d['passagers']
        if 'service_change_info' in d:
            o.service_change_info = d['service_change_info']
        if 'service_provider' in d:
            o.service_provider = d['service_provider']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'start_time_desc' in d:
            o.start_time_desc = d['start_time_desc']
        return o


