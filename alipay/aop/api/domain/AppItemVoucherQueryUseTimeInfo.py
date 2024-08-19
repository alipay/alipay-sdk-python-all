#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemAbsoluteQueryPeriodInfo import AppItemAbsoluteQueryPeriodInfo
from alipay.aop.api.domain.AppItemRelativeQueryPeriodInfo import AppItemRelativeQueryPeriodInfo


class AppItemVoucherQueryUseTimeInfo(object):

    def __init__(self):
        self._app_item_absolute_period_info = None
        self._app_item_relative_period_info = None
        self._period_type = None

    @property
    def app_item_absolute_period_info(self):
        return self._app_item_absolute_period_info

    @app_item_absolute_period_info.setter
    def app_item_absolute_period_info(self, value):
        if isinstance(value, AppItemAbsoluteQueryPeriodInfo):
            self._app_item_absolute_period_info = value
        else:
            self._app_item_absolute_period_info = AppItemAbsoluteQueryPeriodInfo.from_alipay_dict(value)
    @property
    def app_item_relative_period_info(self):
        return self._app_item_relative_period_info

    @app_item_relative_period_info.setter
    def app_item_relative_period_info(self, value):
        if isinstance(value, AppItemRelativeQueryPeriodInfo):
            self._app_item_relative_period_info = value
        else:
            self._app_item_relative_period_info = AppItemRelativeQueryPeriodInfo.from_alipay_dict(value)
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_absolute_period_info:
            if hasattr(self.app_item_absolute_period_info, 'to_alipay_dict'):
                params['app_item_absolute_period_info'] = self.app_item_absolute_period_info.to_alipay_dict()
            else:
                params['app_item_absolute_period_info'] = self.app_item_absolute_period_info
        if self.app_item_relative_period_info:
            if hasattr(self.app_item_relative_period_info, 'to_alipay_dict'):
                params['app_item_relative_period_info'] = self.app_item_relative_period_info.to_alipay_dict()
            else:
                params['app_item_relative_period_info'] = self.app_item_relative_period_info
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherQueryUseTimeInfo()
        if 'app_item_absolute_period_info' in d:
            o.app_item_absolute_period_info = d['app_item_absolute_period_info']
        if 'app_item_relative_period_info' in d:
            o.app_item_relative_period_info = d['app_item_relative_period_info']
        if 'period_type' in d:
            o.period_type = d['period_type']
        return o


