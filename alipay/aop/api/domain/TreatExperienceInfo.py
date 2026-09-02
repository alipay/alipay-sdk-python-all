#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TreatExperienceInfo(object):

    def __init__(self):
        self._count = None
        self._detail_url = None
        self._disease_id = None
        self._disease_name = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def disease_id(self):
        return self._disease_id

    @disease_id.setter
    def disease_id(self, value):
        self._disease_id = value
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.disease_id:
            if hasattr(self.disease_id, 'to_alipay_dict'):
                params['disease_id'] = self.disease_id.to_alipay_dict()
            else:
                params['disease_id'] = self.disease_id
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TreatExperienceInfo()
        if 'count' in d:
            o.count = d['count']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'disease_id' in d:
            o.disease_id = d['disease_id']
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        return o


