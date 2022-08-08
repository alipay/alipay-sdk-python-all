#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasFormtemplateQueryModel(object):

    def __init__(self):
        self._form_template_id = None

    @property
    def form_template_id(self):
        return self._form_template_id

    @form_template_id.setter
    def form_template_id(self, value):
        self._form_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.form_template_id:
            if hasattr(self.form_template_id, 'to_alipay_dict'):
                params['form_template_id'] = self.form_template_id.to_alipay_dict()
            else:
                params['form_template_id'] = self.form_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasFormtemplateQueryModel()
        if 'form_template_id' in d:
            o.form_template_id = d['form_template_id']
        return o


