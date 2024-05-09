#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubRentRiskResult import SubRentRiskResult


class RentRiskResult(object):

    def __init__(self):
        self._record_id = None
        self._risk_desc = None
        self._risk_name = None
        self._risk_rank = None
        self._sub_rent_risk_result = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
    @property
    def risk_name(self):
        return self._risk_name

    @risk_name.setter
    def risk_name(self, value):
        self._risk_name = value
    @property
    def risk_rank(self):
        return self._risk_rank

    @risk_rank.setter
    def risk_rank(self, value):
        self._risk_rank = value
    @property
    def sub_rent_risk_result(self):
        return self._sub_rent_risk_result

    @sub_rent_risk_result.setter
    def sub_rent_risk_result(self, value):
        if isinstance(value, SubRentRiskResult):
            self._sub_rent_risk_result = value
        else:
            self._sub_rent_risk_result = SubRentRiskResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.risk_desc:
            if hasattr(self.risk_desc, 'to_alipay_dict'):
                params['risk_desc'] = self.risk_desc.to_alipay_dict()
            else:
                params['risk_desc'] = self.risk_desc
        if self.risk_name:
            if hasattr(self.risk_name, 'to_alipay_dict'):
                params['risk_name'] = self.risk_name.to_alipay_dict()
            else:
                params['risk_name'] = self.risk_name
        if self.risk_rank:
            if hasattr(self.risk_rank, 'to_alipay_dict'):
                params['risk_rank'] = self.risk_rank.to_alipay_dict()
            else:
                params['risk_rank'] = self.risk_rank
        if self.sub_rent_risk_result:
            if hasattr(self.sub_rent_risk_result, 'to_alipay_dict'):
                params['sub_rent_risk_result'] = self.sub_rent_risk_result.to_alipay_dict()
            else:
                params['sub_rent_risk_result'] = self.sub_rent_risk_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRiskResult()
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'risk_desc' in d:
            o.risk_desc = d['risk_desc']
        if 'risk_name' in d:
            o.risk_name = d['risk_name']
        if 'risk_rank' in d:
            o.risk_rank = d['risk_rank']
        if 'sub_rent_risk_result' in d:
            o.sub_rent_risk_result = d['sub_rent_risk_result']
        return o


