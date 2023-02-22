#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovalCityDTO import ApprovalCityDTO
from alipay.aop.api.domain.ApprovalCityDTO import ApprovalCityDTO


class ApprovalTripDTO(object):

    def __init__(self):
        self._apply_finish_time = None
        self._apply_start_time = None
        self._destination = None
        self._institution_id = None
        self._origin = None
        self._trip_mode = None
        self._trip_way = None

    @property
    def apply_finish_time(self):
        return self._apply_finish_time

    @apply_finish_time.setter
    def apply_finish_time(self, value):
        self._apply_finish_time = value
    @property
    def apply_start_time(self):
        return self._apply_start_time

    @apply_start_time.setter
    def apply_start_time(self, value):
        self._apply_start_time = value
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if isinstance(value, ApprovalCityDTO):
            self._destination = value
        else:
            self._destination = ApprovalCityDTO.from_alipay_dict(value)
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        if isinstance(value, ApprovalCityDTO):
            self._origin = value
        else:
            self._origin = ApprovalCityDTO.from_alipay_dict(value)
    @property
    def trip_mode(self):
        return self._trip_mode

    @trip_mode.setter
    def trip_mode(self, value):
        self._trip_mode = value
    @property
    def trip_way(self):
        return self._trip_way

    @trip_way.setter
    def trip_way(self, value):
        self._trip_way = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_finish_time:
            if hasattr(self.apply_finish_time, 'to_alipay_dict'):
                params['apply_finish_time'] = self.apply_finish_time.to_alipay_dict()
            else:
                params['apply_finish_time'] = self.apply_finish_time
        if self.apply_start_time:
            if hasattr(self.apply_start_time, 'to_alipay_dict'):
                params['apply_start_time'] = self.apply_start_time.to_alipay_dict()
            else:
                params['apply_start_time'] = self.apply_start_time
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.origin:
            if hasattr(self.origin, 'to_alipay_dict'):
                params['origin'] = self.origin.to_alipay_dict()
            else:
                params['origin'] = self.origin
        if self.trip_mode:
            if hasattr(self.trip_mode, 'to_alipay_dict'):
                params['trip_mode'] = self.trip_mode.to_alipay_dict()
            else:
                params['trip_mode'] = self.trip_mode
        if self.trip_way:
            if hasattr(self.trip_way, 'to_alipay_dict'):
                params['trip_way'] = self.trip_way.to_alipay_dict()
            else:
                params['trip_way'] = self.trip_way
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApprovalTripDTO()
        if 'apply_finish_time' in d:
            o.apply_finish_time = d['apply_finish_time']
        if 'apply_start_time' in d:
            o.apply_start_time = d['apply_start_time']
        if 'destination' in d:
            o.destination = d['destination']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'origin' in d:
            o.origin = d['origin']
        if 'trip_mode' in d:
            o.trip_mode = d['trip_mode']
        if 'trip_way' in d:
            o.trip_way = d['trip_way']
        return o


