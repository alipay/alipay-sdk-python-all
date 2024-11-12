#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhoneCardAgreementModel(object):

    def __init__(self):
        self._agreement_content = None
        self._agreement_id = None
        self._agreement_title = None
        self._agreement_type = None

    @property
    def agreement_content(self):
        return self._agreement_content

    @agreement_content.setter
    def agreement_content(self, value):
        self._agreement_content = value
    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def agreement_title(self):
        return self._agreement_title

    @agreement_title.setter
    def agreement_title(self, value):
        self._agreement_title = value
    @property
    def agreement_type(self):
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_content:
            if hasattr(self.agreement_content, 'to_alipay_dict'):
                params['agreement_content'] = self.agreement_content.to_alipay_dict()
            else:
                params['agreement_content'] = self.agreement_content
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.agreement_title:
            if hasattr(self.agreement_title, 'to_alipay_dict'):
                params['agreement_title'] = self.agreement_title.to_alipay_dict()
            else:
                params['agreement_title'] = self.agreement_title
        if self.agreement_type:
            if hasattr(self.agreement_type, 'to_alipay_dict'):
                params['agreement_type'] = self.agreement_type.to_alipay_dict()
            else:
                params['agreement_type'] = self.agreement_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhoneCardAgreementModel()
        if 'agreement_content' in d:
            o.agreement_content = d['agreement_content']
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'agreement_title' in d:
            o.agreement_title = d['agreement_title']
        if 'agreement_type' in d:
            o.agreement_type = d['agreement_type']
        return o


