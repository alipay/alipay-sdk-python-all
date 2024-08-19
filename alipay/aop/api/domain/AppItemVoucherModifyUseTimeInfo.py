#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemAbsoluteModifyPeriodInfo import AppItemAbsoluteModifyPeriodInfo
from alipay.aop.api.domain.AppItemRelativeModifyPeriodInfo import AppItemRelativeModifyPeriodInfo


class AppItemVoucherModifyUseTimeInfo(object):

    def __init__(self):
        self._app_item_absolute_period_info = None
        self._app_item_relative_period_info = None

    @property
    def app_item_absolute_period_info(self):
        return self._app_item_absolute_period_info

    @app_item_absolute_period_info.setter
    def app_item_absolute_period_info(self, value):
        if isinstance(value, AppItemAbsoluteModifyPeriodInfo):
            self._app_item_absolute_period_info = value
        else:
            self._app_item_absolute_period_info = AppItemAbsoluteModifyPeriodInfo.from_alipay_dict(value)
    @property
    def app_item_relative_period_info(self):
        return self._app_item_relative_period_info

    @app_item_relative_period_info.setter
    def app_item_relative_period_info(self, value):
        if isinstance(value, AppItemRelativeModifyPeriodInfo):
            self._app_item_relative_period_info = value
        else:
            self._app_item_relative_period_info = AppItemRelativeModifyPeriodInfo.from_alipay_dict(value)


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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherModifyUseTimeInfo()
        if 'app_item_absolute_period_info' in d:
            o.app_item_absolute_period_info = d['app_item_absolute_period_info']
        if 'app_item_relative_period_info' in d:
            o.app_item_relative_period_info = d['app_item_relative_period_info']
        return o


