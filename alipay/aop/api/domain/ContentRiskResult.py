#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentRiskDetail import ContentRiskDetail
from alipay.aop.api.domain.ContentRisks import ContentRisks


class ContentRiskResult(object):

    def __init__(self):
        self._content_risk_details = None
        self._contents = None
        self._result = None
        self._rl_cnt = None

    @property
    def content_risk_details(self):
        return self._content_risk_details

    @content_risk_details.setter
    def content_risk_details(self, value):
        if isinstance(value, list):
            self._content_risk_details = list()
            for i in value:
                if isinstance(i, ContentRiskDetail):
                    self._content_risk_details.append(i)
                else:
                    self._content_risk_details.append(ContentRiskDetail.from_alipay_dict(i))
    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        if isinstance(value, list):
            self._contents = list()
            for i in value:
                if isinstance(i, ContentRisks):
                    self._contents.append(i)
                else:
                    self._contents.append(ContentRisks.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def rl_cnt(self):
        return self._rl_cnt

    @rl_cnt.setter
    def rl_cnt(self, value):
        self._rl_cnt = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_risk_details:
            if isinstance(self.content_risk_details, list):
                for i in range(0, len(self.content_risk_details)):
                    element = self.content_risk_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_risk_details[i] = element.to_alipay_dict()
            if hasattr(self.content_risk_details, 'to_alipay_dict'):
                params['content_risk_details'] = self.content_risk_details.to_alipay_dict()
            else:
                params['content_risk_details'] = self.content_risk_details
        if self.contents:
            if isinstance(self.contents, list):
                for i in range(0, len(self.contents)):
                    element = self.contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contents[i] = element.to_alipay_dict()
            if hasattr(self.contents, 'to_alipay_dict'):
                params['contents'] = self.contents.to_alipay_dict()
            else:
                params['contents'] = self.contents
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.rl_cnt:
            if hasattr(self.rl_cnt, 'to_alipay_dict'):
                params['rl_cnt'] = self.rl_cnt.to_alipay_dict()
            else:
                params['rl_cnt'] = self.rl_cnt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentRiskResult()
        if 'content_risk_details' in d:
            o.content_risk_details = d['content_risk_details']
        if 'contents' in d:
            o.contents = d['contents']
        if 'result' in d:
            o.result = d['result']
        if 'rl_cnt' in d:
            o.rl_cnt = d['rl_cnt']
        return o


