#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrafficAirticketOrderCommodityInfo import TrafficAirticketOrderCommodityInfo
from alipay.aop.api.domain.TrafficAirticketOrderVoyageInfo import TrafficAirticketOrderVoyageInfo


class TrafficAirticketOrderPassengerInfo(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._commodity_info_list = None
        self._mobile = None
        self._name = None
        self._passenger_uuid = None
        self._self = None
        self._voyage_info_list = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def commodity_info_list(self):
        return self._commodity_info_list

    @commodity_info_list.setter
    def commodity_info_list(self, value):
        if isinstance(value, list):
            self._commodity_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderCommodityInfo):
                    self._commodity_info_list.append(i)
                else:
                    self._commodity_info_list.append(TrafficAirticketOrderCommodityInfo.from_alipay_dict(i))
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def passenger_uuid(self):
        return self._passenger_uuid

    @passenger_uuid.setter
    def passenger_uuid(self, value):
        self._passenger_uuid = value
    @property
    def self(self):
        return self._self

    @self.setter
    def self(self, value):
        self._self = value
    @property
    def voyage_info_list(self):
        return self._voyage_info_list

    @voyage_info_list.setter
    def voyage_info_list(self, value):
        if isinstance(value, list):
            self._voyage_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderVoyageInfo):
                    self._voyage_info_list.append(i)
                else:
                    self._voyage_info_list.append(TrafficAirticketOrderVoyageInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.commodity_info_list:
            if isinstance(self.commodity_info_list, list):
                for i in range(0, len(self.commodity_info_list)):
                    element = self.commodity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commodity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.commodity_info_list, 'to_alipay_dict'):
                params['commodity_info_list'] = self.commodity_info_list.to_alipay_dict()
            else:
                params['commodity_info_list'] = self.commodity_info_list
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.passenger_uuid:
            if hasattr(self.passenger_uuid, 'to_alipay_dict'):
                params['passenger_uuid'] = self.passenger_uuid.to_alipay_dict()
            else:
                params['passenger_uuid'] = self.passenger_uuid
        if self.self:
            if hasattr(self.self, 'to_alipay_dict'):
                params['self'] = self.self.to_alipay_dict()
            else:
                params['self'] = self.self
        if self.voyage_info_list:
            if isinstance(self.voyage_info_list, list):
                for i in range(0, len(self.voyage_info_list)):
                    element = self.voyage_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voyage_info_list[i] = element.to_alipay_dict()
            if hasattr(self.voyage_info_list, 'to_alipay_dict'):
                params['voyage_info_list'] = self.voyage_info_list.to_alipay_dict()
            else:
                params['voyage_info_list'] = self.voyage_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficAirticketOrderPassengerInfo()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'commodity_info_list' in d:
            o.commodity_info_list = d['commodity_info_list']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'passenger_uuid' in d:
            o.passenger_uuid = d['passenger_uuid']
        if 'self' in d:
            o.self = d['self']
        if 'voyage_info_list' in d:
            o.voyage_info_list = d['voyage_info_list']
        return o


