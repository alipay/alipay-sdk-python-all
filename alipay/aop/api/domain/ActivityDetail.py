#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityDetail(object):

    def __init__(self):
        self._activity_id = None
        self._activity_type = None
        self._voucher_constraint = None
        self._voucher_desc = None
        self._voucher_interest = None
        self._voucher_type = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def voucher_constraint(self):
        return self._voucher_constraint

    @voucher_constraint.setter
    def voucher_constraint(self, value):
        self._voucher_constraint = value
    @property
    def voucher_desc(self):
        return self._voucher_desc

    @voucher_desc.setter
    def voucher_desc(self, value):
        self._voucher_desc = value
    @property
    def voucher_interest(self):
        return self._voucher_interest

    @voucher_interest.setter
    def voucher_interest(self, value):
        self._voucher_interest = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.voucher_constraint:
            if hasattr(self.voucher_constraint, 'to_alipay_dict'):
                params['voucher_constraint'] = self.voucher_constraint.to_alipay_dict()
            else:
                params['voucher_constraint'] = self.voucher_constraint
        if self.voucher_desc:
            if hasattr(self.voucher_desc, 'to_alipay_dict'):
                params['voucher_desc'] = self.voucher_desc.to_alipay_dict()
            else:
                params['voucher_desc'] = self.voucher_desc
        if self.voucher_interest:
            if hasattr(self.voucher_interest, 'to_alipay_dict'):
                params['voucher_interest'] = self.voucher_interest.to_alipay_dict()
            else:
                params['voucher_interest'] = self.voucher_interest
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityDetail()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'voucher_constraint' in d:
            o.voucher_constraint = d['voucher_constraint']
        if 'voucher_desc' in d:
            o.voucher_desc = d['voucher_desc']
        if 'voucher_interest' in d:
            o.voucher_interest = d['voucher_interest']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


