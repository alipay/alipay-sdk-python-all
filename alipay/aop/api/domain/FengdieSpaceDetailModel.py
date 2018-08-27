#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieSpaceDomains import FengdieSpaceDomains


class FengdieSpaceDetailModel(object):

    def __init__(self):
        self._domains = None
        self._gmt_create = None
        self._space_id = None
        self._title = None

    @property
    def domains(self):
        return self._domains

    @domains.setter
    def domains(self, value):
        if isinstance(value, list):
            self._domains = list()
            for i in value:
                if isinstance(i, FengdieSpaceDomains):
                    self._domains.append(i)
                else:
                    self._domains.append(FengdieSpaceDomains.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.domains:
            if isinstance(self.domains, list):
                for i in range(0, len(self.domains)):
                    element = self.domains[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.domains[i] = element.to_alipay_dict()
            if hasattr(self.domains, 'to_alipay_dict'):
                params['domains'] = self.domains.to_alipay_dict()
            else:
                params['domains'] = self.domains
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieSpaceDetailModel()
        if 'domains' in d:
            o.domains = d['domains']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'space_id' in d:
            o.space_id = d['space_id']
        if 'title' in d:
            o.title = d['title']
        return o


