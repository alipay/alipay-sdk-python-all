#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitDisplayInfo(object):

    def __init__(self):
        self._benefit_description = None
        self._benefit_icon_url = None
        self._benefit_name = None
        self._pass_through_info = None

    @property
    def benefit_description(self):
        return self._benefit_description

    @benefit_description.setter
    def benefit_description(self, value):
        self._benefit_description = value
    @property
    def benefit_icon_url(self):
        return self._benefit_icon_url

    @benefit_icon_url.setter
    def benefit_icon_url(self, value):
        self._benefit_icon_url = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_description:
            if hasattr(self.benefit_description, 'to_alipay_dict'):
                params['benefit_description'] = self.benefit_description.to_alipay_dict()
            else:
                params['benefit_description'] = self.benefit_description
        if self.benefit_icon_url:
            if hasattr(self.benefit_icon_url, 'to_alipay_dict'):
                params['benefit_icon_url'] = self.benefit_icon_url.to_alipay_dict()
            else:
                params['benefit_icon_url'] = self.benefit_icon_url
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDisplayInfo()
        if 'benefit_description' in d:
            o.benefit_description = d['benefit_description']
        if 'benefit_icon_url' in d:
            o.benefit_icon_url = d['benefit_icon_url']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        return o


