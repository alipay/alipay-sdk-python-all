#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAbsolutePeriodInfo import VoucherAbsolutePeriodInfo
from alipay.aop.api.domain.VoucherRelativePeriodInfo import VoucherRelativePeriodInfo


class VoucherUseTimeInfo(object):

    def __init__(self):
        self._absolute_period_info = None
        self._period_type = None
        self._relative_period_info = None

    @property
    def absolute_period_info(self):
        return self._absolute_period_info

    @absolute_period_info.setter
    def absolute_period_info(self, value):
        if isinstance(value, VoucherAbsolutePeriodInfo):
            self._absolute_period_info = value
        else:
            self._absolute_period_info = VoucherAbsolutePeriodInfo.from_alipay_dict(value)
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def relative_period_info(self):
        return self._relative_period_info

    @relative_period_info.setter
    def relative_period_info(self, value):
        if isinstance(value, VoucherRelativePeriodInfo):
            self._relative_period_info = value
        else:
            self._relative_period_info = VoucherRelativePeriodInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.absolute_period_info:
            if hasattr(self.absolute_period_info, 'to_alipay_dict'):
                params['absolute_period_info'] = self.absolute_period_info.to_alipay_dict()
            else:
                params['absolute_period_info'] = self.absolute_period_info
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.relative_period_info:
            if hasattr(self.relative_period_info, 'to_alipay_dict'):
                params['relative_period_info'] = self.relative_period_info.to_alipay_dict()
            else:
                params['relative_period_info'] = self.relative_period_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseTimeInfo()
        if 'absolute_period_info' in d:
            o.absolute_period_info = d['absolute_period_info']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'relative_period_info' in d:
            o.relative_period_info = d['relative_period_info']
        return o


