#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenSimplestIssueCustomParamDTO(object):

    def __init__(self):
        self._job_category = None
        self._skip_risk_underwrite = None

    @property
    def job_category(self):
        return self._job_category

    @job_category.setter
    def job_category(self, value):
        self._job_category = value
    @property
    def skip_risk_underwrite(self):
        return self._skip_risk_underwrite

    @skip_risk_underwrite.setter
    def skip_risk_underwrite(self, value):
        self._skip_risk_underwrite = value


    def to_alipay_dict(self):
        params = dict()
        if self.job_category:
            if hasattr(self.job_category, 'to_alipay_dict'):
                params['job_category'] = self.job_category.to_alipay_dict()
            else:
                params['job_category'] = self.job_category
        if self.skip_risk_underwrite:
            if hasattr(self.skip_risk_underwrite, 'to_alipay_dict'):
                params['skip_risk_underwrite'] = self.skip_risk_underwrite.to_alipay_dict()
            else:
                params['skip_risk_underwrite'] = self.skip_risk_underwrite
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenSimplestIssueCustomParamDTO()
        if 'job_category' in d:
            o.job_category = d['job_category']
        if 'skip_risk_underwrite' in d:
            o.skip_risk_underwrite = d['skip_risk_underwrite']
        return o


