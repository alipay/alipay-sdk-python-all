#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertContentShareCode(object):

    def __init__(self):
        self._share_code_desc = None

    @property
    def share_code_desc(self):
        return self._share_code_desc

    @share_code_desc.setter
    def share_code_desc(self, value):
        self._share_code_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.share_code_desc:
            if hasattr(self.share_code_desc, 'to_alipay_dict'):
                params['share_code_desc'] = self.share_code_desc.to_alipay_dict()
            else:
                params['share_code_desc'] = self.share_code_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertContentShareCode()
        if 'share_code_desc' in d:
            o.share_code_desc = d['share_code_desc']
        return o


