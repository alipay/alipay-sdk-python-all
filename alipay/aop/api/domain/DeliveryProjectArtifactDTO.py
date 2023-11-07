#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryProjectArtifactDTO(object):

    def __init__(self):
        self._fullname = None
        self._id = None
        self._source = None

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, value):
        self._fullname = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.fullname:
            if hasattr(self.fullname, 'to_alipay_dict'):
                params['fullname'] = self.fullname.to_alipay_dict()
            else:
                params['fullname'] = self.fullname
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryProjectArtifactDTO()
        if 'fullname' in d:
            o.fullname = d['fullname']
        if 'id' in d:
            o.id = d['id']
        if 'source' in d:
            o.source = d['source']
        return o


