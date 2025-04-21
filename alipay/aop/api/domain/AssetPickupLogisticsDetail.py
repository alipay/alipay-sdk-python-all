#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsInfo import LogisticsInfo


class AssetPickupLogisticsDetail(object):

    def __init__(self):
        self._assign_item_id = None
        self._batch_no = None
        self._logistics_infos = None
        self._pickup_status = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def logistics_infos(self):
        return self._logistics_infos

    @logistics_infos.setter
    def logistics_infos(self, value):
        if isinstance(value, LogisticsInfo):
            self._logistics_infos = value
        else:
            self._logistics_infos = LogisticsInfo.from_alipay_dict(value)
    @property
    def pickup_status(self):
        return self._pickup_status

    @pickup_status.setter
    def pickup_status(self, value):
        self._pickup_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.logistics_infos:
            if hasattr(self.logistics_infos, 'to_alipay_dict'):
                params['logistics_infos'] = self.logistics_infos.to_alipay_dict()
            else:
                params['logistics_infos'] = self.logistics_infos
        if self.pickup_status:
            if hasattr(self.pickup_status, 'to_alipay_dict'):
                params['pickup_status'] = self.pickup_status.to_alipay_dict()
            else:
                params['pickup_status'] = self.pickup_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetPickupLogisticsDetail()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'logistics_infos' in d:
            o.logistics_infos = d['logistics_infos']
        if 'pickup_status' in d:
            o.pickup_status = d['pickup_status']
        return o


