#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalSupplierContentDeleteModel(object):

    def __init__(self):
        self._med_content_id = None
        self._owner_id = None
        self._owner_type = None

    @property
    def med_content_id(self):
        return self._med_content_id

    @med_content_id.setter
    def med_content_id(self, value):
        self._med_content_id = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.med_content_id:
            if hasattr(self.med_content_id, 'to_alipay_dict'):
                params['med_content_id'] = self.med_content_id.to_alipay_dict()
            else:
                params['med_content_id'] = self.med_content_id
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalSupplierContentDeleteModel()
        if 'med_content_id' in d:
            o.med_content_id = d['med_content_id']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        return o


