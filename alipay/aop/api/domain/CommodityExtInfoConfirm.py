#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommodityExtInfoConfirm(object):

    def __init__(self):
        self._city_status = None
        self._displayapp_id = None
        self._mapping_displayapp_id = None
        self._memo = None

    @property
    def city_status(self):
        return self._city_status

    @city_status.setter
    def city_status(self, value):
        self._city_status = value
    @property
    def displayapp_id(self):
        return self._displayapp_id

    @displayapp_id.setter
    def displayapp_id(self, value):
        self._displayapp_id = value
    @property
    def mapping_displayapp_id(self):
        return self._mapping_displayapp_id

    @mapping_displayapp_id.setter
    def mapping_displayapp_id(self, value):
        self._mapping_displayapp_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_status:
            if hasattr(self.city_status, 'to_alipay_dict'):
                params['city_status'] = self.city_status.to_alipay_dict()
            else:
                params['city_status'] = self.city_status
        if self.displayapp_id:
            if hasattr(self.displayapp_id, 'to_alipay_dict'):
                params['displayapp_id'] = self.displayapp_id.to_alipay_dict()
            else:
                params['displayapp_id'] = self.displayapp_id
        if self.mapping_displayapp_id:
            if hasattr(self.mapping_displayapp_id, 'to_alipay_dict'):
                params['mapping_displayapp_id'] = self.mapping_displayapp_id.to_alipay_dict()
            else:
                params['mapping_displayapp_id'] = self.mapping_displayapp_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommodityExtInfoConfirm()
        if 'city_status' in d:
            o.city_status = d['city_status']
        if 'displayapp_id' in d:
            o.displayapp_id = d['displayapp_id']
        if 'mapping_displayapp_id' in d:
            o.mapping_displayapp_id = d['mapping_displayapp_id']
        if 'memo' in d:
            o.memo = d['memo']
        return o


