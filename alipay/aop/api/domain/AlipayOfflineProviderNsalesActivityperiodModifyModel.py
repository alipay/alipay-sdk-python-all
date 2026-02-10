#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NSalesSubActivityModify import NSalesSubActivityModify


class AlipayOfflineProviderNsalesActivityperiodModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._out_biz_id = None
        self._period_list = None
        self._reason_code = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def period_list(self):
        return self._period_list

    @period_list.setter
    def period_list(self, value):
        if isinstance(value, list):
            self._period_list = list()
            for i in value:
                if isinstance(i, NSalesSubActivityModify):
                    self._period_list.append(i)
                else:
                    self._period_list.append(NSalesSubActivityModify.from_alipay_dict(i))
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.period_list:
            if isinstance(self.period_list, list):
                for i in range(0, len(self.period_list)):
                    element = self.period_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.period_list[i] = element.to_alipay_dict()
            if hasattr(self.period_list, 'to_alipay_dict'):
                params['period_list'] = self.period_list.to_alipay_dict()
            else:
                params['period_list'] = self.period_list
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNsalesActivityperiodModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'period_list' in d:
            o.period_list = d['period_list']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        return o


