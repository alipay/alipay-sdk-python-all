#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgreementTextInfo(object):

    def __init__(self):
        self._agreement_text_title = None
        self._agreement_text_url = None

    @property
    def agreement_text_title(self):
        return self._agreement_text_title

    @agreement_text_title.setter
    def agreement_text_title(self, value):
        self._agreement_text_title = value
    @property
    def agreement_text_url(self):
        return self._agreement_text_url

    @agreement_text_url.setter
    def agreement_text_url(self, value):
        self._agreement_text_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_text_title:
            if hasattr(self.agreement_text_title, 'to_alipay_dict'):
                params['agreement_text_title'] = self.agreement_text_title.to_alipay_dict()
            else:
                params['agreement_text_title'] = self.agreement_text_title
        if self.agreement_text_url:
            if hasattr(self.agreement_text_url, 'to_alipay_dict'):
                params['agreement_text_url'] = self.agreement_text_url.to_alipay_dict()
            else:
                params['agreement_text_url'] = self.agreement_text_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementTextInfo()
        if 'agreement_text_title' in d:
            o.agreement_text_title = d['agreement_text_title']
        if 'agreement_text_url' in d:
            o.agreement_text_url = d['agreement_text_url']
        return o


