#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubVenueAuditStatus(object):

    def __init__(self):
        self._out_sub_venue_id = None
        self._sub_venue_id = None
        self._sub_venue_status = None

    @property
    def out_sub_venue_id(self):
        return self._out_sub_venue_id

    @out_sub_venue_id.setter
    def out_sub_venue_id(self, value):
        self._out_sub_venue_id = value
    @property
    def sub_venue_id(self):
        return self._sub_venue_id

    @sub_venue_id.setter
    def sub_venue_id(self, value):
        self._sub_venue_id = value
    @property
    def sub_venue_status(self):
        return self._sub_venue_status

    @sub_venue_status.setter
    def sub_venue_status(self, value):
        self._sub_venue_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_sub_venue_id:
            if hasattr(self.out_sub_venue_id, 'to_alipay_dict'):
                params['out_sub_venue_id'] = self.out_sub_venue_id.to_alipay_dict()
            else:
                params['out_sub_venue_id'] = self.out_sub_venue_id
        if self.sub_venue_id:
            if hasattr(self.sub_venue_id, 'to_alipay_dict'):
                params['sub_venue_id'] = self.sub_venue_id.to_alipay_dict()
            else:
                params['sub_venue_id'] = self.sub_venue_id
        if self.sub_venue_status:
            if hasattr(self.sub_venue_status, 'to_alipay_dict'):
                params['sub_venue_status'] = self.sub_venue_status.to_alipay_dict()
            else:
                params['sub_venue_status'] = self.sub_venue_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubVenueAuditStatus()
        if 'out_sub_venue_id' in d:
            o.out_sub_venue_id = d['out_sub_venue_id']
        if 'sub_venue_id' in d:
            o.sub_venue_id = d['sub_venue_id']
        if 'sub_venue_status' in d:
            o.sub_venue_status = d['sub_venue_status']
        return o


