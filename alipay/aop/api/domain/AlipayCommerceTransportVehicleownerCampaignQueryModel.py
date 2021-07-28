#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportVehicleownerCampaignQueryModel(object):

    def __init__(self):
        self._activity_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        if isinstance(value, list):
            self._activity_id = list()
            for i in value:
                self._activity_id.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if isinstance(self.activity_id, list):
                for i in range(0, len(self.activity_id)):
                    element = self.activity_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_id[i] = element.to_alipay_dict()
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehicleownerCampaignQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        return o


