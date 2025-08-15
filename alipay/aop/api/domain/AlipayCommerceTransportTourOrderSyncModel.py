#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TourOrderSyncDetail import TourOrderSyncDetail


class AlipayCommerceTransportTourOrderSyncModel(object):

    def __init__(self):
        self._scene_codes = None
        self._tour_order_list = None

    @property
    def scene_codes(self):
        return self._scene_codes

    @scene_codes.setter
    def scene_codes(self, value):
        if isinstance(value, list):
            self._scene_codes = list()
            for i in value:
                self._scene_codes.append(i)
    @property
    def tour_order_list(self):
        return self._tour_order_list

    @tour_order_list.setter
    def tour_order_list(self, value):
        if isinstance(value, list):
            self._tour_order_list = list()
            for i in value:
                if isinstance(i, TourOrderSyncDetail):
                    self._tour_order_list.append(i)
                else:
                    self._tour_order_list.append(TourOrderSyncDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.scene_codes:
            if isinstance(self.scene_codes, list):
                for i in range(0, len(self.scene_codes)):
                    element = self.scene_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_codes[i] = element.to_alipay_dict()
            if hasattr(self.scene_codes, 'to_alipay_dict'):
                params['scene_codes'] = self.scene_codes.to_alipay_dict()
            else:
                params['scene_codes'] = self.scene_codes
        if self.tour_order_list:
            if isinstance(self.tour_order_list, list):
                for i in range(0, len(self.tour_order_list)):
                    element = self.tour_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tour_order_list[i] = element.to_alipay_dict()
            if hasattr(self.tour_order_list, 'to_alipay_dict'):
                params['tour_order_list'] = self.tour_order_list.to_alipay_dict()
            else:
                params['tour_order_list'] = self.tour_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTourOrderSyncModel()
        if 'scene_codes' in d:
            o.scene_codes = d['scene_codes']
        if 'tour_order_list' in d:
            o.tour_order_list = d['tour_order_list']
        return o


