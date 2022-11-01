#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeGenericItem(object):

    def __init__(self):
        self._attribute = None
        self._id = None
        self._row_type = None
        self._status = None

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, value):
        self._row_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute:
            if hasattr(self.attribute, 'to_alipay_dict'):
                params['attribute'] = self.attribute.to_alipay_dict()
            else:
                params['attribute'] = self.attribute
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.row_type:
            if hasattr(self.row_type, 'to_alipay_dict'):
                params['row_type'] = self.row_type.to_alipay_dict()
            else:
                params['row_type'] = self.row_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApeGenericItem()
        if 'attribute' in d:
            o.attribute = d['attribute']
        if 'id' in d:
            o.id = d['id']
        if 'row_type' in d:
            o.row_type = d['row_type']
        if 'status' in d:
            o.status = d['status']
        return o


