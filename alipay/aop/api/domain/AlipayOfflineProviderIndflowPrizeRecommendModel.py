#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderIndflowPrizeRecommendModel(object):

    def __init__(self):
        self._instance_ids = None
        self._mobile_phone = None
        self._out_pos_id = None

    @property
    def instance_ids(self):
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, value):
        if isinstance(value, list):
            self._instance_ids = list()
            for i in value:
                self._instance_ids.append(i)
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def out_pos_id(self):
        return self._out_pos_id

    @out_pos_id.setter
    def out_pos_id(self, value):
        self._out_pos_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.instance_ids:
            if isinstance(self.instance_ids, list):
                for i in range(0, len(self.instance_ids)):
                    element = self.instance_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.instance_ids[i] = element.to_alipay_dict()
            if hasattr(self.instance_ids, 'to_alipay_dict'):
                params['instance_ids'] = self.instance_ids.to_alipay_dict()
            else:
                params['instance_ids'] = self.instance_ids
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.out_pos_id:
            if hasattr(self.out_pos_id, 'to_alipay_dict'):
                params['out_pos_id'] = self.out_pos_id.to_alipay_dict()
            else:
                params['out_pos_id'] = self.out_pos_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderIndflowPrizeRecommendModel()
        if 'instance_ids' in d:
            o.instance_ids = d['instance_ids']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'out_pos_id' in d:
            o.out_pos_id = d['out_pos_id']
        return o


