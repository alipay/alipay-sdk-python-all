#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizAreaDTO import BizAreaDTO


class AlipayOverseasTravelIntlBizareaSyncModel(object):

    def __init__(self):
        self._biz_area_info = None
        self._request_id = None

    @property
    def biz_area_info(self):
        return self._biz_area_info

    @biz_area_info.setter
    def biz_area_info(self, value):
        if isinstance(value, BizAreaDTO):
            self._biz_area_info = value
        else:
            self._biz_area_info = BizAreaDTO.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_area_info:
            if hasattr(self.biz_area_info, 'to_alipay_dict'):
                params['biz_area_info'] = self.biz_area_info.to_alipay_dict()
            else:
                params['biz_area_info'] = self.biz_area_info
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
        o = AlipayOverseasTravelIntlBizareaSyncModel()
        if 'biz_area_info' in d:
            o.biz_area_info = d['biz_area_info']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


