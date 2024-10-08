#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrafficAirticketOrderCommodityInfo import TrafficAirticketOrderCommodityInfo
from alipay.aop.api.domain.TrafficAirticketOrderSegmentInfo import TrafficAirticketOrderSegmentInfo


class TrafficAirticketOrderVoyageInfo(object):

    def __init__(self):
        self._commodity_info_list = None
        self._end_airport_code = None
        self._end_airport_name = None
        self._end_city_code = None
        self._end_city_name = None
        self._end_time = None
        self._international = None
        self._segment_info_list = None
        self._start_airport_code = None
        self._start_airport_name = None
        self._start_city_code = None
        self._start_city_name = None
        self._start_time = None
        self._transfer = None
        self._voyage_order = None

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
    def end_airport_code(self):
        return self._end_airport_code

    @end_airport_code.setter
    def end_airport_code(self, value):
        self._end_airport_code = value
    @property
    def end_airport_name(self):
        return self._end_airport_name

    @end_airport_name.setter
    def end_airport_name(self, value):
        self._end_airport_name = value
    @property
    def end_city_code(self):
        return self._end_city_code

    @end_city_code.setter
    def end_city_code(self, value):
        self._end_city_code = value
    @property
    def end_city_name(self):
        return self._end_city_name

    @end_city_name.setter
    def end_city_name(self, value):
        self._end_city_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def international(self):
        return self._international

    @international.setter
    def international(self, value):
        self._international = value
    @property
    def segment_info_list(self):
        return self._segment_info_list

    @segment_info_list.setter
    def segment_info_list(self, value):
        if isinstance(value, list):
            self._segment_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderSegmentInfo):
                    self._segment_info_list.append(i)
                else:
                    self._segment_info_list.append(TrafficAirticketOrderSegmentInfo.from_alipay_dict(i))
    @property
    def start_airport_code(self):
        return self._start_airport_code

    @start_airport_code.setter
    def start_airport_code(self, value):
        self._start_airport_code = value
    @property
    def start_airport_name(self):
        return self._start_airport_name

    @start_airport_name.setter
    def start_airport_name(self, value):
        self._start_airport_name = value
    @property
    def start_city_code(self):
        return self._start_city_code

    @start_city_code.setter
    def start_city_code(self, value):
        self._start_city_code = value
    @property
    def start_city_name(self):
        return self._start_city_name

    @start_city_name.setter
    def start_city_name(self, value):
        self._start_city_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def transfer(self):
        return self._transfer

    @transfer.setter
    def transfer(self, value):
        self._transfer = value
    @property
    def voyage_order(self):
        return self._voyage_order

    @voyage_order.setter
    def voyage_order(self, value):
        self._voyage_order = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.end_airport_code:
            if hasattr(self.end_airport_code, 'to_alipay_dict'):
                params['end_airport_code'] = self.end_airport_code.to_alipay_dict()
            else:
                params['end_airport_code'] = self.end_airport_code
        if self.end_airport_name:
            if hasattr(self.end_airport_name, 'to_alipay_dict'):
                params['end_airport_name'] = self.end_airport_name.to_alipay_dict()
            else:
                params['end_airport_name'] = self.end_airport_name
        if self.end_city_code:
            if hasattr(self.end_city_code, 'to_alipay_dict'):
                params['end_city_code'] = self.end_city_code.to_alipay_dict()
            else:
                params['end_city_code'] = self.end_city_code
        if self.end_city_name:
            if hasattr(self.end_city_name, 'to_alipay_dict'):
                params['end_city_name'] = self.end_city_name.to_alipay_dict()
            else:
                params['end_city_name'] = self.end_city_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.international:
            if hasattr(self.international, 'to_alipay_dict'):
                params['international'] = self.international.to_alipay_dict()
            else:
                params['international'] = self.international
        if self.segment_info_list:
            if isinstance(self.segment_info_list, list):
                for i in range(0, len(self.segment_info_list)):
                    element = self.segment_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.segment_info_list[i] = element.to_alipay_dict()
            if hasattr(self.segment_info_list, 'to_alipay_dict'):
                params['segment_info_list'] = self.segment_info_list.to_alipay_dict()
            else:
                params['segment_info_list'] = self.segment_info_list
        if self.start_airport_code:
            if hasattr(self.start_airport_code, 'to_alipay_dict'):
                params['start_airport_code'] = self.start_airport_code.to_alipay_dict()
            else:
                params['start_airport_code'] = self.start_airport_code
        if self.start_airport_name:
            if hasattr(self.start_airport_name, 'to_alipay_dict'):
                params['start_airport_name'] = self.start_airport_name.to_alipay_dict()
            else:
                params['start_airport_name'] = self.start_airport_name
        if self.start_city_code:
            if hasattr(self.start_city_code, 'to_alipay_dict'):
                params['start_city_code'] = self.start_city_code.to_alipay_dict()
            else:
                params['start_city_code'] = self.start_city_code
        if self.start_city_name:
            if hasattr(self.start_city_name, 'to_alipay_dict'):
                params['start_city_name'] = self.start_city_name.to_alipay_dict()
            else:
                params['start_city_name'] = self.start_city_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.transfer:
            if hasattr(self.transfer, 'to_alipay_dict'):
                params['transfer'] = self.transfer.to_alipay_dict()
            else:
                params['transfer'] = self.transfer
        if self.voyage_order:
            if hasattr(self.voyage_order, 'to_alipay_dict'):
                params['voyage_order'] = self.voyage_order.to_alipay_dict()
            else:
                params['voyage_order'] = self.voyage_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficAirticketOrderVoyageInfo()
        if 'commodity_info_list' in d:
            o.commodity_info_list = d['commodity_info_list']
        if 'end_airport_code' in d:
            o.end_airport_code = d['end_airport_code']
        if 'end_airport_name' in d:
            o.end_airport_name = d['end_airport_name']
        if 'end_city_code' in d:
            o.end_city_code = d['end_city_code']
        if 'end_city_name' in d:
            o.end_city_name = d['end_city_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'international' in d:
            o.international = d['international']
        if 'segment_info_list' in d:
            o.segment_info_list = d['segment_info_list']
        if 'start_airport_code' in d:
            o.start_airport_code = d['start_airport_code']
        if 'start_airport_name' in d:
            o.start_airport_name = d['start_airport_name']
        if 'start_city_code' in d:
            o.start_city_code = d['start_city_code']
        if 'start_city_name' in d:
            o.start_city_name = d['start_city_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'transfer' in d:
            o.transfer = d['transfer']
        if 'voyage_order' in d:
            o.voyage_order = d['voyage_order']
        return o


