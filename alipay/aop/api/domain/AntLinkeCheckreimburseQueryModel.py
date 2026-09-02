#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionMonthPair import SubscriptionMonthPair


class AntLinkeCheckreimburseQueryModel(object):

    def __init__(self):
        self._subscription_month_pair_list = None
        self._work_no = None

    @property
    def subscription_month_pair_list(self):
        return self._subscription_month_pair_list

    @subscription_month_pair_list.setter
    def subscription_month_pair_list(self, value):
        if isinstance(value, list):
            self._subscription_month_pair_list = list()
            for i in value:
                if isinstance(i, SubscriptionMonthPair):
                    self._subscription_month_pair_list.append(i)
                else:
                    self._subscription_month_pair_list.append(SubscriptionMonthPair.from_alipay_dict(i))
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.subscription_month_pair_list:
            if isinstance(self.subscription_month_pair_list, list):
                for i in range(0, len(self.subscription_month_pair_list)):
                    element = self.subscription_month_pair_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subscription_month_pair_list[i] = element.to_alipay_dict()
            if hasattr(self.subscription_month_pair_list, 'to_alipay_dict'):
                params['subscription_month_pair_list'] = self.subscription_month_pair_list.to_alipay_dict()
            else:
                params['subscription_month_pair_list'] = self.subscription_month_pair_list
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntLinkeCheckreimburseQueryModel()
        if 'subscription_month_pair_list' in d:
            o.subscription_month_pair_list = d['subscription_month_pair_list']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


