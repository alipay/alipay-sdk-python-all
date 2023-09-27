#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShareAirline import ShareAirline
from alipay.aop.api.domain.StopInfo import StopInfo


class Airline(object):

    def __init__(self):
        self._ac_code = None
        self._ac_name = None
        self._flight_no = None
        self._is_share = None
        self._is_stop = None
        self._plane_model = None
        self._plane_model_size = None
        self._share_airline = None
        self._stop_info = None

    @property
    def ac_code(self):
        return self._ac_code

    @ac_code.setter
    def ac_code(self, value):
        self._ac_code = value
    @property
    def ac_name(self):
        return self._ac_name

    @ac_name.setter
    def ac_name(self, value):
        self._ac_name = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        self._flight_no = value
    @property
    def is_share(self):
        return self._is_share

    @is_share.setter
    def is_share(self, value):
        self._is_share = value
    @property
    def is_stop(self):
        return self._is_stop

    @is_stop.setter
    def is_stop(self, value):
        self._is_stop = value
    @property
    def plane_model(self):
        return self._plane_model

    @plane_model.setter
    def plane_model(self, value):
        self._plane_model = value
    @property
    def plane_model_size(self):
        return self._plane_model_size

    @plane_model_size.setter
    def plane_model_size(self, value):
        self._plane_model_size = value
    @property
    def share_airline(self):
        return self._share_airline

    @share_airline.setter
    def share_airline(self, value):
        if isinstance(value, ShareAirline):
            self._share_airline = value
        else:
            self._share_airline = ShareAirline.from_alipay_dict(value)
    @property
    def stop_info(self):
        return self._stop_info

    @stop_info.setter
    def stop_info(self, value):
        if isinstance(value, list):
            self._stop_info = list()
            for i in value:
                if isinstance(i, StopInfo):
                    self._stop_info.append(i)
                else:
                    self._stop_info.append(StopInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ac_code:
            if hasattr(self.ac_code, 'to_alipay_dict'):
                params['ac_code'] = self.ac_code.to_alipay_dict()
            else:
                params['ac_code'] = self.ac_code
        if self.ac_name:
            if hasattr(self.ac_name, 'to_alipay_dict'):
                params['ac_name'] = self.ac_name.to_alipay_dict()
            else:
                params['ac_name'] = self.ac_name
        if self.flight_no:
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.is_share:
            if hasattr(self.is_share, 'to_alipay_dict'):
                params['is_share'] = self.is_share.to_alipay_dict()
            else:
                params['is_share'] = self.is_share
        if self.is_stop:
            if hasattr(self.is_stop, 'to_alipay_dict'):
                params['is_stop'] = self.is_stop.to_alipay_dict()
            else:
                params['is_stop'] = self.is_stop
        if self.plane_model:
            if hasattr(self.plane_model, 'to_alipay_dict'):
                params['plane_model'] = self.plane_model.to_alipay_dict()
            else:
                params['plane_model'] = self.plane_model
        if self.plane_model_size:
            if hasattr(self.plane_model_size, 'to_alipay_dict'):
                params['plane_model_size'] = self.plane_model_size.to_alipay_dict()
            else:
                params['plane_model_size'] = self.plane_model_size
        if self.share_airline:
            if hasattr(self.share_airline, 'to_alipay_dict'):
                params['share_airline'] = self.share_airline.to_alipay_dict()
            else:
                params['share_airline'] = self.share_airline
        if self.stop_info:
            if isinstance(self.stop_info, list):
                for i in range(0, len(self.stop_info)):
                    element = self.stop_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stop_info[i] = element.to_alipay_dict()
            if hasattr(self.stop_info, 'to_alipay_dict'):
                params['stop_info'] = self.stop_info.to_alipay_dict()
            else:
                params['stop_info'] = self.stop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Airline()
        if 'ac_code' in d:
            o.ac_code = d['ac_code']
        if 'ac_name' in d:
            o.ac_name = d['ac_name']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'is_share' in d:
            o.is_share = d['is_share']
        if 'is_stop' in d:
            o.is_stop = d['is_stop']
        if 'plane_model' in d:
            o.plane_model = d['plane_model']
        if 'plane_model_size' in d:
            o.plane_model_size = d['plane_model_size']
        if 'share_airline' in d:
            o.share_airline = d['share_airline']
        if 'stop_info' in d:
            o.stop_info = d['stop_info']
        return o


