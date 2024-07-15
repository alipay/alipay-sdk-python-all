#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SiteSelectionParam import SiteSelectionParam


class AlipayCommerceTransportChargerSiteselectionCreateModel(object):

    def __init__(self):
        self._site_selection_param = None
        self._template_code = None

    @property
    def site_selection_param(self):
        return self._site_selection_param

    @site_selection_param.setter
    def site_selection_param(self, value):
        if isinstance(value, SiteSelectionParam):
            self._site_selection_param = value
        else:
            self._site_selection_param = SiteSelectionParam.from_alipay_dict(value)
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.site_selection_param:
            if hasattr(self.site_selection_param, 'to_alipay_dict'):
                params['site_selection_param'] = self.site_selection_param.to_alipay_dict()
            else:
                params['site_selection_param'] = self.site_selection_param
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerSiteselectionCreateModel()
        if 'site_selection_param' in d:
            o.site_selection_param = d['site_selection_param']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


