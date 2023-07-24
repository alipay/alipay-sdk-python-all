#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertCommissionClause import KbAdvertCommissionClause


class KbAdvertCascadeCommissionInfo(object):

    def __init__(self):
        self._commission_clause_infos = None
        self._commission_user_type = None

    @property
    def commission_clause_infos(self):
        return self._commission_clause_infos

    @commission_clause_infos.setter
    def commission_clause_infos(self, value):
        if isinstance(value, list):
            self._commission_clause_infos = list()
            for i in value:
                if isinstance(i, KbAdvertCommissionClause):
                    self._commission_clause_infos.append(i)
                else:
                    self._commission_clause_infos.append(KbAdvertCommissionClause.from_alipay_dict(i))
    @property
    def commission_user_type(self):
        return self._commission_user_type

    @commission_user_type.setter
    def commission_user_type(self, value):
        self._commission_user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_clause_infos:
            if isinstance(self.commission_clause_infos, list):
                for i in range(0, len(self.commission_clause_infos)):
                    element = self.commission_clause_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commission_clause_infos[i] = element.to_alipay_dict()
            if hasattr(self.commission_clause_infos, 'to_alipay_dict'):
                params['commission_clause_infos'] = self.commission_clause_infos.to_alipay_dict()
            else:
                params['commission_clause_infos'] = self.commission_clause_infos
        if self.commission_user_type:
            if hasattr(self.commission_user_type, 'to_alipay_dict'):
                params['commission_user_type'] = self.commission_user_type.to_alipay_dict()
            else:
                params['commission_user_type'] = self.commission_user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertCascadeCommissionInfo()
        if 'commission_clause_infos' in d:
            o.commission_clause_infos = d['commission_clause_infos']
        if 'commission_user_type' in d:
            o.commission_user_type = d['commission_user_type']
        return o


