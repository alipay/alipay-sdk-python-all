#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BidDetailVO(object):

    def __init__(self):
        self._bid_close_date = None
        self._bid_lasts_day = None
        self._bid_name = None
        self._bid_no = None
        self._bid_open_date = None
        self._bid_type = None
        self._location_code = None
        self._location_name = None
        self._location_place = None

    @property
    def bid_close_date(self):
        return self._bid_close_date

    @bid_close_date.setter
    def bid_close_date(self, value):
        self._bid_close_date = value
    @property
    def bid_lasts_day(self):
        return self._bid_lasts_day

    @bid_lasts_day.setter
    def bid_lasts_day(self, value):
        self._bid_lasts_day = value
    @property
    def bid_name(self):
        return self._bid_name

    @bid_name.setter
    def bid_name(self, value):
        self._bid_name = value
    @property
    def bid_no(self):
        return self._bid_no

    @bid_no.setter
    def bid_no(self, value):
        self._bid_no = value
    @property
    def bid_open_date(self):
        return self._bid_open_date

    @bid_open_date.setter
    def bid_open_date(self, value):
        self._bid_open_date = value
    @property
    def bid_type(self):
        return self._bid_type

    @bid_type.setter
    def bid_type(self, value):
        self._bid_type = value
    @property
    def location_code(self):
        return self._location_code

    @location_code.setter
    def location_code(self, value):
        self._location_code = value
    @property
    def location_name(self):
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        self._location_name = value
    @property
    def location_place(self):
        return self._location_place

    @location_place.setter
    def location_place(self, value):
        self._location_place = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid_close_date:
            if hasattr(self.bid_close_date, 'to_alipay_dict'):
                params['bid_close_date'] = self.bid_close_date.to_alipay_dict()
            else:
                params['bid_close_date'] = self.bid_close_date
        if self.bid_lasts_day:
            if hasattr(self.bid_lasts_day, 'to_alipay_dict'):
                params['bid_lasts_day'] = self.bid_lasts_day.to_alipay_dict()
            else:
                params['bid_lasts_day'] = self.bid_lasts_day
        if self.bid_name:
            if hasattr(self.bid_name, 'to_alipay_dict'):
                params['bid_name'] = self.bid_name.to_alipay_dict()
            else:
                params['bid_name'] = self.bid_name
        if self.bid_no:
            if hasattr(self.bid_no, 'to_alipay_dict'):
                params['bid_no'] = self.bid_no.to_alipay_dict()
            else:
                params['bid_no'] = self.bid_no
        if self.bid_open_date:
            if hasattr(self.bid_open_date, 'to_alipay_dict'):
                params['bid_open_date'] = self.bid_open_date.to_alipay_dict()
            else:
                params['bid_open_date'] = self.bid_open_date
        if self.bid_type:
            if hasattr(self.bid_type, 'to_alipay_dict'):
                params['bid_type'] = self.bid_type.to_alipay_dict()
            else:
                params['bid_type'] = self.bid_type
        if self.location_code:
            if hasattr(self.location_code, 'to_alipay_dict'):
                params['location_code'] = self.location_code.to_alipay_dict()
            else:
                params['location_code'] = self.location_code
        if self.location_name:
            if hasattr(self.location_name, 'to_alipay_dict'):
                params['location_name'] = self.location_name.to_alipay_dict()
            else:
                params['location_name'] = self.location_name
        if self.location_place:
            if hasattr(self.location_place, 'to_alipay_dict'):
                params['location_place'] = self.location_place.to_alipay_dict()
            else:
                params['location_place'] = self.location_place
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BidDetailVO()
        if 'bid_close_date' in d:
            o.bid_close_date = d['bid_close_date']
        if 'bid_lasts_day' in d:
            o.bid_lasts_day = d['bid_lasts_day']
        if 'bid_name' in d:
            o.bid_name = d['bid_name']
        if 'bid_no' in d:
            o.bid_no = d['bid_no']
        if 'bid_open_date' in d:
            o.bid_open_date = d['bid_open_date']
        if 'bid_type' in d:
            o.bid_type = d['bid_type']
        if 'location_code' in d:
            o.location_code = d['location_code']
        if 'location_name' in d:
            o.location_name = d['location_name']
        if 'location_place' in d:
            o.location_place = d['location_place']
        return o


