#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsVenueQueryModel(object):

    def __init__(self):
        self._out_venue_id = None
        self._venue_id = None

    @property
    def out_venue_id(self):
        return self._out_venue_id

    @out_venue_id.setter
    def out_venue_id(self, value):
        self._out_venue_id = value
    @property
    def venue_id(self):
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        self._venue_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_venue_id:
            if hasattr(self.out_venue_id, 'to_alipay_dict'):
                params['out_venue_id'] = self.out_venue_id.to_alipay_dict()
            else:
                params['out_venue_id'] = self.out_venue_id
        if self.venue_id:
            if hasattr(self.venue_id, 'to_alipay_dict'):
                params['venue_id'] = self.venue_id.to_alipay_dict()
            else:
                params['venue_id'] = self.venue_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsVenueQueryModel()
        if 'out_venue_id' in d:
            o.out_venue_id = d['out_venue_id']
        if 'venue_id' in d:
            o.venue_id = d['venue_id']
        return o


