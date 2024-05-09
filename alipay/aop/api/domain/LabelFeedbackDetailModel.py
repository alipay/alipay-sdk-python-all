#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LabelFeedbackDetailModel(object):

    def __init__(self):
        self._action_content = None
        self._action_count = None
        self._action_date = None
        self._action_type = None
        self._count_type = None
        self._ep_cert_no = None

    @property
    def action_content(self):
        return self._action_content

    @action_content.setter
    def action_content(self, value):
        if isinstance(value, list):
            self._action_content = list()
            for i in value:
                self._action_content.append(i)
    @property
    def action_count(self):
        return self._action_count

    @action_count.setter
    def action_count(self, value):
        self._action_count = value
    @property
    def action_date(self):
        return self._action_date

    @action_date.setter
    def action_date(self, value):
        self._action_date = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def count_type(self):
        return self._count_type

    @count_type.setter
    def count_type(self, value):
        self._count_type = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_content:
            if isinstance(self.action_content, list):
                for i in range(0, len(self.action_content)):
                    element = self.action_content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.action_content[i] = element.to_alipay_dict()
            if hasattr(self.action_content, 'to_alipay_dict'):
                params['action_content'] = self.action_content.to_alipay_dict()
            else:
                params['action_content'] = self.action_content
        if self.action_count:
            if hasattr(self.action_count, 'to_alipay_dict'):
                params['action_count'] = self.action_count.to_alipay_dict()
            else:
                params['action_count'] = self.action_count
        if self.action_date:
            if hasattr(self.action_date, 'to_alipay_dict'):
                params['action_date'] = self.action_date.to_alipay_dict()
            else:
                params['action_date'] = self.action_date
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.count_type:
            if hasattr(self.count_type, 'to_alipay_dict'):
                params['count_type'] = self.count_type.to_alipay_dict()
            else:
                params['count_type'] = self.count_type
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LabelFeedbackDetailModel()
        if 'action_content' in d:
            o.action_content = d['action_content']
        if 'action_count' in d:
            o.action_count = d['action_count']
        if 'action_date' in d:
            o.action_date = d['action_date']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'count_type' in d:
            o.count_type = d['count_type']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        return o


