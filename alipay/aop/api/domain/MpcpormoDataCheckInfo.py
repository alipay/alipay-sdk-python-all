#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcpormoDataCheckInfo(object):

    def __init__(self):
        self._check_info = None
        self._id = None
        self._title = None

    @property
    def check_info(self):
        return self._check_info

    @check_info.setter
    def check_info(self, value):
        self._check_info = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_info:
            if hasattr(self.check_info, 'to_alipay_dict'):
                params['check_info'] = self.check_info.to_alipay_dict()
            else:
                params['check_info'] = self.check_info
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        o = MpcpormoDataCheckInfo()
        if 'check_info' in d:
            o.check_info = d['check_info']
        if 'id' in d:
            o.id = d['id']
        if 'title' in d:
            o.title = d['title']
        return o


