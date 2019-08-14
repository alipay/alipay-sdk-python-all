#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetDeliveryProcessInfo(object):

    def __init__(self):
        self._assign_item_id = None
        self._batch_no = None
        self._count = None
        self._delivery_process_no = None
        self._item_id = None

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
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def delivery_process_no(self):
        return self._delivery_process_no

    @delivery_process_no.setter
    def delivery_process_no(self, value):
        self._delivery_process_no = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


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
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.delivery_process_no:
            if hasattr(self.delivery_process_no, 'to_alipay_dict'):
                params['delivery_process_no'] = self.delivery_process_no.to_alipay_dict()
            else:
                params['delivery_process_no'] = self.delivery_process_no
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetDeliveryProcessInfo()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'count' in d:
            o.count = d['count']
        if 'delivery_process_no' in d:
            o.delivery_process_no = d['delivery_process_no']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


