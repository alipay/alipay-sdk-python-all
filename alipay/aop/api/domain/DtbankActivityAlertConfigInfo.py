#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtbankActivityAlertConfigInfo(object):

    def __init__(self):
        self._alert_value = None
        self._app_id_list = None
        self._budget_alert_notify_type = None
        self._phone_no_list = None
        self._write_off_rate_alert_value = None

    @property
    def alert_value(self):
        return self._alert_value

    @alert_value.setter
    def alert_value(self, value):
        self._alert_value = value
    @property
    def app_id_list(self):
        return self._app_id_list

    @app_id_list.setter
    def app_id_list(self, value):
        if isinstance(value, list):
            self._app_id_list = list()
            for i in value:
                self._app_id_list.append(i)
    @property
    def budget_alert_notify_type(self):
        return self._budget_alert_notify_type

    @budget_alert_notify_type.setter
    def budget_alert_notify_type(self, value):
        self._budget_alert_notify_type = value
    @property
    def phone_no_list(self):
        return self._phone_no_list

    @phone_no_list.setter
    def phone_no_list(self, value):
        if isinstance(value, list):
            self._phone_no_list = list()
            for i in value:
                self._phone_no_list.append(i)
    @property
    def write_off_rate_alert_value(self):
        return self._write_off_rate_alert_value

    @write_off_rate_alert_value.setter
    def write_off_rate_alert_value(self, value):
        self._write_off_rate_alert_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.alert_value:
            if hasattr(self.alert_value, 'to_alipay_dict'):
                params['alert_value'] = self.alert_value.to_alipay_dict()
            else:
                params['alert_value'] = self.alert_value
        if self.app_id_list:
            if isinstance(self.app_id_list, list):
                for i in range(0, len(self.app_id_list)):
                    element = self.app_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_id_list[i] = element.to_alipay_dict()
            if hasattr(self.app_id_list, 'to_alipay_dict'):
                params['app_id_list'] = self.app_id_list.to_alipay_dict()
            else:
                params['app_id_list'] = self.app_id_list
        if self.budget_alert_notify_type:
            if hasattr(self.budget_alert_notify_type, 'to_alipay_dict'):
                params['budget_alert_notify_type'] = self.budget_alert_notify_type.to_alipay_dict()
            else:
                params['budget_alert_notify_type'] = self.budget_alert_notify_type
        if self.phone_no_list:
            if isinstance(self.phone_no_list, list):
                for i in range(0, len(self.phone_no_list)):
                    element = self.phone_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone_no_list[i] = element.to_alipay_dict()
            if hasattr(self.phone_no_list, 'to_alipay_dict'):
                params['phone_no_list'] = self.phone_no_list.to_alipay_dict()
            else:
                params['phone_no_list'] = self.phone_no_list
        if self.write_off_rate_alert_value:
            if hasattr(self.write_off_rate_alert_value, 'to_alipay_dict'):
                params['write_off_rate_alert_value'] = self.write_off_rate_alert_value.to_alipay_dict()
            else:
                params['write_off_rate_alert_value'] = self.write_off_rate_alert_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtbankActivityAlertConfigInfo()
        if 'alert_value' in d:
            o.alert_value = d['alert_value']
        if 'app_id_list' in d:
            o.app_id_list = d['app_id_list']
        if 'budget_alert_notify_type' in d:
            o.budget_alert_notify_type = d['budget_alert_notify_type']
        if 'phone_no_list' in d:
            o.phone_no_list = d['phone_no_list']
        if 'write_off_rate_alert_value' in d:
            o.write_off_rate_alert_value = d['write_off_rate_alert_value']
        return o


