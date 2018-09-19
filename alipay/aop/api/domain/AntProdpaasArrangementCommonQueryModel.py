#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArrangementBaseSelector import ArrangementBaseSelector
from alipay.aop.api.domain.ArrangementConditionGroupSelector import ArrangementConditionGroupSelector
from alipay.aop.api.domain.ArrangementInvolvedPartyQuerier import ArrangementInvolvedPartyQuerier
from alipay.aop.api.domain.ArrangementNoQuerier import ArrangementNoQuerier


class AntProdpaasArrangementCommonQueryModel(object):

    def __init__(self):
        self._arrangement_base_selector = None
        self._arrangement_condition_group_selector = None
        self._arrangement_involved_party_querier = None
        self._arrangement_no_querier = None

    @property
    def arrangement_base_selector(self):
        return self._arrangement_base_selector

    @arrangement_base_selector.setter
    def arrangement_base_selector(self, value):
        if isinstance(value, ArrangementBaseSelector):
            self._arrangement_base_selector = value
        else:
            self._arrangement_base_selector = ArrangementBaseSelector.from_alipay_dict(value)
    @property
    def arrangement_condition_group_selector(self):
        return self._arrangement_condition_group_selector

    @arrangement_condition_group_selector.setter
    def arrangement_condition_group_selector(self, value):
        if isinstance(value, ArrangementConditionGroupSelector):
            self._arrangement_condition_group_selector = value
        else:
            self._arrangement_condition_group_selector = ArrangementConditionGroupSelector.from_alipay_dict(value)
    @property
    def arrangement_involved_party_querier(self):
        return self._arrangement_involved_party_querier

    @arrangement_involved_party_querier.setter
    def arrangement_involved_party_querier(self, value):
        if isinstance(value, ArrangementInvolvedPartyQuerier):
            self._arrangement_involved_party_querier = value
        else:
            self._arrangement_involved_party_querier = ArrangementInvolvedPartyQuerier.from_alipay_dict(value)
    @property
    def arrangement_no_querier(self):
        return self._arrangement_no_querier

    @arrangement_no_querier.setter
    def arrangement_no_querier(self, value):
        if isinstance(value, ArrangementNoQuerier):
            self._arrangement_no_querier = value
        else:
            self._arrangement_no_querier = ArrangementNoQuerier.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.arrangement_base_selector:
            if hasattr(self.arrangement_base_selector, 'to_alipay_dict'):
                params['arrangement_base_selector'] = self.arrangement_base_selector.to_alipay_dict()
            else:
                params['arrangement_base_selector'] = self.arrangement_base_selector
        if self.arrangement_condition_group_selector:
            if hasattr(self.arrangement_condition_group_selector, 'to_alipay_dict'):
                params['arrangement_condition_group_selector'] = self.arrangement_condition_group_selector.to_alipay_dict()
            else:
                params['arrangement_condition_group_selector'] = self.arrangement_condition_group_selector
        if self.arrangement_involved_party_querier:
            if hasattr(self.arrangement_involved_party_querier, 'to_alipay_dict'):
                params['arrangement_involved_party_querier'] = self.arrangement_involved_party_querier.to_alipay_dict()
            else:
                params['arrangement_involved_party_querier'] = self.arrangement_involved_party_querier
        if self.arrangement_no_querier:
            if hasattr(self.arrangement_no_querier, 'to_alipay_dict'):
                params['arrangement_no_querier'] = self.arrangement_no_querier.to_alipay_dict()
            else:
                params['arrangement_no_querier'] = self.arrangement_no_querier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntProdpaasArrangementCommonQueryModel()
        if 'arrangement_base_selector' in d:
            o.arrangement_base_selector = d['arrangement_base_selector']
        if 'arrangement_condition_group_selector' in d:
            o.arrangement_condition_group_selector = d['arrangement_condition_group_selector']
        if 'arrangement_involved_party_querier' in d:
            o.arrangement_involved_party_querier = d['arrangement_involved_party_querier']
        if 'arrangement_no_querier' in d:
            o.arrangement_no_querier = d['arrangement_no_querier']
        return o


