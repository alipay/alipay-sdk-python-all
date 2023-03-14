#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaSystemCrossPageRequest import CaSystemCrossPageRequest
from alipay.aop.api.domain.CaSystemMainBodyRequest import CaSystemMainBodyRequest


class CaSystemSignAreaRequest(object):

    def __init__(self):
        self._ca_system_cross_page_request = None
        self._ca_system_main_body_request = None
        self._location_type = None
        self._position_type = None
        self._seal_id = None

    @property
    def ca_system_cross_page_request(self):
        return self._ca_system_cross_page_request

    @ca_system_cross_page_request.setter
    def ca_system_cross_page_request(self, value):
        if isinstance(value, CaSystemCrossPageRequest):
            self._ca_system_cross_page_request = value
        else:
            self._ca_system_cross_page_request = CaSystemCrossPageRequest.from_alipay_dict(value)
    @property
    def ca_system_main_body_request(self):
        return self._ca_system_main_body_request

    @ca_system_main_body_request.setter
    def ca_system_main_body_request(self, value):
        if isinstance(value, CaSystemMainBodyRequest):
            self._ca_system_main_body_request = value
        else:
            self._ca_system_main_body_request = CaSystemMainBodyRequest.from_alipay_dict(value)
    @property
    def location_type(self):
        return self._location_type

    @location_type.setter
    def location_type(self, value):
        self._location_type = value
    @property
    def position_type(self):
        return self._position_type

    @position_type.setter
    def position_type(self, value):
        self._position_type = value
    @property
    def seal_id(self):
        return self._seal_id

    @seal_id.setter
    def seal_id(self, value):
        self._seal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ca_system_cross_page_request:
            if hasattr(self.ca_system_cross_page_request, 'to_alipay_dict'):
                params['ca_system_cross_page_request'] = self.ca_system_cross_page_request.to_alipay_dict()
            else:
                params['ca_system_cross_page_request'] = self.ca_system_cross_page_request
        if self.ca_system_main_body_request:
            if hasattr(self.ca_system_main_body_request, 'to_alipay_dict'):
                params['ca_system_main_body_request'] = self.ca_system_main_body_request.to_alipay_dict()
            else:
                params['ca_system_main_body_request'] = self.ca_system_main_body_request
        if self.location_type:
            if hasattr(self.location_type, 'to_alipay_dict'):
                params['location_type'] = self.location_type.to_alipay_dict()
            else:
                params['location_type'] = self.location_type
        if self.position_type:
            if hasattr(self.position_type, 'to_alipay_dict'):
                params['position_type'] = self.position_type.to_alipay_dict()
            else:
                params['position_type'] = self.position_type
        if self.seal_id:
            if hasattr(self.seal_id, 'to_alipay_dict'):
                params['seal_id'] = self.seal_id.to_alipay_dict()
            else:
                params['seal_id'] = self.seal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaSystemSignAreaRequest()
        if 'ca_system_cross_page_request' in d:
            o.ca_system_cross_page_request = d['ca_system_cross_page_request']
        if 'ca_system_main_body_request' in d:
            o.ca_system_main_body_request = d['ca_system_main_body_request']
        if 'location_type' in d:
            o.location_type = d['location_type']
        if 'position_type' in d:
            o.position_type = d['position_type']
        if 'seal_id' in d:
            o.seal_id = d['seal_id']
        return o


