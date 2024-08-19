#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePetMerchantarchiveQueryModel(object):

    def __init__(self):
        self._archive_id = None
        self._external_pet_id = None

    @property
    def archive_id(self):
        return self._archive_id

    @archive_id.setter
    def archive_id(self, value):
        self._archive_id = value
    @property
    def external_pet_id(self):
        return self._external_pet_id

    @external_pet_id.setter
    def external_pet_id(self, value):
        self._external_pet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.archive_id:
            if hasattr(self.archive_id, 'to_alipay_dict'):
                params['archive_id'] = self.archive_id.to_alipay_dict()
            else:
                params['archive_id'] = self.archive_id
        if self.external_pet_id:
            if hasattr(self.external_pet_id, 'to_alipay_dict'):
                params['external_pet_id'] = self.external_pet_id.to_alipay_dict()
            else:
                params['external_pet_id'] = self.external_pet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePetMerchantarchiveQueryModel()
        if 'archive_id' in d:
            o.archive_id = d['archive_id']
        if 'external_pet_id' in d:
            o.external_pet_id = d['external_pet_id']
        return o


