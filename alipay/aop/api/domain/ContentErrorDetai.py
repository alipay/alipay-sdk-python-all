#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentErrorLine import ContentErrorLine


class ContentErrorDetai(object):

    def __init__(self):
        self._error_contents = None
        self._unique_id = None

    @property
    def error_contents(self):
        return self._error_contents

    @error_contents.setter
    def error_contents(self, value):
        if isinstance(value, list):
            self._error_contents = list()
            for i in value:
                if isinstance(i, ContentErrorLine):
                    self._error_contents.append(i)
                else:
                    self._error_contents.append(ContentErrorLine.from_alipay_dict(i))
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_contents:
            if isinstance(self.error_contents, list):
                for i in range(0, len(self.error_contents)):
                    element = self.error_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.error_contents[i] = element.to_alipay_dict()
            if hasattr(self.error_contents, 'to_alipay_dict'):
                params['error_contents'] = self.error_contents.to_alipay_dict()
            else:
                params['error_contents'] = self.error_contents
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentErrorDetai()
        if 'error_contents' in d:
            o.error_contents = d['error_contents']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


