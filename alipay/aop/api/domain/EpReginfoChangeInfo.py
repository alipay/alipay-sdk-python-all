#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpReginfoChangeInfo(object):

    def __init__(self):
        self._after_change = None
        self._before_change = None
        self._change_date = None
        self._change_matter = None
        self._change_matter_details = None

    @property
    def after_change(self):
        return self._after_change

    @after_change.setter
    def after_change(self, value):
        self._after_change = value
    @property
    def before_change(self):
        return self._before_change

    @before_change.setter
    def before_change(self, value):
        self._before_change = value
    @property
    def change_date(self):
        return self._change_date

    @change_date.setter
    def change_date(self, value):
        self._change_date = value
    @property
    def change_matter(self):
        return self._change_matter

    @change_matter.setter
    def change_matter(self, value):
        self._change_matter = value
    @property
    def change_matter_details(self):
        return self._change_matter_details

    @change_matter_details.setter
    def change_matter_details(self, value):
        self._change_matter_details = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_change:
            if hasattr(self.after_change, 'to_alipay_dict'):
                params['after_change'] = self.after_change.to_alipay_dict()
            else:
                params['after_change'] = self.after_change
        if self.before_change:
            if hasattr(self.before_change, 'to_alipay_dict'):
                params['before_change'] = self.before_change.to_alipay_dict()
            else:
                params['before_change'] = self.before_change
        if self.change_date:
            if hasattr(self.change_date, 'to_alipay_dict'):
                params['change_date'] = self.change_date.to_alipay_dict()
            else:
                params['change_date'] = self.change_date
        if self.change_matter:
            if hasattr(self.change_matter, 'to_alipay_dict'):
                params['change_matter'] = self.change_matter.to_alipay_dict()
            else:
                params['change_matter'] = self.change_matter
        if self.change_matter_details:
            if hasattr(self.change_matter_details, 'to_alipay_dict'):
                params['change_matter_details'] = self.change_matter_details.to_alipay_dict()
            else:
                params['change_matter_details'] = self.change_matter_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpReginfoChangeInfo()
        if 'after_change' in d:
            o.after_change = d['after_change']
        if 'before_change' in d:
            o.before_change = d['before_change']
        if 'change_date' in d:
            o.change_date = d['change_date']
        if 'change_matter' in d:
            o.change_matter = d['change_matter']
        if 'change_matter_details' in d:
            o.change_matter_details = d['change_matter_details']
        return o


