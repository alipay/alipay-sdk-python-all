#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CraftsmanWorkCreateOpenModel import CraftsmanWorkCreateOpenModel


class KoubeiCraftsmanDataWorkCreateModel(object):

    def __init__(self):
        self._auth_code = None
        self._craftsman_id = None
        self._shop_ids = None
        self._works = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def craftsman_id(self):
        return self._craftsman_id

    @craftsman_id.setter
    def craftsman_id(self, value):
        self._craftsman_id = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)
    @property
    def works(self):
        return self._works

    @works.setter
    def works(self, value):
        if isinstance(value, list):
            self._works = list()
            for i in value:
                if isinstance(i, CraftsmanWorkCreateOpenModel):
                    self._works.append(i)
                else:
                    self._works.append(CraftsmanWorkCreateOpenModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.craftsman_id:
            if hasattr(self.craftsman_id, 'to_alipay_dict'):
                params['craftsman_id'] = self.craftsman_id.to_alipay_dict()
            else:
                params['craftsman_id'] = self.craftsman_id
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        if self.works:
            if isinstance(self.works, list):
                for i in range(0, len(self.works)):
                    element = self.works[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.works[i] = element.to_alipay_dict()
            if hasattr(self.works, 'to_alipay_dict'):
                params['works'] = self.works.to_alipay_dict()
            else:
                params['works'] = self.works
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCraftsmanDataWorkCreateModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'craftsman_id' in d:
            o.craftsman_id = d['craftsman_id']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'works' in d:
            o.works = d['works']
        return o


