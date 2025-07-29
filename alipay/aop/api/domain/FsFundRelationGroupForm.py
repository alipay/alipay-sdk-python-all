#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FsFundRelationDetailForm import FsFundRelationDetailForm


class FsFundRelationGroupForm(object):

    def __init__(self):
        self._fund_relation_details = None
        self._fund_strategy = None
        self._group_id = None

    @property
    def fund_relation_details(self):
        return self._fund_relation_details

    @fund_relation_details.setter
    def fund_relation_details(self, value):
        if isinstance(value, list):
            self._fund_relation_details = list()
            for i in value:
                if isinstance(i, FsFundRelationDetailForm):
                    self._fund_relation_details.append(i)
                else:
                    self._fund_relation_details.append(FsFundRelationDetailForm.from_alipay_dict(i))
    @property
    def fund_strategy(self):
        return self._fund_strategy

    @fund_strategy.setter
    def fund_strategy(self, value):
        self._fund_strategy = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_relation_details:
            if isinstance(self.fund_relation_details, list):
                for i in range(0, len(self.fund_relation_details)):
                    element = self.fund_relation_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_relation_details[i] = element.to_alipay_dict()
            if hasattr(self.fund_relation_details, 'to_alipay_dict'):
                params['fund_relation_details'] = self.fund_relation_details.to_alipay_dict()
            else:
                params['fund_relation_details'] = self.fund_relation_details
        if self.fund_strategy:
            if hasattr(self.fund_strategy, 'to_alipay_dict'):
                params['fund_strategy'] = self.fund_strategy.to_alipay_dict()
            else:
                params['fund_strategy'] = self.fund_strategy
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FsFundRelationGroupForm()
        if 'fund_relation_details' in d:
            o.fund_relation_details = d['fund_relation_details']
        if 'fund_strategy' in d:
            o.fund_strategy = d['fund_strategy']
        if 'group_id' in d:
            o.group_id = d['group_id']
        return o


