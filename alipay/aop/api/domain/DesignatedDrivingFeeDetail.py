#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DesignatedDrivingFeeDetail(object):

    def __init__(self):
        self._fee_amount = None
        self._fee_desc = None
        self._fee_id = None
        self._fee_title = None

    @property
    def fee_amount(self):
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        self._fee_amount = value
    @property
    def fee_desc(self):
        return self._fee_desc

    @fee_desc.setter
    def fee_desc(self, value):
        self._fee_desc = value
    @property
    def fee_id(self):
        return self._fee_id

    @fee_id.setter
    def fee_id(self, value):
        self._fee_id = value
    @property
    def fee_title(self):
        return self._fee_title

    @fee_title.setter
    def fee_title(self, value):
        self._fee_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_amount:
            if hasattr(self.fee_amount, 'to_alipay_dict'):
                params['fee_amount'] = self.fee_amount.to_alipay_dict()
            else:
                params['fee_amount'] = self.fee_amount
        if self.fee_desc:
            if hasattr(self.fee_desc, 'to_alipay_dict'):
                params['fee_desc'] = self.fee_desc.to_alipay_dict()
            else:
                params['fee_desc'] = self.fee_desc
        if self.fee_id:
            if hasattr(self.fee_id, 'to_alipay_dict'):
                params['fee_id'] = self.fee_id.to_alipay_dict()
            else:
                params['fee_id'] = self.fee_id
        if self.fee_title:
            if hasattr(self.fee_title, 'to_alipay_dict'):
                params['fee_title'] = self.fee_title.to_alipay_dict()
            else:
                params['fee_title'] = self.fee_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DesignatedDrivingFeeDetail()
        if 'fee_amount' in d:
            o.fee_amount = d['fee_amount']
        if 'fee_desc' in d:
            o.fee_desc = d['fee_desc']
        if 'fee_id' in d:
            o.fee_id = d['fee_id']
        if 'fee_title' in d:
            o.fee_title = d['fee_title']
        return o


