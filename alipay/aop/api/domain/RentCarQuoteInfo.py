#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarQuoteInfo(object):

    def __init__(self):
        self._amt_rank_sort = None
        self._car_type = None
        self._diff_adv_quote_amt = None
        self._end_address = None
        self._end_city_name = None
        self._end_latitude = None
        self._end_longitude = None
        self._end_time = None
        self._isv_name = None
        self._sku_actual_amt = None
        self._sku_avg_amt = None
        self._sku_id = None
        self._sku_sname = None
        self._sku_total_amt = None
        self._spu_id = None
        self._spu_name = None
        self._start_address = None
        self._start_city_name = None
        self._start_latitude = None
        self._start_longitude = None
        self._start_time = None
        self._trace_datetime = None

    @property
    def amt_rank_sort(self):
        return self._amt_rank_sort

    @amt_rank_sort.setter
    def amt_rank_sort(self, value):
        self._amt_rank_sort = value
    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def diff_adv_quote_amt(self):
        return self._diff_adv_quote_amt

    @diff_adv_quote_amt.setter
    def diff_adv_quote_amt(self, value):
        self._diff_adv_quote_amt = value
    @property
    def end_address(self):
        return self._end_address

    @end_address.setter
    def end_address(self, value):
        self._end_address = value
    @property
    def end_city_name(self):
        return self._end_city_name

    @end_city_name.setter
    def end_city_name(self, value):
        self._end_city_name = value
    @property
    def end_latitude(self):
        return self._end_latitude

    @end_latitude.setter
    def end_latitude(self, value):
        self._end_latitude = value
    @property
    def end_longitude(self):
        return self._end_longitude

    @end_longitude.setter
    def end_longitude(self, value):
        self._end_longitude = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def sku_actual_amt(self):
        return self._sku_actual_amt

    @sku_actual_amt.setter
    def sku_actual_amt(self, value):
        self._sku_actual_amt = value
    @property
    def sku_avg_amt(self):
        return self._sku_avg_amt

    @sku_avg_amt.setter
    def sku_avg_amt(self, value):
        self._sku_avg_amt = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_sname(self):
        return self._sku_sname

    @sku_sname.setter
    def sku_sname(self, value):
        self._sku_sname = value
    @property
    def sku_total_amt(self):
        return self._sku_total_amt

    @sku_total_amt.setter
    def sku_total_amt(self, value):
        self._sku_total_amt = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def spu_name(self):
        return self._spu_name

    @spu_name.setter
    def spu_name(self, value):
        self._spu_name = value
    @property
    def start_address(self):
        return self._start_address

    @start_address.setter
    def start_address(self, value):
        self._start_address = value
    @property
    def start_city_name(self):
        return self._start_city_name

    @start_city_name.setter
    def start_city_name(self, value):
        self._start_city_name = value
    @property
    def start_latitude(self):
        return self._start_latitude

    @start_latitude.setter
    def start_latitude(self, value):
        self._start_latitude = value
    @property
    def start_longitude(self):
        return self._start_longitude

    @start_longitude.setter
    def start_longitude(self, value):
        self._start_longitude = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def trace_datetime(self):
        return self._trace_datetime

    @trace_datetime.setter
    def trace_datetime(self, value):
        self._trace_datetime = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt_rank_sort:
            if hasattr(self.amt_rank_sort, 'to_alipay_dict'):
                params['amt_rank_sort'] = self.amt_rank_sort.to_alipay_dict()
            else:
                params['amt_rank_sort'] = self.amt_rank_sort
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.diff_adv_quote_amt:
            if hasattr(self.diff_adv_quote_amt, 'to_alipay_dict'):
                params['diff_adv_quote_amt'] = self.diff_adv_quote_amt.to_alipay_dict()
            else:
                params['diff_adv_quote_amt'] = self.diff_adv_quote_amt
        if self.end_address:
            if hasattr(self.end_address, 'to_alipay_dict'):
                params['end_address'] = self.end_address.to_alipay_dict()
            else:
                params['end_address'] = self.end_address
        if self.end_city_name:
            if hasattr(self.end_city_name, 'to_alipay_dict'):
                params['end_city_name'] = self.end_city_name.to_alipay_dict()
            else:
                params['end_city_name'] = self.end_city_name
        if self.end_latitude:
            if hasattr(self.end_latitude, 'to_alipay_dict'):
                params['end_latitude'] = self.end_latitude.to_alipay_dict()
            else:
                params['end_latitude'] = self.end_latitude
        if self.end_longitude:
            if hasattr(self.end_longitude, 'to_alipay_dict'):
                params['end_longitude'] = self.end_longitude.to_alipay_dict()
            else:
                params['end_longitude'] = self.end_longitude
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.sku_actual_amt:
            if hasattr(self.sku_actual_amt, 'to_alipay_dict'):
                params['sku_actual_amt'] = self.sku_actual_amt.to_alipay_dict()
            else:
                params['sku_actual_amt'] = self.sku_actual_amt
        if self.sku_avg_amt:
            if hasattr(self.sku_avg_amt, 'to_alipay_dict'):
                params['sku_avg_amt'] = self.sku_avg_amt.to_alipay_dict()
            else:
                params['sku_avg_amt'] = self.sku_avg_amt
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_sname:
            if hasattr(self.sku_sname, 'to_alipay_dict'):
                params['sku_sname'] = self.sku_sname.to_alipay_dict()
            else:
                params['sku_sname'] = self.sku_sname
        if self.sku_total_amt:
            if hasattr(self.sku_total_amt, 'to_alipay_dict'):
                params['sku_total_amt'] = self.sku_total_amt.to_alipay_dict()
            else:
                params['sku_total_amt'] = self.sku_total_amt
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.spu_name:
            if hasattr(self.spu_name, 'to_alipay_dict'):
                params['spu_name'] = self.spu_name.to_alipay_dict()
            else:
                params['spu_name'] = self.spu_name
        if self.start_address:
            if hasattr(self.start_address, 'to_alipay_dict'):
                params['start_address'] = self.start_address.to_alipay_dict()
            else:
                params['start_address'] = self.start_address
        if self.start_city_name:
            if hasattr(self.start_city_name, 'to_alipay_dict'):
                params['start_city_name'] = self.start_city_name.to_alipay_dict()
            else:
                params['start_city_name'] = self.start_city_name
        if self.start_latitude:
            if hasattr(self.start_latitude, 'to_alipay_dict'):
                params['start_latitude'] = self.start_latitude.to_alipay_dict()
            else:
                params['start_latitude'] = self.start_latitude
        if self.start_longitude:
            if hasattr(self.start_longitude, 'to_alipay_dict'):
                params['start_longitude'] = self.start_longitude.to_alipay_dict()
            else:
                params['start_longitude'] = self.start_longitude
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.trace_datetime:
            if hasattr(self.trace_datetime, 'to_alipay_dict'):
                params['trace_datetime'] = self.trace_datetime.to_alipay_dict()
            else:
                params['trace_datetime'] = self.trace_datetime
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarQuoteInfo()
        if 'amt_rank_sort' in d:
            o.amt_rank_sort = d['amt_rank_sort']
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'diff_adv_quote_amt' in d:
            o.diff_adv_quote_amt = d['diff_adv_quote_amt']
        if 'end_address' in d:
            o.end_address = d['end_address']
        if 'end_city_name' in d:
            o.end_city_name = d['end_city_name']
        if 'end_latitude' in d:
            o.end_latitude = d['end_latitude']
        if 'end_longitude' in d:
            o.end_longitude = d['end_longitude']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'sku_actual_amt' in d:
            o.sku_actual_amt = d['sku_actual_amt']
        if 'sku_avg_amt' in d:
            o.sku_avg_amt = d['sku_avg_amt']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_sname' in d:
            o.sku_sname = d['sku_sname']
        if 'sku_total_amt' in d:
            o.sku_total_amt = d['sku_total_amt']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'spu_name' in d:
            o.spu_name = d['spu_name']
        if 'start_address' in d:
            o.start_address = d['start_address']
        if 'start_city_name' in d:
            o.start_city_name = d['start_city_name']
        if 'start_latitude' in d:
            o.start_latitude = d['start_latitude']
        if 'start_longitude' in d:
            o.start_longitude = d['start_longitude']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'trace_datetime' in d:
            o.trace_datetime = d['trace_datetime']
        return o


