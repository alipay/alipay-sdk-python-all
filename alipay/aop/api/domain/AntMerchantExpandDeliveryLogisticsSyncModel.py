#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsInfo import LogisticsInfo


class AntMerchantExpandDeliveryLogisticsSyncModel(object):

    def __init__(self):
        self._assign_item_id = None
        self._logistics_info = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, LogisticsInfo):
            self._logistics_info = value
        else:
            self._logistics_info = LogisticsInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.logistics_info:
            if hasattr(self.logistics_info, 'to_alipay_dict'):
                params['logistics_info'] = self.logistics_info.to_alipay_dict()
            else:
                params['logistics_info'] = self.logistics_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandDeliveryLogisticsSyncModel()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'logistics_info' in d:
            o.logistics_info = d['logistics_info']
        return o


