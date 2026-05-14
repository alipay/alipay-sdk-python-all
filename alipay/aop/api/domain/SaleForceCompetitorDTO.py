#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleForceCompetitorDTO(object):

    def __init__(self):
        self._competitor = None
        self._db_type = None

    @property
    def competitor(self):
        return self._competitor

    @competitor.setter
    def competitor(self, value):
        if isinstance(value, list):
            self._competitor = list()
            for i in value:
                self._competitor.append(i)
    @property
    def db_type(self):
        return self._db_type

    @db_type.setter
    def db_type(self, value):
        self._db_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.competitor:
            if isinstance(self.competitor, list):
                for i in range(0, len(self.competitor)):
                    element = self.competitor[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.competitor[i] = element.to_alipay_dict()
            if hasattr(self.competitor, 'to_alipay_dict'):
                params['competitor'] = self.competitor.to_alipay_dict()
            else:
                params['competitor'] = self.competitor
        if self.db_type:
            if hasattr(self.db_type, 'to_alipay_dict'):
                params['db_type'] = self.db_type.to_alipay_dict()
            else:
                params['db_type'] = self.db_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleForceCompetitorDTO()
        if 'competitor' in d:
            o.competitor = d['competitor']
        if 'db_type' in d:
            o.db_type = d['db_type']
        return o


