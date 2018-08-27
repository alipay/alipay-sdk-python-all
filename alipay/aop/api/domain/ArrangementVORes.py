#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArrangementBaseVO import ArrangementBaseVO


class ArrangementVORes(object):

    def __init__(self):
        self._ar_base = None
        self._ar_bsn_status = None
        self._ar_condition = None
        self._arrangement_no = None

    @property
    def ar_base(self):
        return self._ar_base

    @ar_base.setter
    def ar_base(self, value):
        if isinstance(value, ArrangementBaseVO):
            self._ar_base = value
        else:
            self._ar_base = ArrangementBaseVO.from_alipay_dict(value)
    @property
    def ar_bsn_status(self):
        return self._ar_bsn_status

    @ar_bsn_status.setter
    def ar_bsn_status(self, value):
        self._ar_bsn_status = value
    @property
    def ar_condition(self):
        return self._ar_condition

    @ar_condition.setter
    def ar_condition(self, value):
        self._ar_condition = value
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_base:
            if hasattr(self.ar_base, 'to_alipay_dict'):
                params['ar_base'] = self.ar_base.to_alipay_dict()
            else:
                params['ar_base'] = self.ar_base
        if self.ar_bsn_status:
            if hasattr(self.ar_bsn_status, 'to_alipay_dict'):
                params['ar_bsn_status'] = self.ar_bsn_status.to_alipay_dict()
            else:
                params['ar_bsn_status'] = self.ar_bsn_status
        if self.ar_condition:
            if hasattr(self.ar_condition, 'to_alipay_dict'):
                params['ar_condition'] = self.ar_condition.to_alipay_dict()
            else:
                params['ar_condition'] = self.ar_condition
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArrangementVORes()
        if 'ar_base' in d:
            o.ar_base = d['ar_base']
        if 'ar_bsn_status' in d:
            o.ar_bsn_status = d['ar_bsn_status']
        if 'ar_condition' in d:
            o.ar_condition = d['ar_condition']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        return o


