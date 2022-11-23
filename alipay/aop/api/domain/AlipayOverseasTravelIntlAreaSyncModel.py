#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AreaDTO import AreaDTO


class AlipayOverseasTravelIntlAreaSyncModel(object):

    def __init__(self):
        self._area_info = None
        self._request_id = None

    @property
    def area_info(self):
        return self._area_info

    @area_info.setter
    def area_info(self, value):
        if isinstance(value, AreaDTO):
            self._area_info = value
        else:
            self._area_info = AreaDTO.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_info:
            if hasattr(self.area_info, 'to_alipay_dict'):
                params['area_info'] = self.area_info.to_alipay_dict()
            else:
                params['area_info'] = self.area_info
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelIntlAreaSyncModel()
        if 'area_info' in d:
            o.area_info = d['area_info']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


