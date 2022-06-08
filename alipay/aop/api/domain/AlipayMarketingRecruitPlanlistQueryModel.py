#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitEnrollMerchant import RecruitEnrollMerchant


class AlipayMarketingRecruitPlanlistQueryModel(object):

    def __init__(self):
        self._enroll_merchant = None
        self._page_num = None
        self._page_size = None

    @property
    def enroll_merchant(self):
        return self._enroll_merchant

    @enroll_merchant.setter
    def enroll_merchant(self, value):
        if isinstance(value, RecruitEnrollMerchant):
            self._enroll_merchant = value
        else:
            self._enroll_merchant = RecruitEnrollMerchant.from_alipay_dict(value)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.enroll_merchant:
            if hasattr(self.enroll_merchant, 'to_alipay_dict'):
                params['enroll_merchant'] = self.enroll_merchant.to_alipay_dict()
            else:
                params['enroll_merchant'] = self.enroll_merchant
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingRecruitPlanlistQueryModel()
        if 'enroll_merchant' in d:
            o.enroll_merchant = d['enroll_merchant']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


