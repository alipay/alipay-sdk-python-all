#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertCommissionClause import KbAdvertCommissionClause


class KbAdvertMissionSubject(object):

    def __init__(self):
        self._commission_clause_list = None
        self._subject_biz_id = None
        self._subject_type = None

    @property
    def commission_clause_list(self):
        return self._commission_clause_list

    @commission_clause_list.setter
    def commission_clause_list(self, value):
        if isinstance(value, list):
            self._commission_clause_list = list()
            for i in value:
                if isinstance(i, KbAdvertCommissionClause):
                    self._commission_clause_list.append(i)
                else:
                    self._commission_clause_list.append(KbAdvertCommissionClause.from_alipay_dict(i))
    @property
    def subject_biz_id(self):
        return self._subject_biz_id

    @subject_biz_id.setter
    def subject_biz_id(self, value):
        self._subject_biz_id = value
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_clause_list:
            if isinstance(self.commission_clause_list, list):
                for i in range(0, len(self.commission_clause_list)):
                    element = self.commission_clause_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commission_clause_list[i] = element.to_alipay_dict()
            if hasattr(self.commission_clause_list, 'to_alipay_dict'):
                params['commission_clause_list'] = self.commission_clause_list.to_alipay_dict()
            else:
                params['commission_clause_list'] = self.commission_clause_list
        if self.subject_biz_id:
            if hasattr(self.subject_biz_id, 'to_alipay_dict'):
                params['subject_biz_id'] = self.subject_biz_id.to_alipay_dict()
            else:
                params['subject_biz_id'] = self.subject_biz_id
        if self.subject_type:
            if hasattr(self.subject_type, 'to_alipay_dict'):
                params['subject_type'] = self.subject_type.to_alipay_dict()
            else:
                params['subject_type'] = self.subject_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertMissionSubject()
        if 'commission_clause_list' in d:
            o.commission_clause_list = d['commission_clause_list']
        if 'subject_biz_id' in d:
            o.subject_biz_id = d['subject_biz_id']
        if 'subject_type' in d:
            o.subject_type = d['subject_type']
        return o


