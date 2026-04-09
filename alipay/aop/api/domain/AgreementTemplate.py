#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgreementTemplate(object):

    def __init__(self):
        self._agreement_name = None
        self._agreement_template_id = None
        self._agreement_url = None

    @property
    def agreement_name(self):
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, value):
        self._agreement_name = value
    @property
    def agreement_template_id(self):
        return self._agreement_template_id

    @agreement_template_id.setter
    def agreement_template_id(self, value):
        self._agreement_template_id = value
    @property
    def agreement_url(self):
        return self._agreement_url

    @agreement_url.setter
    def agreement_url(self, value):
        self._agreement_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_name:
            if hasattr(self.agreement_name, 'to_alipay_dict'):
                params['agreement_name'] = self.agreement_name.to_alipay_dict()
            else:
                params['agreement_name'] = self.agreement_name
        if self.agreement_template_id:
            if hasattr(self.agreement_template_id, 'to_alipay_dict'):
                params['agreement_template_id'] = self.agreement_template_id.to_alipay_dict()
            else:
                params['agreement_template_id'] = self.agreement_template_id
        if self.agreement_url:
            if hasattr(self.agreement_url, 'to_alipay_dict'):
                params['agreement_url'] = self.agreement_url.to_alipay_dict()
            else:
                params['agreement_url'] = self.agreement_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgreementTemplate()
        if 'agreement_name' in d:
            o.agreement_name = d['agreement_name']
        if 'agreement_template_id' in d:
            o.agreement_template_id = d['agreement_template_id']
        if 'agreement_url' in d:
            o.agreement_url = d['agreement_url']
        return o


